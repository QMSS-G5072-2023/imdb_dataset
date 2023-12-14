import numpy as np
import requests
from urllib.parse import quote
import pandas as pd
from imdb_dataset import api_initialize
import copy


class MovieSearch:
    def __init__(self, api_key: str, string = '', mode: str = 'title', option = {}):
        """
        Search related information of movies according to five modes.

        Args:
            api_key (str): The API key for authentication.
            string (str): Enter search content according to different modes.
            mode (str, optional): The mode of the API (default is 'title').
            option (dict, optional): Additional options for API initialization (default is an empty dictionary).

        Note:
            - The `mode` parameter specifies the mode of the API (e.g., 'title' mode).
            - The `option` parameter allows passing additional options as a dictionary.

        Example:
            >>> api_initialize("your_api_key", mode='title', option={'titleType': 'movie'})

        """

        self.api_key = api_key
        self.mode = mode
        self.option = option
        self.utils = api_initialize.ApiInitialize(api_key).get_utils()

        # URL encoding
        self.url = f"https://moviesdatabase.p.rapidapi.com/titles/search/{mode}/{quote(string)}"
        self.headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
        }
        self._validate_mode()
        self._validate_option()

    def _validate_mode(self):
        # Set of expected modes
        expected_modes = {'title', 'akas', 'keyword', 'id', 'genre'}

        # Check if the provided mode is in the expected set
        if self.mode not in expected_modes:
            raise ValueError(f"Error: Invalid mode. Expected modes: {expected_modes}")

    def _validate_option(self):
        # Set of expected keys
        expected_keys = {'startYear', 'endYear', 'page', 'limit', 'titleType'}

        # Check if all keys are in the expected set
        invalid_keys = set(self.option.keys()) - expected_keys
        if invalid_keys:
            raise ValueError("Error: Invalid keys in 'option'. Unexpected keys:", invalid_keys)

        # Check if values are integers, except for 'titleType'
        for key, value in self.option.items():
            if key == 'titleType':
                if value is not None and not isinstance(value, str):
                    raise ValueError(f"Error: Value for 'titleType' must be a string or None.")
            elif not isinstance(value, int):
                raise ValueError(f"Error: Value for '{key}' must be an integer.")

            # Check if 'limit' does not exceed 50
            if 'limit' in self.option and self.option['limit'] > 50:
                raise ValueError("Error: 'limit' cannot exceed 50.")

        self.option['titleType'] = self._validate_titleType(self.option.get('titleType'))

    def _validate_genres(self, genres):
        allowed_genres = self.utils[0]

        # Check if genres is not None before using lower()
        if genres is not None:
            allowed_genres = [genre for genre in allowed_genres if genre is not None]

            # Convert the input genres to lowercase
            genres_lower = genres.lower()

            # Check if it's in the lowercase form of allowed_genres
            if genres_lower not in [genre.lower() for genre in allowed_genres]:
                raise ValueError("Error: Invalid 'genres' value. Expected values:", allowed_genres)
            else:
                # Replace genres with the corresponding lowercase value from allowed_genres
                genres = next(genre for genre in allowed_genres if genre.lower() == genres_lower)

        return genres

    def _validate_lists(self, lists):
        allowed_lists = self.utils[1]

        # Check if lists is not None before using lower()
        if lists is not None:
            allowed_lists = [i for i in allowed_lists if i is not None]

            # Convert the input lists to lowercase
            lists_lower = lists.lower()

            # Check if it's in the lowercase form of allowed_lists
            if lists_lower not in [i.lower() for i in allowed_lists]:
                raise ValueError("Error: Invalid 'lists' value. Expected values:", allowed_lists)
            else:
                # Replace lists with the corresponding lowercase value from allowed_lists
                lists = next(i for i in allowed_lists if i.lower() == lists_lower)

        return lists

    def _validate_titleType(self, titleType):
        allowed_titleType = self.utils[2]

        # Check if titleType is not None before using lower()
        if titleType is not None:
            allowed_titleType = [i for i in allowed_titleType if i is not None]

            # Convert the input titleType to lowercase
            titleType_lower = titleType.lower()

            # Check if it's in the lowercase form of allowed_titleType
            if titleType_lower not in [i.lower() for i in allowed_titleType]:
                raise ValueError("Error: Invalid 'titleType' value. Expected values:", allowed_titleType)
            else:
                # Replace titleType with the corresponding lowercase value from allowed_titleType
                titleType = next(i for i in allowed_titleType if i.lower() == titleType_lower)

        return titleType

    def get_akas_results(self):
        params = copy.deepcopy(self.option)
        api_results = requests.get(self.url, headers = self.headers, params = params).json()
        data = pd.json_normalize(api_results['results'])

        if len(data) != 0:
            data['releaseDate'] = data[
                ['releaseDate.year', 'releaseDate.month', 'releaseDate.day']].astype(str).agg('-'.join, axis = 1)
            data['releaseDate'] = pd.to_datetime(data['releaseDate'])
            columns = ['id', 'primaryImage.url', 'primaryImage.caption.plainText', 'titleType.text', 'releaseDate']
            data = data[columns]
            data.columns = ['imdbId', 'imgUrl', 'imdbTitle', 'titleType', 'releaseDate']
        return data

    def get_keyword_results(self):
        params = copy.deepcopy(self.option)
        api_results = requests.get(self.url, headers = self.headers, params = params).json()
        data = pd.json_normalize(api_results['results'])

        if len(data) != 0:
            data['releaseDate'] = data[
                ['releaseDate.year', 'releaseDate.month', 'releaseDate.day']].astype(str).agg('-'.join, axis = 1)
            data['releaseDate'] = pd.to_datetime(data['releaseDate'])
            columns = ['id', 'primaryImage.url', 'primaryImage.caption.plainText', 'titleType.text', 'releaseDate']
            data = data[columns]
            data.columns = ['imdbId', 'imgUrl', 'imdbTitle', 'titleType', 'releaseDate']
        return data

    def get_title_results(self, exact = True, list = 'titles'):
        params = copy.deepcopy(self.option)
        list = self._validate_lists(list)

        assert isinstance(exact, bool), "exact parameter must be boolean."

        if exact:
            params['exact'] = 'true'
        else:
            params['exact'] = 'false'

        params['list'] = list

        api_results = requests.get(self.url, headers = self.headers, params = params).json()
        data = pd.json_normalize(api_results['results'])

        if len(data) != 0:
            data['releaseDate'] = data[
                ['releaseDate.year', 'releaseDate.month', 'releaseDate.day']].astype(str).agg('-'.join, axis = 1)
            data['releaseDate'] = pd.to_datetime(data['releaseDate'])
            columns = ['id', 'primaryImage.url', 'primaryImage.caption.plainText', 'titleType.text', 'releaseDate']
            data = data[columns]
            data.columns = ['imdbId', 'imgUrl', 'imdbTitle', 'titleType', 'releaseDate']
        return data

    def get_id_results(self, id):
        url = f"https://moviesdatabase.p.rapidapi.com/titles/{id}"
        api_results = requests.get(url, headers = self.headers).json()
        data = pd.json_normalize(api_results['results'])

        if len(data) != 0:
            title = data['titleText.text'][0]
            params = copy.deepcopy(self.option)
            search = MovieSearch(self.api_key, string = title, mode = 'title', option = params)
            data = search.get_title_results()

        return data

    def get_genre_results(self, genre = "Drama"):
        url = "https://moviesdatabase.p.rapidapi.com/titles"

        params = copy.deepcopy(self.option)
        genre = self._validate_genres(genre)
        params['genre'] = genre

        api_results = requests.get(url, headers = self.headers, params = params).json()
        data = pd.json_normalize(api_results['results'])

        if len(data) != 0:
            data[['releaseDate.year', 'releaseDate.month', 'releaseDate.day']] = data[
                ['releaseDate.year', 'releaseDate.month', 'releaseDate.day']].fillna(0).astype(int)
            data['releaseDate'] = data[
                ['releaseDate.year', 'releaseDate.month', 'releaseDate.day']].astype(str).agg('-'.join, axis = 1)
            data['releaseDate'] = data['releaseDate'].replace('0-0-0', '2199-12-31')
            data['releaseDate'] = pd.to_datetime(data['releaseDate'])
            columns = ['id', 'primaryImage.url', 'primaryImage.caption.plainText', 'titleType.text', 'releaseDate']
            data = data[columns]
            data.columns = ['imdbId', 'imgUrl', 'imdbTitle', 'titleType', 'releaseDate']
            data.loc[data['releaseDate'] == pd.Timestamp('2199-12-31'), 'releaseDate'] = np.NaN

        return data
