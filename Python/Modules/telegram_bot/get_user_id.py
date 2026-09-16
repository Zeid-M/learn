import json

import requests


def get_user_id(bot_token: str):
    # Send a GET request to the Telegram Bot API to get the latest updates
    response = requests.get(f"https://api.telegram.org/bot{bot_token}/getUpdates")

    # Decode the response content from JSON format to a Python dictionary
    response = json.loads(response.content.decode("utf-8"))

    # Check if the 'result' field in the response is empty
    if not response["result"]:
        # Print a message if there are no updates
        print("Updates are empty")
        return

    # Extract the user ID from the first update in the 'result' list
    user_id = response["result"][0]["message"]["chat"]["id"]

    # Extract the update ID and increment it by 1 to acknowledge the update
    update_id = response["result"][0]["update_id"] + 1

    # Send another GET request to the Telegram Bot API with an offset to confirm the update
    response = requests.get(
        f"https://api.telegram.org/bot{bot_token}/getUpdates?offset={update_id}"
    )

    # Return the extracted user ID
    return user_id


if __name__ == "__main__":

    bot_token = ""
    print(get_user_id(bot_token))
