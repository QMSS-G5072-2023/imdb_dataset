import requests


class ApiInitialize:
    def __init__(self, api_key: str):
        """ApiInitialize.

        Args:
            api_key : api_key from https://rapidapi.com/SAdrian/api/moviesdatabase
        """

        self.api_key = api_key
        self.headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
        }
        self.validate_api()

    def validate_api(self):
        url = "https://moviesdatabase.p.rapidapi.com/titles/utils/titleTypes"
        response = requests.get(url, headers = self.headers)

        # Verify whether the API return is successful (status code is 200)
        if response.status_code == 200:
            pass
        else:
            print(f"API request failed with status code {response.status_code}. Maybe the key is entered incorrectly or the access is restricted.")

    def _get_genres_results(self):
        url = "https://moviesdatabase.p.rapidapi.com/titles/utils/genres"
        response = requests.get(url, headers = self.headers)
        genres = response.json()['results']
        return genres

    def _get_lists_results(self):
        url = "https://moviesdatabase.p.rapidapi.com/titles/utils/lists"
        response = requests.get(url, headers = self.headers)
        lists = response.json()['results']
        return lists

    def _get_titleTypes_results(self):
        url = "https://moviesdatabase.p.rapidapi.com/titles/utils/titleTypes"
        response = requests.get(url, headers = self.headers)
        titleTypes = response.json()['results']
        return titleTypes

    def get_utils(self):
        genres = self._get_genres_results()
        lists = self._get_lists_results()
        titleTypes = self._get_titleTypes_results()
        return genres, lists, titleTypes
