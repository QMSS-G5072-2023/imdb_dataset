from imdb_dataset.movie_search import MovieSearch

api_key = "6fff73e170msh4b1276331400f97p1b4552jsn68d88f580ee6"


def test_movie_search():
    # akas
    string = '阿甘正传'
    mode = 'akas'
    option = {'startYear': 1991, 'endYear': 2023, 'page': 1, 'limit': 5, 'titleType': 'Movie'}

    search = MovieSearch(api_key, string, mode, option)
    data = search.get_akas_results()
    print(data)

    # keyword
    string = 'forrest'
    mode = 'keyword'
    option = {'startYear': 1991, 'endYear': 2023, 'page': 1, 'limit': 5, 'titleType': 'Movie'}

    search = MovieSearch(api_key, string, mode, option)
    data = search.get_keyword_results()
    print(data)

    # title
    string = 'Forrest Gump'
    mode = 'title'
    option = {'startYear': 1991, 'endYear': 2023, 'page': 1, 'limit': 5, 'titleType': 'Movie'}

    search = MovieSearch(api_key, string, mode, option)
    data = search.get_title_results(exact = False, list = 'top_rated_english_250')
    print(data)

    # id
    string = ''
    mode = 'id'
    id = 'tt0109830'
    option = {'startYear': 1991, 'endYear': 2023, 'page': 1, 'limit': 5, 'titleType': 'Movie'}
    search = MovieSearch(api_key, string, mode, option)
    data = search.get_id_results(id)
    print(data)

    # genre
    string = ''
    mode = 'genre'
    genre = 'Drama'
    option = {'startYear': 1991, 'endYear': 2023, 'page': 1, 'limit': 5, 'titleType': 'Movie'}

    search = MovieSearch(api_key, string, mode, option)
    data = search.get_genre_results(genre)
    print(data)
