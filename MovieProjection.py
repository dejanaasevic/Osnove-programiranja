import re

from tabulate import tabulate


class MovieProjection:
    def __init__(self, projection_code, hall, start_time, end_time, projection_days, movie, ticket_price):
        self.projection_code = projection_code
        self.hall = hall
        self.start_time = start_time
        self.end_time = end_time
        self.projection_days = projection_days
        self.movie = movie
        self.ticket_price = ticket_price

    def display_movie_projection_staro(self):
        print(f"Projection Code: {self.projection_code}\nHall: {self.hall.hall_code}\nStart Time: {self.start_time}\n"
              f"End Time: {self.end_time}\nProjection Days: {self.projection_days}\nMovie: {self.movie}\n"
              f"Ticket Price: {self.ticket_price}")

    def display_movie_projection(self):
        start_time_str = self.start_time.strftime("%H:%M")
        end_time_str = self.end_time.strftime("%H:%M")
        movie_projection_data = [
            ["Projection Code", self.projection_code],
            ["Hall", self.hall.hall_code],
            ["Start Time", start_time_str],
            ["End Time", end_time_str],
            ["Projection Days", self.projection_days],
            ["Movie", self.movie],
            ["Ticket Price", self.ticket_price]
        ]
        table = tabulate(movie_projection_data, headers=["Attribute", "Information"], tablefmt="grid")
        print(table)
    @staticmethod
    def valid_time_format(time_string):
        pattern = r"^(?:[01]\d|2[0-3]):[0-5]\d$"
        return bool(re.match(pattern, time_string))

    @staticmethod
    def valid_code(input_string):
        pattern = r"^\d{4}$"
        return bool(re.match(pattern, input_string))

    @staticmethod
    def valid_day_input(projection_days):
        pattern = r"^\b(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday)(?:,\s*\b(?:Monday|Tuesday|Wednesday|Thursday|Friday|Saturday|Sunday))*\b$"
        return bool(re.match(pattern, projection_days))

    @staticmethod
    def valid_price(price):
        pattern = r"^\d+\.\d{2}$"
        return bool(re.match(pattern, price))


