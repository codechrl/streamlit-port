import requests
from bs4 import BeautifulSoup

BASE_URL = "https://twitter.com/"


def scrap(username):
    response = requests.get(BASE_URL + username)
