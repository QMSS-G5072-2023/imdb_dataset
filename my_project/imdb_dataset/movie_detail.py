import pandas as pd
import requests
from PIL import Image
from imdb_dataset.movie_search import MovieSearch


class MovieDetail:
    def __init__(self, api_key, data: pd.DataFrame):
        """ApiInitialize.
        Args:
            api_key : api_key.
        """

        self.api_key = api_key
        self.data = data

        # self.utils = api_initialize.ApiInitialize(api_key).get_utils()

        self.headers = {
            "X-RapidAPI-Key": api_key,
            "X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
        }

    def get_movie_ratings(self):
        ratings = pd.DataFrame()
        for id in self.data['imdbId']:
            url = f"https://moviesdatabase.p.rapidapi.com/titles/{id}/ratings"
            response = requests.get(url, headers = self.headers).json()
            data = pd.json_normalize(response['results'])
            ratings = pd.concat([ratings, data])

        ratings.rename(columns = {'tconst': 'imdbId'}, inplace = True)
        ratings = ratings.reset_index(drop = True)
        return ratings

    def get_movie_aka(self, id):
        url = f"https://moviesdatabase.p.rapidapi.com/titles/{id}/aka"
        response = requests.get(url, headers = self.headers).json()
        data = pd.json_normalize(response['results'])
        data.rename(columns = {'titleId': 'imdbId'}, inplace = True)
        data = data.reset_index(drop = True)
        return data

    def get_movie_poster(self, id, show = True, save = True):
        string = ''
        mode = 'id'
        option = {}

        search = MovieSearch(self.api_key, string, mode, option)
        data = search.get_id_results(id)
        imgUrl = data.loc[data['imdbId'] == id, 'imgUrl'].values[0]

        # Download the image
        response = requests.get(imgUrl, stream = True)
        img = Image.open(response.raw)

        if show:
            # Display the image
            img.show()

        if save:
            name = data.loc[data['imdbId'] == id, 'imdbTitle'].values[0]
            # Save the image
            img.save(f"{name}.jpg")
