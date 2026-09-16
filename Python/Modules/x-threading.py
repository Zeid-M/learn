import queue
import threading
import time

# Schedule Library imported
import schedule
from icecream import ic

done = False


q = queue.PriorityQueue()

q.put((1, "a"))
q.put((2, "b"))
q.put((3, "f"))
q.put((2, "g"))
q.put((4, "hj"))


ic(q.qsize())


def len_q():
    for i in range(q.qsize()):
        time.sleep(2)
        ic()
        ic(i)


def counting(name):
    counter = 0
    while not done:
        time.sleep(1)
        counter += 1
        ic(f"{name}: {counter}")


# counting()

t1 = threading.Thread(target=counting, daemon=True, args=("T1",))
t2 = threading.Thread(target=counting, daemon=True, args=("T2",))
t3 = threading.Thread(target=len_q)

# t1.start()
# t2.start()

t3.start()

# Wait for the thread to finish
# t1.join()
# t2.join()
a = 8
while True:
    # a = tuple(input("Press Enter to stop"))
    time.sleep(1)
    a += 1
    q.put((a, "aa"))
    ic(q.qsize())

done = True

# Program to demonstrate
# timer objects in python


def gfg():
    print("GeeksforGeeks\n")


timer = threading.Timer(2.0, gfg)
timer.start()
print("Exit\n")
