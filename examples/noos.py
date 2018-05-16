# import requests


class noos:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        self.headers = {
            'User-Token': self.user,
            'Accept-Token': self.password,
        }
