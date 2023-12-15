from imdb_dataset.api_initialize import ApiInitialize

api_key = "6fff73e170msh4b1276331400f97p1b4552jsn68d88f580ee6"


def test_api_initialize():
    genres, lists, titleTypes = ApiInitialize(api_key).get_utils()
    print(genres, lists, titleTypes)


test_api_initialize()
