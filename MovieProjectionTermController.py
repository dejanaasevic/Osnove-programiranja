from datetime import datetime
from MovieProjectionTerm import MovieProjectionTerm
from MovieProjectionController import MovieProjectionController
from CinemaHallController import CinemaHallController

projection_controller = MovieProjectionController()
projection_controller.load_projections()
list_of_projections = projection_controller.list_of_projections
cinema_controller = CinemaHallController()
cinema_controller.load_cinema_halls()
list_of_halls = cinema_controller.list_of_cinema_halls


def get_index_from_code(code):
    code = code.upper()
    index = 0
    for i, char in enumerate(code):
        index += (ord(char) - 65) * (26 ** (len(code) - i - 1))
    return index

def save_projection(movie_projection_term):
    with open('projectionterms.txt', 'a') as file:
        projection_term_info = f"{movie_projection_term.code}\n"
        file.write(projection_term_info)


def remove_projection_term_from_file(projection_term):
    with open('projectionterms.txt', 'r') as file:
        lines = file.readlines()
    with open('projectionterms.txt', 'w') as file:
        for line in lines:
            if line.strip().upper() != str(projection_term.code).strip().upper():
                file.write(line)
            else:
                print(f"obrisan termin projekcije: {str(projection_term.code).strip().upper()}")


class MovieProjectionTermController:

    def __init__(self):
        self.list_of_projection_terms = []

    def load_projection_terms(self):
        with open('projectionterms.txt', 'r') as file:
            for line in file:
                # 1111AA|17.12.2023.
                movie_projection_terms_items = line.strip().split('|')
                code = movie_projection_terms_items[0]
                date = movie_projection_terms_items[1]
                date_object = datetime.strptime(date, '%d.%m.%Y.')
                for i in range(len(list_of_projections)):
                    if list_of_projections[i].projection_code == code[0:4]:
                        index = get_index_from_code(code[4:])
                        self.list_of_projection_terms.append(MovieProjectionTerm(list_of_projections[i],
                                                                                 index, date_object))

    def search(self, criterion):
        filtered_movies_projection_terms = []
        for movie_projection_term in self.list_of_projection_terms:
            if criterion.valid_projection_term(movie_projection_term):
                filtered_movies_projection_terms.append(movie_projection_term)
        if not filtered_movies_projection_terms:
            return None
        else:
            return filtered_movies_projection_terms

    def unique_code(self, projection_term_code):
        for term in self.list_of_projection_terms:
            if projection_term_code == term.code:
                return False
        return True

    def add_projection_term(self, projection_term):
        if isinstance(projection_term, MovieProjectionTerm):
            if not self.unique_code(projection_term.code):
                print("Termin projekcije vec postoji. Molimo pokusajte ponovo.")
                return False
            if self.unique_code(projection_term.code):
                self.list_of_projection_terms.append(projection_term)
                save_projection(projection_term)
            return True
        else:
            if not isinstance(projection_term, MovieProjectionTerm):
                print("Prosleđen objekat nije tipa MovieProjectionTerm")
                return False

    def remove_projection_terms(self, delete_projection_term_list):
        if not delete_projection_term_list:
            return
        for projection_term in delete_projection_term_list:
            self.remove_projection_term(projection_term)

    def remove_projection_term(self, projection_term_choice):
        for projection_term in self.list_of_projection_terms:
            if projection_term.code == projection_term_choice.code:
                remove_projection_term_from_file(projection_term)
                self.list_of_projection_terms.remove(projection_term)
                return True
        return False

    @staticmethod
    def get_day_of_week(date_item):
        days_of_week = ["ponedeljak", "utorak", "sreda", "četvrtak", "petak", "subota", "nedelja"]
        day_of_week = date_item.weekday()
        return days_of_week[day_of_week]

    @staticmethod
    def valid_date(projection, date_object):
        day_of_week = MovieProjectionTermController.get_day_of_week(date_object)
        projection_days = projection.projection_days.split(',')
        for day in projection_days:
            if day == day_of_week:
                return True
        return False

    def generate_index(self, projection):
        index = None
        for projection_term in self.list_of_projection_terms:
            if projection_term.movie_projection.projection_code == projection.projection_code:
                index = projection_term.index
                break
        if index is not None:
            return index
        else:
            max_index = self.list_of_projection_terms[0].index
            for projection_term in self.list_of_projection_terms:
                if projection_term.index > max_index:
                    max_index = projection_term.index

            return max_index + 1


