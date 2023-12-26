import textwrap
from tabulate import tabulate
from CinemaHallController import CinemaHallController
from MovieController import MovieController


class DisplayController:

    def display_genres(self):
        genres_list = [
            "action", "adventure", "animation", "comedy", "crime", "documentary",
            "drama", "fantasy", "horror", "mystery", "romance", "sci-fi",
            "thriller", "western", "war", "biography", "music", "sports",
            "superhero", "family", "teenage"
        ]
        table = tabulate([[genre] for genre in genres_list], headers=["Genres"], tablefmt="fancy_grid")
        print(table)

    def display_filtered_projection_term(self, filtered_list):
        projection_term_data = []
        for term in filtered_list:
            formatted_date = term.date.strftime('%d.%m.%Y.')
            projection_term_data.append([
                term.movie_projection.movie, term.movie_projection.hall.hall_code, formatted_date,
                term.movie_projection.start_time, term.movie_projection.end_time
            ])
        headers = ["Title", "Hall", "Date", "Start time", "End time"]
        print(tabulate(projection_term_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    def display_filtered_movies(self, filtered_list):
        movie_data = []
        for movie in filtered_list:
            wrapped_roles = "\n".join(textwrap.wrap(movie.main_roles, width=25))
            movie_data.append([
                movie.title, movie.genre, str(movie.duration), movie.director,
                wrapped_roles, movie.country_of_origin, str(movie.release_year)
            ])

        headers = ["Title", "Genre", "Duration", "Director", "Main Roles", "Country of Origin", "Release Year"]
        print(tabulate(movie_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    def display_movies(self):
        movie_controller = MovieController()
        movie_controller.load_movies()
        list_of_movies = movie_controller.list_of_movies
        movie_data = []
        for movie in list_of_movies:
            wrapped_roles = "\n".join(textwrap.wrap(movie.main_roles, width=25))
            movie_data.append([
                movie.title, movie.genre, str(movie.duration), movie.director,
                wrapped_roles, movie.country_of_origin, str(movie.release_year)
            ])

        headers = ["Title", "Genre", "Duration", "Director", "Main Roles", "Country of Origin", "Release Year"]
        print(tabulate(movie_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    def display_movies_name(self):
        movie_controller = MovieController()
        movie_controller.load_movies()
        list_of_movies = movie_controller.list_of_movies
        movie_data = []
        for movie in list_of_movies:
            movie_data.append([
                movie.title
            ])
        headers = ["Title"]
        print(tabulate(movie_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    def display_cinemahall_code(self):
        cinemahall_controler = CinemaHallController()
        cinemahall_controler.load_cinema_halls()
        list_of_halls = cinemahall_controler.list_of_cinema_halls
        hall_data = []
        for hall in list_of_halls:
            hall_data.append([
                hall.hall_code
            ])
        headers = ["Hall Code"]
        print(tabulate(hall_data, headers=headers, tablefmt="fancy_grid", numalign="center"))
