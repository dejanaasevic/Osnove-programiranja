from Movie import Movie
from MovieCriterion import MovieCriterion


def save_movie(movie):
    with open('movies.txt', 'a') as file:
        file.write(f"{movie.title},{movie.genre},{movie.duration},{movie.main_roles},{movie.country_of_origin},"
                   f"{movie.release_year},{movie.description}")


class MovieController:
    def __init__(self):
        self.list_of_movies = []

    def load_movies(self):
        with open('movies.txt', 'r') as file:
            for line in file:
                new_movie = line.strip().split(',')
                self.list_of_movies.append(Movie(*new_movie))

    def search(self, criterion):
        filtered_movies = []
        for movie in self.list_of_movies:
            if criterion.valid_movie(movie):
                filtered_movies.append(movie)
        if not filtered_movies:
            return None
        else:
            return filtered_movies
