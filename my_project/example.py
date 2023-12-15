from imdb_dataset import api_initialize, movie_search, movie_detail


api_key = "6fff73e170msh4b1276331400f97p1b4552jsn68d88f580ee6"

# get utils
genres, lists, titleTypes = api_initialize.ApiInitialize(api_key).get_utils()
print(genres)
print(lists)
print(titleTypes)

# search movies
# genre
string = ''
mode = 'genre'
option = {'startYear': 1991, 'endYear': 2010, 'page': 1, 'limit': 10, 'titleType': 'Movie'}

search = movie_search.MovieSearch(api_key, string, mode, option)
data = search.get_genre_results(genre = 'Drama')
print(data)

# get data detail
detail = movie_detail.MovieDetail(api_key, data)
data1 = detail.get_movie_ratings()
print(data1)

# get_movie_poster
id = data1['imdbId'][0]
data2 = detail.get_movie_aka(id)
print(data2)
detail.get_movie_poster(id, show = True, save = True)
