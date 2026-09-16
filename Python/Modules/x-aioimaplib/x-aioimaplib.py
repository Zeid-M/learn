import asyncio
import imaplib
import ssl
from email.parser import BytesHeaderParser
from email.utils import parsedate_to_datetime
from time import sleep

from aioimaplib import STOP_WAIT_SERVER_PUSH, aioimaplib


async def get_client(host, user, pwd):
    client = aioimaplib.IMAP4_SSL(host)
    await client.wait_hello_from_server()
    await client.login(user=user, password=pwd)

    return client


async def check_mailbox(host, user, password):
    imap_client = aioimaplib.IMAP4_SSL(host=host)
    await imap_client.wait_hello_from_server()

    await imap_client.login(user, password)

    res, data = await imap_client.select()
    print("there is %s messages INBOX" % data[0])

    await imap_client.logout()


async def wait_for_new_message_old(host, user, password):
    imap_client = aioimaplib.IMAP4_SSL(host=host)
    await imap_client.wait_hello_from_server()

    await imap_client.login(user, password)
    await imap_client.select()

    res, unseen = await imap_client.uid_search("UNSEEN")
    parser = BytesHeaderParser()
    print(f"{res=}")
    for raw_uid in unseen[0].split():
        uid = raw_uid.decode()
        print(f"{uid=}")
        # 2. Fetch just the envelope for speed
        res = await imap_client.uid(
            "fetch", uid, "(BODY.PEEK[HEADER.FIELDS (SUBJECT DATE FROM)])"
        )
        print(f"{res=}")
        data = res.lines[1]
        print(f"{data=}")
        header = parser.parsebytes(bytes(data))
        date_str = header.get("Date")
        subject = header.get("Subject")
        from_header = header.get("From")
        dt = parsedate_to_datetime(date_str)

        print(f"{subject=}, {from_header=}, {dt=}")
        # print(f"{res=},{data=}")
        # subject_line = data[0][1].decode(errors="replace").strip()
        # print(f"{subject_line}")
    idle = await imap_client.idle_start(timeout=10)
    while imap_client.has_pending_idle():
        msg = await imap_client.wait_server_push()
        print(msg)
        if msg == STOP_WAIT_SERVER_PUSH:
            imap_client.idle_done()
            await asyncio.wait_for(idle, 1)

    await imap_client.logout()


# Create an SSL context that points at certifi’s bundle:


async def wait_for_new_message(host, user, password):
    ctx = ssl.create_default_context()  # secure defaults…
    ctx.check_hostname = False  # …but turn off hostname checks
    ctx.verify_mode = ssl.CERT_NONE
    imap_client = aioimaplib.IMAP4_SSL(host=host, ssl_context=ctx)
    await imap_client.wait_hello_from_server()

    await imap_client.login(user, password)
    await imap_client.select()
    print(9)
    idle = await imap_client.idle_start(timeout=5)
    print(1)
    while imap_client.has_pending_idle():
        msg = await imap_client.wait_server_push()
        imap_client.idle_done()
        print(msg)
        if msg == STOP_WAIT_SERVER_PUSH:
            print(2)
            await asyncio.wait_for(idle, 1)
        print(3)
        await on_new(imap_client)
    await imap_client.logout()


async def idle_loop(host, user, password):
    imap_client = aioimaplib.IMAP4_SSL(host=host, timeout=30)
    await imap_client.wait_hello_from_server()

    await imap_client.login(user, password)
    await imap_client.select()

    while True:
        print(
            (
                await imap_client.uid(
                    "fetch", "7610", "(BODY.PEEK[HEADER.FIELDS (SUBJECT)])"
                )
            )
        )

        idle = await imap_client.idle_start(timeout=60)
        print((await imap_client.wait_server_push()))

        imap_client.idle_done()
        await asyncio.wait_for(idle, 30)


async def on_new(imap_client):
    parser = BytesHeaderParser()
    res, unseen = await imap_client.uid_search("UNSEEN")
    print("start fetch unseen -------------------------------")
    for raw_uid in unseen[0].split():
        uid = raw_uid.decode()
        print(f"{uid=}")
        # 2. Fetch just the envelope for speed
        res = await imap_client.uid(
            "fetch", uid, "(BODY.PEEK[HEADER.FIELDS (SUBJECT DATE FROM)])"
        )
        # print(f"{res=}")
        data = res.lines[1]
        # print(f"{data=}")
        header = parser.parsebytes(bytes(data))
        date_str = header.get("Date")
        subject = header.get("Subject")
        from_header = header.get("From")
        dt = parsedate_to_datetime(date_str)

        print(f"{subject=}, {from_header=}, {dt=}")

    print("stop fetch unseen -------------------------------")


async def fetch_data(host, user, password):
    imap_client = aioimaplib.IMAP4_SSL(host=host)
    await imap_client.wait_hello_from_server()

    await imap_client.login(user, password)
    await imap_client.select()
    await on_new(imap_client)

    while True:
        idle = await imap_client.idle_start(timeout=10)
        msg = await imap_client.wait_server_push()  # blocks until EXISTS/EXPUNGE, etc.
        print(msg)
        if b"EXISTS" in msg[0]:
            await on_new(imap_client)  # e.g. fetch subject + relay to Telegram
        imap_client.idle_done()
        await asyncio.wait_for(idle, 10)


async def fetch_data2(host, user, password):
    imap_client = aioimaplib.IMAP4_SSL(host=host)
    await imap_client.wait_hello_from_server()

    await imap_client.login(user, password)
    await imap_client.select()

    parser = BytesHeaderParser()

    idle = await imap_client.idle_start(timeout=2)

    while imap_client.has_pending_idle():
        msg = await imap_client.wait_server_push()
        print(msg)
        if b"EXISTS" in msg[0]:
            res, unseen = await imap_client.uid_search("UNSEEN")
            print("start fetch unseen -------------------------------")
            for raw_uid in unseen[0].split():
                uid = raw_uid.decode()
                print(f"{uid=}")
                # 2. Fetch just the envelope for speed
                res = await imap_client.uid(
                    "fetch", uid, "(BODY.PEEK[HEADER.FIELDS (SUBJECT DATE FROM)])"
                )
                # print(f"{res=}")
                data = res.lines[1]
                # print(f"{data=}")
                header = parser.parsebytes(bytes(data))
                date_str = header.get("Date")
                subject = header.get("Subject")
                from_header = header.get("From")
                dt = parsedate_to_datetime(date_str)

                print(f"{subject=}, {from_header=}, {dt=}")

            print("stop fetch unseen -------------------------------")
        if msg == STOP_WAIT_SERVER_PUSH:
            imap_client.idle_done()
            await asyncio.wait_for(idle, 1)
            idle = await imap_client.idle_start(timeout=2)

    await imap_client.logout()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    # loop.run_until_complete(
    #     check_mailbox("imap.gmail.com", "zizo.bone@gmail.com", "oyvpxpnnpcdtjilv")
    # )
    loop.run_until_complete(
        wait_for_new_message("lin.scs-net.org", "dch@dch.syriatel.sy", "ScrEX63.X*90")
    )
    loop.run_until_complete(
        wait_for_new_message(
            "imap.gmail.com", "zizo.bone@gmail.com", "oyvpxpnnpcdtjilv"
        )
    )
    # loop.run_until_complete(
    #     idle_loop("imap.gmail.com", "zizo.bone@gmail.com", "oyvpxpnnpcdtjilv")
    # )
    # loop.run_until_complete(
    #     fetch_data("imap.gmail.com", "zizo.bone@gmail.com", "oyvpxpnnpcdtjilv")
    # )
    # loop.run_until_complete(
    #     fetch_data2("imap.gmail.com", "zizo.bone@gmail.com", "oyvpxpnnpcdtjilv")
    # )

async def get_client(host, user, password):
    ctx = ssl.create_default_context()  # secure defaults…
    ctx.check_hostname = False  # …but turn off hostname checks
    ctx.verify_mode = ssl.CERT_NONE
    imap_client = aioimaplib.IMAP4_SSL(host=host, ssl_context=ctx)
    await imap_client.wait_hello_from_server()
    await imap_client.login(user, password)

    return imap_client


async def wait_for_new_message(imap_client):

    await imap_client.select()

    idle = await imap_client.idle_start(timeout=10)

    while imap_client.has_pending_idle():
        msg = await imap_client.wait_server_push()
        imap_client.idle_done()
        await asyncio.wait_for(idle, 1)
        print(msg)
        if msg != STOP_WAIT_SERVER_PUSH:
            await fetch_unseen_emails(imap_client)

        idle = await imap_client.idle_start(timeout=5)

    await imap_client.logout()


async def fetch_unseen_emails(imap_client):
    parser = BytesHeaderParser()
    data_list = []
    res, unseen = await imap_client.uid_search("UNSEEN")
    print("start fetch unseen -------------------------------")
    for raw_uid in unseen[0].split():
        uid = raw_uid.decode()
        print(f"{uid=}")
        # 2. Fetch just the envelope for speed
        res = await imap_client.uid(
            "fetch", uid, "(BODY.PEEK[HEADER.FIELDS (SUBJECT DATE FROM)])"
        )
        # print(f"{res=}")
        data = res.lines[1]
        # print(f"{data=}")
        header = parser.parsebytes(bytes(data))

        date_str = header.get("Date")
        subject = header.get("Subject")
        from_header = header.get("From")
        dt = parsedate_to_datetime(date_str)
        data_list.append(
            {"uid": uid, "subject": subject, "sender": from_header, "timestamp": dt}
        )
        # print(f"{subject=}, {from_header=}, {dt=}")

    print("stop fetch unseen -------------------------------")
    return data_list


async def watch_email(host, user, password):

    imap_client = await get_client(host, user, password)

    await wait_for_new_message(imap_client)

