import requests
from datetime import datetime, timedelta


def getThisWeekReservationOptionsList(token: str, self_id: str):
    foods_list = {
        "Saturday": None,
        "Sunday": None,
        "Monday": None,
        "Tuesday": None,
        "Wednesday": None,
        "Thursday": None,
        "Friday": None
    }

    today = datetime.today()
    saturday = today - timedelta((today.weekday() + 2) % 7)
    saturday_str = saturday.strftime('%Y-%m-%d')
    url = f"https://setad.dining.sharif.edu/rest/programs/v2?selfId={self_id}&weekStartDate={saturday_str}" + "+00:00:00"

    response = requests.get(url, headers={"Authorization": f"Bearer {token}"})

    if response.status_code == 200:
        response = response.json()
        for programs_of_day in response['payload']['selfWeekPrograms']:
            program_list = []
            for program in programs_of_day:
                program_list.append(program['foodName'])

            foods_list[program['dayTranslated']] = program_list

    return foods_list

def getThisWeekReserverdFoodsList(token: str, self_id: str):
    foods_list ={
        "Saturday": {
            "lunch": None,
            "dinner": None
        },
        "Sunday": {
            "lunch": None,
            "dinner": None
        },
        "Monday": {
            "lunch": None,
            "dinner": None
        },
        "Tuesday": {
            "lunch": None,
            "dinner": None
        },
        "Wednesday": {
            "lunch": None,
            "dinner": None
        },
        "Thursday": {
            "lunch": None,
            "dinner": None
        },
        "Friday": {
            "lunch": None,
            "dinner": None
        }
    }

    today = datetime.today()
    saturday = today - timedelta((today.weekday() + 2) % 7)
    saturday_str = saturday.strftime('%Y-%m-%d')
    url = f"https://setad.dining.sharif.edu/rest/programs/v2?selfId={self_id}&weekStartDate={saturday_str}" + "+00:00:00"

    response = requests.get(url, headers={"Authorization": f"Bearer {token}"})

    if response.status_code == 200:
        response = response.json()


def beautifyReservationOptionsList(reservation_options_list: dict):
    reservation_options_string = ""
    try:
        for day, foods in reservation_options_list.items():
            reservation_options_string += f"{day}:\n"
            if foods is not None:
                for food in foods:
                    reservation_options_string += f"  - {food}\n"
    except Exception as e:
        reservation_options_string = f"Error in fetching reservation options: {str(e)}. Please try again later."

    return reservation_options_string

def get_weekday_name(date_str):
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    weekday_name = date_obj.strftime('%A')
    return weekday_name