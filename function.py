from datetime import datetime, timedelta
from CinemaHall import CinemaHall
from CinemaHallController import CinemaHallController
from DisplayController import DisplayController
from Movie import Movie
from MovieController import MovieController
from MovieCriterion import MovieCriterion
from MovieProjection import MovieProjection
from MovieProjectionController import MovieProjectionController
from MovieProjectionTerm import MovieProjectionTerm
from MovieProjectionTermController import MovieProjectionTermController
from MovieProjectionTermCriterion import MovieProjectionTermCriterion
from ReportController import ReportController
from SoldTicket import SoldTicket
from SoldTicketController import SoldTicketController
from Ticket import Ticket
from TicketController import TicketController, update_ticket_in_file
from TicketCriterion import TicketCriterion
from User import User
from UserController import UserController
from tabulate import tabulate


# main function


if __name__ == '__main__':
    user_controller = UserController()
    user_controller.load_users()

    movie_controller = MovieController()
    movie_controller.load_movies()

    movie_projection_controller = MovieProjectionController()
    movie_projection_controller.load_projections()

    movie_projection_term_controller = MovieProjectionTermController()
    movie_projection_term_controller.load_projection_terms()

    ticket_controller = TicketController()
    ticket_controller.load_tickets()

    cinema_hall_controller = CinemaHallController()
    cinema_hall_controller.load_cinema_halls()

    sold_tickets_controller = SoldTicketController()
    sold_tickets_controller.load_sold_tickets()

    display_controller = DisplayController()
    report_controller = ReportController()
