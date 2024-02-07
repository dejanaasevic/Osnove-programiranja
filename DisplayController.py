import textwrap
from tabulate import tabulate
from CinemaHallController import CinemaHallController
from MovieController import MovieController
from MovieProjectionController import MovieProjectionController
from MovieProjectionTermController import MovieProjectionTermController
from TicketController import TicketController


class DisplayController:

    def display_genres(self):
        genres_list = [
            "action", "adventure", "animation", "comedy", "crime", "documentary",
            "drama", "fantasy", "horror", "mystery", "romance", "sci-fi",
            "thriller", "western", "war", "biography", "music", "sports",
            "superhero", "family", "teenage"
        ]
        table = tabulate([[genre] for genre in genres_list], headers=["Genres"], tablefmt="fancy_grid")
        print(table)

    def display_user(self, user):
        user_data = [user.username, user.password, user.name, user.surname, user.role]
        headers = ["Korisničko ime", "Lozinka", "Ime", "Prezime", "Uloga"]
        table = tabulate(user_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        print(table)

    def display_filtered_projection_term(self, filtered_list):
        projection_term_data = []
        i = 0
        for term in filtered_list:
            i += 1
            formatted_date = term.date.strftime('%d.%m.%Y.')
            projection_term_data.append([
                i, term.movie_projection.movie, term.movie_projection.hall.hall_code, formatted_date,
                term.movie_projection.start_time, term.movie_projection.end_time
            ])
        headers = ["ID", "Title", "Hall", "Date", "Start time", "End time"]
        print(tabulate(projection_term_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    def display_filtered_movies(self, filtered_list):
        movie_data = []
        for movie in filtered_list:
            wrapped_roles = "\n".join(textwrap.wrap(movie.main_roles, width=25))
            movie_data.append([
                movie.title, movie.genre, str(movie.duration), movie.director,
                wrapped_roles, movie.country_of_origin, str(movie.release_year)
            ])

        headers = ["Title", "Genre", "Duration", "Director", "Main Roles", "Country of Origin", "Release Year"]
        print(tabulate(movie_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    def display_movies(self):
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

        headers = ["ID", "Title", "Genre", "Duration", "Director", "Main Roles", "Country of Origin", "Release Year"]
        print(tabulate(movie_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    def display_movies_name(self):
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
        headers = ["ID", "Title"]
        print(tabulate(movie_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    def display_cinemahall_code(self):
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
        headers = ["ID", "Hall Code"]
        print(tabulate(hall_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    def display_reserved_tickets(self):
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

        headers = [
            "ID", "Code term", "Owner", "Movie", "Date", "Start time",
            "End time", "Seat label", "Status"
        ]

        print(tabulate(ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    def display_projection_codes(self):
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

        #number_table = [[int(num)] for num in projection_code_data]
        table = tabulate(projection_code_data, headers=["ID", "Code"], tablefmt="fancy_grid", numalign="center")
        print(table)

    def display_filtered_ticket(self, filtered_list):
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
            "ID", "Code term", "Owner", "Movie", "Date", "Start time",
            "End time", "Seat label", "Status"
        ]
        print(tabulate(ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    def display_projection_term_codes(self):
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
        headers = ["ID", "Code term"]
        print(tabulate(projection_term_code_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    def display_projection_term(self):
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
        headers = ["ID", "Projection term code", "Title", "Hall", "Date", "Start time", "End time"]
        print(tabulate(projection_term_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    def display_projection(self):
        projection_controller = MovieProjectionController()
        projection_controller.load_projections()
        list_of_projection = projection_controller.list_of_projections
        projection_data = []
        i = 1
        for projection in list_of_projection:
            projection_data.append([
                i, projection.projection_code, projection.hall, projection.start_time, projection.end_time,
                projection.projection_days, projection.movie, projection.ticket_price])
            i += 1
        headers = ["ID", "Projection term code", "Hall", "Start time", "End time", "Projection days", "Title",
                   "Ticket Price"]
        print(tabulate(projection_data, headers=headers, tablefmt="fancy_grid", numalign="center"))

    def display_sold_tickets_by_sale_date(self, filtered_tickets):
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
            "ID", "Code term", "Owner", "Movie", "Projection term date", "Start time",
            "End time", "Seat label", "Status", "Ticket date"
        ]
        table = tabulate(ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        return table

    def display_sold_tickets_by_projection_term_date(self, filtered_tickets):
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
            "ID", "Code term", "Owner", "Movie", "Projection term date", "Start time",
            "End time", "Seat label", "Status", "Ticket date"
        ]
        table = tabulate(ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        return table

        pass

    def display_sold_tickets_by_date_and_sellperson(self, filtered_tickets):
        sold_ticket_data = []
        i = 1
        for sold_ticket in filtered_tickets:
            string_projection_date = sold_ticket.ticket.projection_term.date.strftime("%d.%m.%Y.")
            string_ticket_date = sold_ticket.ticket.date.strftime("%d.%m.%Y.")
            sold_ticket_data.append([
                i, sold_ticket.sellperson, sold_ticket.ticket.projection_term.code, sold_ticket.ticket.owner,
                sold_ticket.ticket.projection_term.movie_projection.movie,
                string_projection_date, sold_ticket.ticket.projection_term.movie_projection.start_time,
                sold_ticket.ticket.projection_term.movie_projection.end_time, sold_ticket.ticket.seat_label,
                'rezervisana karta' if sold_ticket.ticket.status == '1' else 'prodata karta', string_ticket_date,
                sold_ticket.price
            ])
        headers = [
            "ID", "Sellperson", "Code term", "Owner", "Movie", "Projection term date", "Start time",
            "End time", "Seat label", "Status", "Ticket date", "Price"
        ]
        table = tabulate(sold_ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        return table

    def display_sold_tickets_by_sale_day(self, filtered_tickets):
        sold_ticket_data = []
        i = 1
        for sold_ticket in filtered_tickets:
            string_projection_date = sold_ticket.ticket.projection_term.date.strftime("%d.%m.%Y.")
            string_ticket_date = sold_ticket.ticket.date.strftime("%d.%m.%Y.")
            sold_ticket_data.append([
                i, sold_ticket.ticket.projection_term.code, sold_ticket.ticket.owner,
                sold_ticket.ticket.projection_term.movie_projection.movie,
                string_projection_date, sold_ticket.ticket.projection_term.movie_projection.start_time,
                sold_ticket.ticket.projection_term.movie_projection.end_time, sold_ticket.ticket.seat_label,
                'rezervisana karta' if sold_ticket.ticket.status == '1' else 'prodata karta', string_ticket_date,
                sold_ticket.price
            ])
        headers = [
            "ID", "Code term", "Owner", "Movie", "Projection term date", "Start time",
            "End time", "Seat label", "Status", "Ticket date", "Price"
        ]
        table = tabulate(sold_ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        return table

    def display_sold_tickets_by_projection_term_day(self, filtered_tickets):
        sold_ticket_data = []
        i = 1
        for sold_ticket in filtered_tickets:
            string_projection_date = sold_ticket.ticket.projection_term.date.strftime("%d.%m.%Y.")
            string_ticket_date = sold_ticket.ticket.date.strftime("%d.%m.%Y.")
            sold_ticket_data.append([
                i, sold_ticket.ticket.projection_term.code, sold_ticket.ticket.owner,
                sold_ticket.ticket.projection_term.movie_projection.movie,
                string_projection_date, sold_ticket.ticket.projection_term.movie_projection.start_time,
                sold_ticket.ticket.projection_term.movie_projection.end_time, sold_ticket.ticket.seat_label,
                'rezervisana karta' if sold_ticket.ticket.status == '1' else 'prodata karta', string_ticket_date,
                sold_ticket.price
            ])
        headers = [
            "ID", "Code term", "Owner", "Movie", "Projection term date", "Start time",
            "End time", "Seat label", "Status", "Ticket date", "Price"
        ]
        table = tabulate(sold_ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        return table

    def display_total_price_for_sold_tickets_by_movie(self, movie_title, filtered_tickets):
        total_price = 0.0
        sold_ticket_data = []
        for sold_ticket in filtered_tickets:
            total_price += float(sold_ticket.price)

        sold_ticket_data.append([movie_title, total_price])
        headers = ["Movie title", "Total price"]
        table = tabulate(sold_ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        return table

    def sold_tickets_by_sale_day_and_sellperson(self, day, date, sellperson, filtered_tickets):
        total_price = 0.0
        sold_ticket_data = []
        for sold_ticket in filtered_tickets:
            total_price += float(sold_ticket.price)
        total_count = len(filtered_tickets)
        sold_ticket_data.append([sellperson, date, day, total_count, total_price])
        headers = ["Sellperson", "Date", "Day", "Total count", "Total price"]
        table = tabulate(sold_ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        return table

    def sold_tickets_for_each_sellperson_in_last_30_days(self, sold_tickets_data):
        headers = ["ID", "Sellperson", "Total price", "Total count"]
        table = tabulate(sold_tickets_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        return table

    def display_reserved_tickets_for_user(self, user_reserved_ticket):
        reserved_ticket_data = []
        i = 0
        for ticket in user_reserved_ticket:
            i += 1
            reserved_ticket_data.append([i, ticket.projection_term.code, ticket.projection_term.movie_projection.movie,
                                         ticket.projection_term.date.strftime('%d.%m.%Y.'),
                                         ticket.projection_term.movie_projection.start_time,
                                         ticket.projection_term.movie_projection.end_time,
                                         ticket.seat_label])
        headers = ["ID", "Projection term code", "Movie", "Date", "Start time", "End time", "Seat label"]
        table = tabulate(reserved_ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center")
        print(table)

    def display_all_tickets(self):
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
            "ID", "Code term", "Owner", "Movie", "Date", "Start time",
            "End time", "Seat label", "Status"
        ]

        print(tabulate(ticket_data, headers=headers, tablefmt="fancy_grid", numalign="center"))
