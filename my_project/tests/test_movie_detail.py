from imdb_dataset.movie_search import MovieSearch
from imdb_dataset.movie_detail import MovieDetail

api_key = "6fff73e170msh4b1276331400f97p1b4552jsn68d88f580ee6"


def test_movie_detail():
    # genre
    string = ''
    mode = 'genre'
    option = {'startYear': 1991, 'endYear': 2010, 'page': 1, 'limit': 5, 'titleType': 'Movie'}

    search = MovieSearch(api_key, string, mode, option)
    data = search.get_genre_results(genre = 'Drama')
    data = data.dropna().reset_index(drop = True)

    # get data detail
    detail = MovieDetail(api_key, data)
    data1 = detail.get_movie_ratings()
    print(data1)

    # get_movie_poster
    id = data1['imdbId'][0]
    data2 = detail.get_movie_aka(id)
    print(data2)
    detail.get_movie_poster(id, show = False, save = True)


test_movie_detail()
