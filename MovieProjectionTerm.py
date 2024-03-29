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

