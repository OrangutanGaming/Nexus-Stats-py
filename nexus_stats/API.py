import requests
from nexus_stats.Profile import Profile

class Requester():
    def __init__(self):
        self.url = "https://api.nexus-stats.com/warframe/v1"

    def get_user_profile(self, userName):
        response = Profile(self.url, userName)
        return response
