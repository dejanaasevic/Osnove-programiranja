import re


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

    def display_movie(self):
        movie_info = (f"Title: {self.title}\nGenre:{self.genre}\nDuration:{self.duration}\nDirector:{self.director}\n"
                      f"Main roles:{self.main_roles}\nCountry of origin:{self.country_of_origin}\n"
                      f"Release year:{self.release_year}\nDescription:{self.description}\n")
        print(movie_info)

    @staticmethod
    def valid_name(movie_name):
        return not movie_name.isspace()

    @staticmethod
    def valid_genre(genre_name):
        if genre_name.isspace():
            return False
        else:
            genres = [
                "action", "adventure", "animation", "comedy", "crime", "documentary",
                "drama", "fantasy", "horror", "mystery", "romance", "sci-fi",
                "thriller", "western", "war", "biography", "music", "sports",
                "superhero", "family", "teenage"
            ]
            for genre in genres:
                if genre_name.lower() == genre:
                    return True

        return False
    @staticmethod
    def valid_duration(movie_duration):
        try:
            movie_duration = int(movie_duration)
            if movie_duration > 30:
                return  True
            else:
                return  False

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
    def valid_country_name(country_name):
        return not country_name.isspace()

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
