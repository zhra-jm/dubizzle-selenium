import requests

from utils import get_cookies


class Crawler:

    def __init__(self):
        self.cookie = get_cookies()

    @staticmethod
    def get(link):
        try:
            response = requests.get(link, cookie=get_cookies())
        except requests.HTTPError:
            return None
        return response

