# IMDB_Dataset API

[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

## Project Overview

The IMDB_Dataset API project aims to provide access to and manipulation of the IMDB dataset. This API offers various functionalities, including **API initialization**, **retrieving movie data**, and **searching for specific movies**.

## Features

Based on the three provided classes (`ApiInitialize`, `MovieDetail`, `MovieSearch`), the API has the following features:

- **Movie Database Access:**
  - The API provides an initialization class `ApiInitialize` to configure the API access with the necessary key and basic information.
  - The `validate_api` method of this class ensures the validity of API access, verifying the correctness of the API key and the ability to access the movie database.

- **Movie Search Functionality:**
  - Through the `MovieSearch` class, your API supports various search modes, including movie titles, aliases, keywords, IMDb IDs, and movie types.
  - During the search process, the API validates and processes search parameters to ensure that user input meets expectations.

- **Fetching Movie Details:**
  - With the `MovieDetail` class, the API provides the ability to retrieve detailed movie information, including movie ratings, aliases, and displaying posters.
  - These functionalities retrieve relevant information from the movie database based on the provided IMDb ID, organizing the information into an easily usable Pandas DataFrame.

- **Data Format Handling:**
  - The data returned by the API is presented in the form of Pandas DataFrames, making it easy to handle and analyze data in Python.
  - Movie search results, alias information, keyword information, etc., are all presented in tabular form, facilitating further operations and analysis by users.

- **Graphical Representation:**
  - The `MovieDetail` class supports retrieving movie posters and displaying them in the code or saving them as image files.
  - This provides users with a graphical way to visually showcase movie posters, enhancing the user experience.

- **API License and Services:**
  - The Apache License Version 2.0 mentioned in the README file indicates that the API uses this open-source license, allowing users to freely use, modify, and distribute the API under certain conditions.
  - The API's service is based on the RapidAPI platform, which may provide additional services and management features. Users can learn more about these features through RapidAPI.

## Getting Started

Here is a brief guide on how to set up and use the IMDBdataset API.

### Install Dependencies

```bash
# Use the following command to install the required dependencies
pip install -r requirements.txt
```

### Project Structure



### ![IMDB_DatasetClassDiagram](IMDB_DatasetClassDiagram.png)





### Quick Start Guide

#### 1. API Initialization

To get started with the IMDb Dataset API, you need to initialize the API by providing your Rapid API key. Follow these steps:

```python
from imdb_dataset.api_initialize import ApiInitialize

# Replace 'your_rapidapi_key' with your actual RapidAPI key
api_key = "your_rapidapi_key"

# Initialize the API
api = ApiInitialize(api_key)

# Get utility information such as genres, lists, and title types
genres, lists, titleTypes = api.get_utils()

# Print the utility information
print("Genres:", genres)
print("Lists:", lists)
print("Title Types:", titleTypes)
```



#### 2. Movie Search

Perform a movie search using different modes such as title, akas (also known as), keyword, id, or genre. Customize your search with additional options.

````python
#### 1. Search Movies by Also Known As (AKAs)

```python
from imdb_dataset.movie_search import MovieSearch

# Set up API key
api_key = "your_rapidapi_key"

# Perform AKAs search
string = '阿甘正传'
mode = 'akas'
option = {'startYear': 1991, 'endYear': 2023, 'page': 1, 'limit': 5, 'titleType': 'Movie'}

search = MovieSearch(api_key, string, mode, option)
data = search.get_akas_results()
print("AKAs Results:")
print(data)
```

#### 2. Search Movies by Keyword

```python
# Perform keyword search
string = 'forrest'
mode = 'keyword'
option = {'startYear': 1991, 'endYear': 2023, 'page': 1, 'limit': 5, 'titleType': 'Movie'}

search = MovieSearch(api_key, string, mode, option)
data = search.get_keyword_results()
print("Keyword Results:")
print(data)
```

#### 3. Search Movies by Title

```python
# Perform title search
string = 'Forrest Gump'
mode = 'title'
option = {'startYear': 1991, 'endYear': 2023, 'page': 1, 'limit': 5, 'titleType': 'Movie'}

search = MovieSearch(api_key, string, mode, option)
data = search.get_title_results(exact=False, list='top_rated_english_250')
print("Title Results:")
print(data)
```

#### 4. Search Movies by IMDb ID

```python
# Perform ID search
string = ''
mode = 'id'
movie_id = 'tt0109830'
option = {'startYear': 1991, 'endYear': 2023, 'page': 1, 'limit': 5, 'titleType': 'Movie'}

search = MovieSearch(api_key, string, mode, option)
data = search.get_id_results(movie_id)
print("ID Results:")
print(data)
```

#### 5. Search Movies by Genre

```python
# Perform genre search
string = ''
mode = 'genre'
genre = 'Drama'
option = {'startYear': 1991, 'endYear': 2023, 'page': 1, 'limit': 5, 'titleType': 'Movie'}

search = MovieSearch(api_key, string, mode, option)
data = search.get_genre_results(genre)
print("Genre Results:")
print(data)
```

Remember to replace "your_rapidapi_key" with your actual RapidAPI key. Adjust the search parameters and explore various search modes to get detailed information about movies.
````



#### 3. Movie Detail

Retrieve detailed information about a specific movie, including ratings, aka (also known as) details, and movie posters.

````python
#### 1. Search Movies by Genre and Get Ratings

```python
from imdb_dataset.movie_search import MovieSearch
from imdb_dataset.movie_detail import MovieDetail

# Set up API key
api_key = "your_rapidapi_key"

# Search movies by genre
string = ''
mode = 'genre'
option = {'startYear': 1991, 'endYear': 2010, 'page': 1, 'limit': 5, 'titleType': 'Movie'}

search = MovieSearch(api_key, string, mode, option)
data = search.get_genre_results(genre='Drama')
data = data.dropna().reset_index(drop=True)

# Get detailed movie ratings
detail = MovieDetail(api_key, data)
ratings_data = detail.get_movie_ratings()
print("Movie Ratings:")
print(ratings_data)
```

#### 2. Get Also Known As (AKA) Information and Movie Poster

```python
# Get movie AKA information
movie_id = ratings_data['imdbId'][0]
aka_data = detail.get_movie_aka(movie_id)
print("Movie AKA Information:")
print(aka_data)

# Get and save movie poster
detail.get_movie_poster(movie_id, show=False, save=True)
```

Remember to replace "your_rapidapi_key" with your actual RapidAPI key. Customize the search parameters and explore different movie details, including ratings, AKAs, and posters.
````



This quick start guide covers the basic usage of the IMDb Dataset API. Refer to the API documentation for more details on available endpoints, parameters, and response formats.



### Legal Stuff

**IMDB_Dataset** is distributed under the **Apache Software License**. See the [LICENSE.txt](./LICENSE.txt) file in the release for details.

It's an open-source tool that uses Movies Database publicly available APIs, and is intended for research and educational purposes. 


### P.S.

Please drop me an note with any feedback you have.

