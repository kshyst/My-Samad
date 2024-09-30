import requests
import json


def getTokenResponse(username: str, password: str):
    url = "https://setad.dining.sharif.edu/oauth/token"
    headers = {
        "Authorization": "Basic c2FtYWQtbW9iaWxlOnNhbWFkLW1vYmlsZS1zZWNyZXQ=",
        "Content-Type": "application/x-www-form-urlencoded",
        "Accept": "application/json",
    }

    data = {
        "username": username,
        "password": password,
        "grant_type": "password"
    }

    response = requests.post(url, headers=headers, data=data)
    return response.json()


def getAccessToken(username: str, password: str):
    response = getTokenResponse(username, password)
    return response['access_token']

def getRefreshToken(username: str, password: str):
    response = getTokenResponse(username, password)
    return response['refresh_token']