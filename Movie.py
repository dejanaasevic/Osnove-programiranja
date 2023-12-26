import re
from tabulate import tabulate
import textwrap





class Movie:
    def __init__(self, title, genre, duration, director, main_roles, country_of_origin, release_year, description):
        self.title = title
        self.genre = genre
        self.duration = duration
        self.director = director
        self.main_roles = main_roles
        self.country_of_origin = country_of_origin
        self.release_year = release_year
        self.description = description

    def display_movie_staro(self):
        movie_info = (f"Title: {self.title}\nGenre:{self.genre}\nDuration:{self.duration}\nDirector:{self.director}\n"
                      f"Main roles:{self.main_roles}\nCountry of origin:{self.country_of_origin}\n"
                      f"Release year:{self.release_year}\nDescription:{self.description}\n")
        print(movie_info)

    def display_movie(self):
        movie_data = [
            ["Title", self.title],
            ["Genre", self.genre],
            ["Duration", self.duration],
            ["Director", self.director],
            ["Main roles", self.main_roles],
            ["Country of origin", self.country_of_origin],
            ["Release year", self.release_year],
            ["Description", "\n".join(textwrap.wrap(self.description, width=60))]
        ]
        table = tabulate(movie_data, headers=["Attribute", "Information"], tablefmt="grid")
        print(table)

    @staticmethod
    def valid_name(movie_name):
        return not movie_name.isspace()

    @staticmethod
    def valid_genre(genre_name):
        genres = [
            "action", "adventure", "animation", "comedy", "crime", "documentary",
            "drama", "fantasy", "horror", "mystery", "romance", "sci-fi",
            "thriller", "western", "war", "biography", "music", "sports",
            "superhero", "family", "teenage"
        ]

        genre_name_array = genre_name.lower().split()

        for genre_info in genre_name_array:
            if genre_info not in genres:
                return False

        return True

    @staticmethod
    def valid_duration(movie_duration):
        try:
            movie_duration = int(movie_duration)
            if movie_duration > 30:
                return True
            else:
                return False

        except ValueError:
            return False

    @staticmethod
    def valid_person_name(person_name):
        regex_name = r'^[A-Z][a-z]*(\s[A-Z][a-z]*)*$'
        if re.match(regex_name, person_name):
            return True
        else:
            return False

    @staticmethod
    def valid_main_roles(main_roles):
        pattern = r'^[A-Z][a-zA-Z]*(?:[\s,]+[A-Z][a-zA-Z]*)*$'
        return bool(re.match(pattern, main_roles))

    @staticmethod
    def valid_country_name(country_name):
        pattern = r'^[A-Z][a-zA-Z]{1,}$'
        if re.match(pattern, country_name) and len(country_name) >= 2:
            return True
        else:
            return False

    @staticmethod
    def valid_year(year):
        try:
            year = int(year)
            if 1800 <= year <= 2100:
                return True
            else:
                return False
        except ValueError:
            return False
