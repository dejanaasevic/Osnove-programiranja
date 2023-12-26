import re

from tabulate import tabulate


class MovieProjectionTerm:
    def __init__(self, movie_projection, index, date):
        self.index = index
        self.movie_projection = movie_projection
        self.date = date

        self.code = self.generate_projection_term_code()

    def generate_projection_term_code(self):
        formatted_date = self.date.strftime('%d.%m.%Y.')
        movie_projection_code = str(self.movie_projection.projection_code)
        random_code = self.generate_letters_code()
        return movie_projection_code + random_code + '|' + formatted_date

    def generate_letters_code(self):
        if self.index == 0:
            return 'AA'
        else:
            first_letter_index = self.index // 26
            first_letter = chr(65 + first_letter_index)
            second_letter_index = self.index % 26
            second_letter = chr(65 + second_letter_index)
            return f"{first_letter}{second_letter}"

    def display_movie_projection_term_staro(self):
        formatted_date = self.date.strftime('%d.%m.%Y.')
        movie_projection_term_info = (f"Title: {self.movie_projection.movie}\n"
                                      f"Hall:{self.movie_projection.hall.hall_code}\n"
                                      f"Date:{formatted_date}\nStart time:{self.movie_projection.start_time}\n"
                                      f"End time:{self.movie_projection.end_time}\n")

        print(movie_projection_term_info)

    def display_movie_projection_term(self):
        formatted_date = self.date.strftime('%d.%m.%Y.')
        movie_projection_term_data = [
            ["Title", self.movie_projection.movie],
            ["Hall", self.movie_projection.hall.hall_code],
            ["Date", formatted_date],
            ["Start Time", self.movie_projection.start_time],
            ["End Time", self.movie_projection.end_time]
        ]
        table = tabulate(movie_projection_term_data, headers=["Attribute", "Information"], tablefmt="grid")
        print(table)


    @staticmethod
    def valid_date_format(date_string):
        pattern = r"^\d{1,2}\.\d{1,2}\.\d{4}\."
        return bool(re.match(pattern, date_string))

    @staticmethod
    def valid_code(code):
        pattern = r"^\d{4}[A-Z]{2}\|\d{1,2}\.\d{1,2}\.\d{4}\.$"
        return bool(re.match(pattern, code))


