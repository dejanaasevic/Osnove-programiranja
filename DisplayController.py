import textwrap
from tabulate import tabulate
from CinemaHallController import CinemaHallController
from MovieController import MovieController
from MovieProjectionController import MovieProjectionController
from MovieProjectionTermController import MovieProjectionTermController
from TicketController import TicketController


class DisplayController:
    @staticmethod
    def display_genres():
        genres_list = [
             "akcija", "avantura", "animirani", "komedija", "krimi", "dokumentarni", "drama", "fantastika", "horor",
             "misterija", "romantika", "fantastika", "triler", "vestern", "ratni", "biografski", "muzički",
             "sportski", "superheroj", "porodični", "teenage"
        ]
        table = tabulate([[genre] for genre in genres_list], headers=["žanr"], tablefmt="fancy_grid", numalign="center")
        print(table)


    @staticmethod
    def display_filtered_projection_term(filtered_list):
        projection_term_data = []
        i = 0
        for term in filtered_list:
            i += 1
            formatted_date = term.date.strftime('%d.%m.%Y.')
            projection_term_data.append([
                i, term.movie_projection.movie, term.movie_projection.hall.hall_code, formatted_date,
                term.movie_projection.start_time, term.movie_projection.end_time
            ])
        headers = ["ID", "naziv", "sala", "datim", "vreme početka", "vreme kraja"]
        print(tabulate(projection_term_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    @staticmethod
    def display_filtered_movies(filtered_list):
        movie_data = []
        for movie in filtered_list:
            wrapped_roles = "\n".join(textwrap.wrap(movie.main_roles, width=25))
            movie_data.append([
                movie.title, movie.genre, str(movie.duration), movie.director,
                wrapped_roles, movie.country_of_origin, str(movie.release_year)
            ])

        headers = ["naslov", "žanr", "trajanje", "režiser", "glavne uloge", "zemlja porekla", "godina"]
        print(tabulate(movie_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    @staticmethod
    def display_movies():
        movie_controller = MovieController()
        movie_controller.load_movies()
        list_of_movies = movie_controller.list_of_movies
        movie_data = []
        i = 0
        for movie in list_of_movies:
            i += 1
            wrapped_roles = "\n".join(textwrap.wrap(movie.main_roles, width=25))
            movie_data.append([
                i, movie.title, movie.genre, str(movie.duration), movie.director,
                wrapped_roles, movie.country_of_origin, str(movie.release_year)
            ])

        headers = ["ID", "naslov", "žanr", "trajanje", "režiser", "glavne uloge", "zemlja porekla", "godina"]
        print(tabulate(movie_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    @staticmethod
    def display_movies_name():
        movie_controller = MovieController()
        movie_controller.load_movies()
        list_of_movies = movie_controller.list_of_movies
        movie_data = []
        i = 0
        for movie in list_of_movies:
            i += 1
            movie_data.append([
                i, movie.title
            ])
        headers = ["ID", "naziv"]
        print(tabulate(movie_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    @staticmethod
    def display_cinemahall_code():
        cinemahall_controler = CinemaHallController()
        cinemahall_controler.load_cinema_halls()
        list_of_halls = cinemahall_controler.list_of_cinema_halls
        hall_data = []
        i = 0
        for hall in list_of_halls:
            i += 1
            hall_data.append([
                i, hall.hall_code
            ])
        headers = ["ID", "kod sale"]
        print(tabulate(hall_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    @staticmethod
    def display_reserved_tickets():
        ticket_controller = TicketController()
        ticket_controller.load_tickets()
        list_of_tickets = ticket_controller.list_of_tickets
        ticket_data = []
        i = 1
        for ticket in list_of_tickets:
            if ticket.status == "1":
                ticket_data.append([
                    i, ticket.projection_term.code, ticket.owner, ticket.projection_term.movie_projection.movie,
                    ticket.projection_term.date, ticket.projection_term.movie_projection.start_time,
                    ticket.projection_term.movie_projection.end_time, ticket.seat_label,
                    'rezervisana karta' if ticket.status == '1' else 'prodata karta'
                ])
            i += 1

        headers = ["ID", "oznaka termina", "vlasnik", "film", "datum", "početak", "kraj", "oznaka sedišta", "status"]
        print(tabulate(ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    @staticmethod
    def display_projection_codes():
        projection_controller = MovieProjectionController()
        projection_controller.load_projections()
        list_of_projections = projection_controller.list_of_projections
        projection_code_data = []
        i = 0
        for projection in list_of_projections:
            i += 1
            projection_code_data.append([
                i, int(projection.projection_code)
            ])

        table = tabulate(projection_code_data, headers=["ID", "kod projekcije"], tablefmt="fancy_grid",
                         numalign="center")
        print(table)

    @staticmethod
    def display_filtered_ticket(filtered_list):
        ticket_data = []
        i = 1
        for ticket in filtered_list:
            string_date = ticket.projection_term.date.strftime("%d.%m.%Y.")
            ticket_data.append([
                i, ticket.projection_term.code, ticket.owner, ticket.projection_term.movie_projection.movie,
                string_date, ticket.projection_term.movie_projection.start_time,
                ticket.projection_term.movie_projection.end_time, ticket.seat_label,
                'rezervisana karta' if ticket.status == '1' else 'prodata karta'
            ])
            i += 1
        headers = [
            "ID", "kod termina", "vlasnik", "film", "datum", "vreme početka",
            "vreme završetka", "oznaka sedišta", "status"
        ]
        print(tabulate(ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    @staticmethod
    def display_projection_term_codes():
        projection_term_controller = MovieProjectionTermController()
        projection_term_controller.load_projection_terms()
        list_of_projection_terms = projection_term_controller.list_of_projection_terms
        projection_term_code_data = []
        i = 1
        for term in list_of_projection_terms:
            projection_term_code_data.append([
                i, term.code
            ])
            i += 1
        headers = ["ID", "kod termina"]
        print(tabulate(projection_term_code_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    @staticmethod
    def display_projection_term():
        projection_term_controller = MovieProjectionTermController()
        projection_term_controller.load_projection_terms()
        list_of_projection_terms = projection_term_controller.list_of_projection_terms
        projection_term_data = []
        i = 1
        for term in list_of_projection_terms:
            formatted_date = term.date.strftime('%d.%m.%Y.')
            projection_term_data.append([
                i, term.code, term.movie_projection.movie, term.movie_projection.hall.hall_code, formatted_date,
                term.movie_projection.start_time, term.movie_projection.end_time
            ])
            i += 1
        headers = ["ID", "kod termina projekcije", "naslov", "sala", "datum", "vreme početka", "vreme završetka"]
        print(tabulate(projection_term_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    @staticmethod
    def display_projection():
        projection_controller = MovieProjectionController()
        projection_controller.load_projections()
        list_of_projection = projection_controller.list_of_projections
        projection_data = []
        i = 1
        for projection in list_of_projection:
            projection_data.append([
                i, projection.projection_code, projection.hall.hall_code, projection.start_time, projection.end_time,
                projection.projection_days, projection.movie, projection.ticket_price])
            i += 1
        headers = ["ID", "kod termina projekcije", "sala", "vreme početka", "vreme završetka", "dani projekcije",
                   "naslov", "cena karte"
                   ]
        print(tabulate(projection_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    @staticmethod
    def display_sold_tickets_by_sale_date(filtered_tickets):
        ticket_data = []
        i = 1
        for ticket in filtered_tickets:
            string_projection_date = ticket.projection_term.date.strftime("%d.%m.%Y.")
            string_ticket_date = ticket.date.strftime("%d.%m.%Y.")

            ticket_data.append([
                i, ticket.projection_term.code, ticket.owner, ticket.projection_term.movie_projection.movie,
                string_projection_date, ticket.projection_term.movie_projection.start_time,
                ticket.projection_term.movie_projection.end_time, ticket.seat_label,
                'rezervisana karta' if ticket.status == '1' else 'prodata karta', string_ticket_date
            ])
            i += 1

        headers = [
            "ID", "kod termina", "vlasnik", "film", "datum termina projekcije", "vreme početka",
            "vreme završetka", "oznaka sedišta", "status", "datum karte"
        ]
        table = tabulate(ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        return table

    @staticmethod
    def display_sold_tickets_by_projection_term_date(filtered_tickets):
        ticket_data = []
        i = 1
        for ticket in filtered_tickets:
            string_projection_date = ticket.projection_term.date.strftime("%d.%m.%Y.")
            string_ticket_date = ticket.date.strftime("%d.%m.%Y.")
            ticket_data.append([
                i, ticket.projection_term.code, ticket.owner, ticket.projection_term.movie_projection.movie,
                string_projection_date, ticket.projection_term.movie_projection.start_time,
                ticket.projection_term.movie_projection.end_time, ticket.seat_label,
                'rezervisana karta' if ticket.status == '1' else 'prodata karta', string_ticket_date
            ])
            i += 1
        headers = [
            "ID", "kod termina", "vlasnik", "film", "datum termina projekcije", "vreme početka",
            "vreme završetka", "oznaka sedišta", "status", "datum karte"
        ]
        table = tabulate(ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        return table

        pass

    @staticmethod
    def display_sold_tickets_by_date_and_sellperson(filtered_tickets):
        sold_ticket_data = []
        for sold_ticket in filtered_tickets:
            string_projection_date = sold_ticket.ticket.projection_term.date.strftime("%d.%m.%Y.")
            string_ticket_date = sold_ticket.ticket.date.strftime("%d.%m.%Y.")
            sold_ticket_data.append([
                sold_ticket.sellperson, sold_ticket.ticket.projection_term.code, sold_ticket.ticket.owner,
                sold_ticket.ticket.projection_term.movie_projection.movie,
                string_projection_date, sold_ticket.ticket.projection_term.movie_projection.start_time,
                sold_ticket.ticket.projection_term.movie_projection.end_time, sold_ticket.ticket.seat_label,
                string_ticket_date,
                sold_ticket.price
            ])
        headers = [
            "prodavac", "kôd termina", "vlasnik", "film", "datum projekcije", "vreme početka",
            "vreme završetka", "oznaka sedišta", "datum karte", "cena"

        ]
        table = tabulate(sold_ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        return table

    @staticmethod
    def display_total_number_and_price_by_sale_day(filtered_tickets):
        total_quantity = len(filtered_tickets)
        total_price = sum(float(sold_ticket.price) for sold_ticket in filtered_tickets)

        ticket_data = [
            ["ukupan broj", total_quantity],
            ["ukupna cena", total_price]
        ]

        table = tabulate(ticket_data, headers=["", ""], tablefmt="fancy_grid", numalign="center")
        return table

    @staticmethod
    def display_total_number_and_price_by_projection_term_day(filtered_tickets):
        total_quantity = len(filtered_tickets)
        total_price = sum(float(sold_ticket.price) for sold_ticket in filtered_tickets)

        ticket_data = [
            ["ukupan broj", total_quantity],
            ["ukupna cena", total_price]
        ]

        table = tabulate(ticket_data, headers=["", ""], tablefmt="fancy_grid", numalign="center")
        return table

    @staticmethod
    def display_total_price_for_sold_tickets_by_movie(movie_title, filtered_tickets):
        total_price = 0.0
        sold_ticket_data = []
        for sold_ticket in filtered_tickets:
            total_price += float(sold_ticket.price)

        sold_ticket_data.append([movie_title, total_price])
        headers = ["naziv filma", "ukupna cena"]
        table = tabulate(sold_ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        return table

    @staticmethod
    def sold_tickets_by_sale_day_and_sellperson(day, sellperson, filtered_tickets):
        total_price = 0.0
        sold_ticket_data = []
        for sold_ticket in filtered_tickets:
            total_price += float(sold_ticket.price)
        total_count = len(filtered_tickets)
        sold_ticket_data.append([sellperson, day, str(total_count), str(total_price)])
        headers = ["prodavac", "dan", "ukupan broj", "ukupna cena"]
        table = tabulate(sold_ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        return table

    @staticmethod
    def sold_tickets_for_each_sellperson_in_last_30_days(sold_tickets_data):
        headers = ["ID", "prodavac", "ukupna cena", "ukupan broj"]
        table = tabulate(sold_tickets_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        return table

    @staticmethod
    def display_reserved_tickets_for_user(user_reserved_ticket):
        reserved_ticket_data = []
        i = 0
        for ticket in user_reserved_ticket:
            i += 1
            reserved_ticket_data.append([i, ticket.projection_term.code, ticket.projection_term.movie_projection.movie,
                                         ticket.projection_term.date.strftime('%d.%m.%Y.'),
                                         ticket.projection_term.movie_projection.start_time,
                                         ticket.projection_term.movie_projection.end_time,
                                         ticket.seat_label])
        headers = ["ID", "kod termina projekcije", "film", "datum", "vreme početka", "vreme završetka",
                   "oznaka sedišta"]
        table = tabulate(reserved_ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        print(table)

    @staticmethod
    def display_all_tickets():
        ticket_controller = TicketController()
        ticket_controller.load_tickets()
        list_of_tickets = ticket_controller.list_of_tickets
        ticket_data = []
        i = 1
        for ticket in list_of_tickets:
            ticket_data.append([
                i, ticket.projection_term.code, ticket.owner, ticket.projection_term.movie_projection.movie,
                ticket.projection_term.date, ticket.projection_term.movie_projection.start_time,
                ticket.projection_term.movie_projection.end_time, ticket.seat_label,
                'rezervisana karta' if ticket.status == '1' else 'prodata karta'
            ])
            i += 1

        headers = [
            "ID", "kod termina", "vlasnik", "film", "datum",
            "vreme početka", "vreme završetka", "oznaka sedišta", "status"
        ]

        print(tabulate(ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    @staticmethod
    def display_total_number_and_price_by_sale_day_in_previous_week(filtered_tickets):
        total_quantity = len(filtered_tickets)
        total_price = 0.0
        for sold_ticket in filtered_tickets:
            total_price += float(sold_ticket.price)
        ticket_data = [total_quantity, total_price]
        headers = ["ukupan broj", "ukupna cena"]
        table = tabulate(ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        return table

    @staticmethod
    def display_total_number_and_price_by_projection_term_day_in_previous_week(filtered_tickets):
        total_quantity = len(filtered_tickets)
        total_price = 0.0
        for sold_ticket in filtered_tickets:
            total_price += float(sold_ticket.price)
        ticket_data = [total_quantity, total_price]
        headers = ["ukupan broj", "ukupna cena"]
        table = tabulate(ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        return table

    @staticmethod
    def display_projections():
        movie_projection_controller = MovieProjectionController()
        movie_projection_controller.load_projections()
        projection_data = []
        i = 0
        for projection in movie_projection_controller.list_of_projections:
            i += 1
            projection_data.append([i, projection.projection_code, projection.hall.hall_code, projection.start_time,
                                    projection.end_time, projection.projection_days, projection.movie,
                                    projection.ticket_price])
        headers = ["ID", "kod projekcije", "kod sale", "vreme početka",
                   "vreme kraja", "dani projekcije", "film", "cena karte"]
        table = tabulate(projection_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        print(table)

    @staticmethod
    def display_cinema_hall(hall):
        hall_data = [hall.hall_code, hall.hall_name if hall.hall_name else "",
                     hall.num_rows, ", ".join(hall.seat_labels)]
        headers = ["kod sale", "ime sale", "broj redova", "oznake sedišta"]
        table = tabulate(hall_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        print(table)

    @staticmethod
    def display_movie(self):
        movie_data = [self.title, self.genre, self.duration, self.director, self.main_roles, self.country_of_origin,
                      self.release_year]
        headers = ["naziv", "žanr", "trajanje", "režiser", "glavne uloge", "država" "godina"]
        table = tabulate(movie_data, headers=headers, tablefmt="grid")
        print(table)
        print()
        print("\n".join(textwrap.wrap(self.description, width=60)))
