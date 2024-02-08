import re


class ValidationController:
    @staticmethod
    def user_valid_username(username):
        regex_username = r"^[a-z0-9_.]+$"
        if re.match(regex_username, username):
            return True
        else:
            return False

    @staticmethod
    def user_valid_password(password):
        return len(password) > 6 and any(char.isdigit() for char in password)

    @staticmethod
    def user_valid_name(name):
        regex_name = r"^[A-Z][a-z]{2,29}$"
        if re.match(regex_name, name):
            return True
        else:
            return False

    @staticmethod
    def user_valid_surname(surname):
        regex_surname = r"^[A-Z][a-z]{2,29}$"
        if re.match(regex_surname, surname):
            return True
        else:
            return False

    @staticmethod
    def movie_valid_name(movie_name):
        return not movie_name.isspace()

    @staticmethod
    def movie_valid_genre(genre_name):
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
    def movie_valid_duration(movie_duration):
        try:
            movie_duration = int(movie_duration)
            if movie_duration > 30:
                return True
            else:
                return False

        except ValueError:
            return False

    @staticmethod
    def movie_valid_main_roles(main_roles):
        pattern = r'^[A-Z][a-zA-Z]*(?:[\s,]+[A-Z][a-zA-Z]*)*$'
        return bool(re.match(pattern, main_roles))

    @staticmethod
    def movie_valid_director(main_roles):
        pattern = r'^[A-Z][a-zA-Z]*(?:[\s,]+[A-Z][a-zA-Z]*)*$'
        return bool(re.match(pattern, main_roles))

    @staticmethod
    def movie_valid_country_name(country_name):
        pattern = r'^[A-Z][a-zA-Z]{1,}$'
        if re.match(pattern, country_name) and len(country_name) >= 2:
            return True
        else:
            return False

    @staticmethod
    def movie_valid_year(year):
        try:
            year = int(year)
            if 1800 <= year <= 2100:
                return True
            else:
                return False
        except ValueError:
            return False

    @staticmethod
    def cinema_hall_valid_hall_code(hall_code):
        return len(hall_code) == 1 and hall_code.isalpha() and hall_code.isupper()

    @staticmethod
    def projection_term_valid_date_format(date_string):
        pattern = r"^\d{1,2}\.\d{1,2}\.\d{4}\."
        return bool(re.match(pattern, date_string))

    @staticmethod
    def projection_term_valid_code(code):
        pattern = r"^\d{4}[A-Z]{2}\|\d{1,2}\.\d{1,2}\.\d{4}\.$"
        return bool(re.match(pattern, code))

    @staticmethod
    def projection_valid_time_format(time_string):
        pattern = r"^(?:[01]\d|2[0-3]):[0-5]\d$"
        return bool(re.match(pattern, time_string))

    @staticmethod
    def cinema_hall_valid_seat_label(seat_label):
        pattern = r'^\d+[A-Z]$'
        return bool(re.match(pattern, seat_label))

    @staticmethod
    def ticket_valid_name(name):
        pattern = r'^[A-Z][a-zA-Z]*(?:[\s,]+[A-Z][a-zA-Z]*)*$'
        return bool(re.match(pattern, name))

    @staticmethod
    def movie_projection_valid_code(input_string):
        pattern = r"^\d{4}$"
        return bool(re.match(pattern, input_string))

    @staticmethod
    def movie_projection_valid_day_input(projection_days):
        pattern = r"^\b(?:Ponedeljak|Utorak|Sreda|Četvrtak|Petak|Subota|Nedelja)(?:,\s*\b(?:Ponedeljak|Utorak|Sreda|Četvrtak|Petak|Subota|Nedelja))*\b$"
        return bool(re.match(pattern, projection_days))

    @staticmethod
    def movie_projection_valid_price(price):
        pattern = r"^\d+\.\d{2}$"
        return bool(re.match(pattern, price))

    @staticmethod
    def cinema_hall_valid_name(cinema_hall_name):
        pattern = r"^[A-Z][a-zA-Z0-9\s]*$"
        return bool(re.match(pattern, cinema_hall_name))

    @staticmethod
    def cinema_hall_valid_num_rows(num_rows):
        pattern = r"^[1-9]\d*$"
        return bool(re.match(pattern, num_rows))

    @staticmethod
    def cinema_hall_valid_seat_labels(seat_labels):
        pattern = r"^[A-Z](,[A-Z])*$"
        return bool(re.match(pattern, seat_labels))