import requests


class Python_Repos:
    def __init__(self):
        self.url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
        self.headers = {'Accept': 'application/vnd.github.v3+json'}
        self.r = requests.get(self.url, headers=self.headers)
        self.status_code = self.r.status_code

        # Store api response in a variable
        self.response_dict = self.r.json()

    def get_num_items(self):
        return len(self.response_dict['items'])
