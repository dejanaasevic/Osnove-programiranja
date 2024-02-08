from DisplayController import DisplayController

display_controller = DisplayController()


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
        display_controller.display_movie(self)
