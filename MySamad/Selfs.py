import requests
from telegram.ext import CallbackQueryHandler

import App
import CallBackQueries

def get_self_list(token: str):
    url = "https://setad.dining.sharif.edu/rest/selfs"

    response = requests.get(url, headers={"Authorization": f"Bearer {token}"})

    selfs_list = {}

    if response.status_code == 200:
        response = response.json()
        for self in response['payload']:
            selfs_list.update({self['name']: self['id']})
    else:
        print("Error in fetching selfs list")

    return selfs_list


class CallBackQueryHandler:
    pass


def create_selfs_callback_handler(selfs_list: dict) -> str:
    regex = ""
    for self_name in selfs_list:
        regex += f"{self_name}|"

    regex = regex.replace("(", r"\(")
    regex = regex.replace(")", r"\)")
    App.app.add_handler(CallbackQueryHandler(CallBackQueries.selfs_callback_handler, pattern=regex[:-1]))
    return regex[:-1]
