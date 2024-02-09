from Movie import Movie
from MovieProjection import MovieProjection
from MovieProjectionController import MovieProjectionController

movie_projection_controller = MovieProjectionController()
movie_projection_controller.load_projections()
list_of_projections = movie_projection_controller.list_of_projections


def save_movie(movie):
    with open('movies.txt', 'a', encoding="utf-8") as file:
        file.write(f"{movie.title}|{movie.genre}|{movie.duration}|{movie.director}|{movie.main_roles}|"
                   f"{movie.country_of_origin}|"f"{movie.release_year}|{movie.description}\n")


def update_movie_in_file(status, file_movie, updated_movie):
    with open('movies.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    with open('movies.txt', 'w', encoding='utf-8') as file:
        for line in lines:
            data = line.strip().split('|')
            if (data[0] == file_movie.title and data[1] == file_movie.genre and
                    data[2] == file_movie.duration and data[3] == file_movie.director
                    and data[4] == file_movie.main_roles and data[5] == file_movie.country_of_origin
                    and data[6] == file_movie.release_year and data[7] == file_movie.description):
                updated_line = "|".join([
                    updated_movie.title, updated_movie.genre, updated_movie.duration,
                    updated_movie.director, updated_movie.main_roles, updated_movie.country_of_origin,
                    updated_movie.release_year, updated_movie.description
                ]) + "\n"
                file.write(updated_line)
            else:
                file.write(line)

    if status:
        for projection in list_of_projections:
            if projection.movie.title == file_movie.title and projection.movie.duration == file_movie.duration:
                projection.movie.title = updated_movie.title
                projection.movie.duration = updated_movie.duration

        with open('projections.txt', 'r') as file:
            lines = file.readlines()
        with open('projections.txt', 'w') as file:
            for line in lines:
                data = line.strip().split('|')
                new_ending_time = MovieProjection.calculate_new_ending(data[2], updated_movie.duration)
                if data[5] == file_movie.title:
                    updated_line = "|".join([
                        data[0], data[1], data[2], new_ending_time, data[4], updated_movie.title, data[6]
                    ]) + "\n"
                    file.write(updated_line)
                else:
                    file.write(line)


def remove_movie_from_file(movie_choice):
    with open('movies.txt', 'r', encoding="utf-8") as file:
        lines = file.readlines()
    with open('movies.txt', 'w', encoding="utf-8") as file:
        for line in lines:
            movie_info = line.strip().split('|')
            if (movie_info[0] == movie_choice.title and movie_info[1] == movie_choice.genre and
                    movie_info[2] == movie_choice.duration and movie_info[3] == movie_choice.director and
                    movie_info[4] == movie_choice.main_roles and movie_info[5] == movie_choice.country_of_origin
                    and movie_info[6] and movie_choice.release_year and movie_info[7] == movie_choice.description):
                continue
            file.write(line)


class MovieController:
    def __init__(self):
        self.list_of_movies = []

    def load_movies(self):
        with open('movies.txt', 'r', encoding="utf-8") as file:
            for line in file:
                new_movie = line.strip().split('|')
                self.list_of_movies.append(Movie(*new_movie))

    def add_movie(self, movie):
        if isinstance(movie, Movie):
            self.list_of_movies.append(movie)
            save_movie(movie)
            return True
        else:
            if not isinstance(movie, Movie):
                print("Prosleđen objekat nije tipa Movie")
                return False

    def search(self, criterion):
        filtered_movies = []
        for movie in self.list_of_movies:
            if criterion.valid_movie(movie):
                filtered_movies.append(movie)
        if not filtered_movies:
            return None
        else:
            return filtered_movies

    def update_movie(self, file_movie, updated_movie):
        for movie in self.list_of_movies:
            status = movie.title != updated_movie.title or int(movie.duration) != int(updated_movie.duration)
            update_movie_in_file(status, file_movie, updated_movie)
        return True

    def remove_movie(self, movie_choice):
        for movie in self.list_of_movies:
            if (movie.title == movie_choice.title and movie.genre == movie_choice.genre and
                    movie.duration == movie_choice.duration and movie.director == movie_choice.director and
                    movie.main_roles == movie_choice.main_roles and movie.country_of_origin == movie_choice.country_of_origin
                    and movie.release_year and movie_choice.release_year and movie.description == movie_choice.description):
                remove_movie_from_file(movie)
                self.list_of_movies.remove(movie)
                return True
        return False
