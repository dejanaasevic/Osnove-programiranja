from datetime import datetime
from MovieProjection import MovieProjection
from MovieProjectionTerm import MovieProjectionTerm


def save_projection(movie_projection_term):
    with open('projectionterms.txt', 'a') as file:
        projection_term_info = f"{movie_projection_term.code}\n"
        file.write(projection_term_info)


def get_day_of_week(date_item):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    day_of_week = date_item.weekday()
    return days_of_week[day_of_week]


def valid_date(projection, date):
    day_of_week = get_day_of_week(date)
    projection_days = projection.projection_days.split(', ')
    for day in projection_days:
        if day == day_of_week:
            return True
    return False


def add_movie_projection_term(projection, index, date):
    if valid_date(projection, date):
        return MovieProjectionTerm(projection, index, date)
    else:
        print("Neodgovarajuci datum")
        return None


def load_projections():
    list_of_projections = []
    with open('projections.txt', 'r') as file:
        for line in file:
            new_projection = line.strip().split('|')
            list_of_projections.append(MovieProjection(*new_projection))

        return list_of_projections


class MovieProjectionTermController:

    def __init__(self):
        self.list_of_projection_terms = []
        self.list_of_projections = load_projections()

    def load_projection_terms(self):
        with open('projectionterms.txt', 'r') as file:
            for line in file:
                # 1111AA|17.12.2023.
                movie_projection_terms_items = line.strip().split('|')
                code = movie_projection_terms_items[0]
                date = movie_projection_terms_items[1]
                date_object = datetime.strptime(date, '%d.%m.%Y.')
                for i in range(len(self.list_of_projections)):
                    if self.list_of_projections[i].projection_code == code[0:4]:
                        if valid_date(self.list_of_projections[i], date_object):
                            self.list_of_projection_terms.append(MovieProjectionTerm(self.list_of_projections[i],
                                                                                     i, date_object))

    def search(self, criterion):
        filtered_movies_projection_terms = []
        for movie_projection_term in self.list_of_projection_terms:
            if criterion.valid_projection_term(movie_projection_term):
                filtered_movies_projection_terms.append(movie_projection_term)
        if not filtered_movies_projection_terms:
            return None
        else:
            return filtered_movies_projection_terms
