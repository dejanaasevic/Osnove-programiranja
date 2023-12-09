from Ticket import Ticket
from MovieProjectionTermController import MovieProjectionTermController


def save_ticket(ticket):
    with open('tickets.txt', 'a') as file:
        file.write(f"{ticket.owner}|{ticket.projection_term.code}|{ticket.seat_label}|{ticket.date}|{ticket.status}\n")


movie_projection_term_controller = MovieProjectionTermController()
movie_projection_term_controller.load_projection_terms()
list_of_projection_terms = movie_projection_term_controller.list_of_projection_terms


class TicketController:
    def __init__(self):
        self.list_of_tickets = []

    def load_tickets(self):
        with open('tickets.txt', 'r') as file:
            for line in file:
                ticket_info = line.strip().split('|')
                ticket_code = ticket_info[1] + '|' + ticket_info[2]
                for projection_term in list_of_projection_terms:
                    if projection_term.code == ticket_code:
                        self.list_of_tickets.append(Ticket(ticket_info[0], projection_term,
                                                           ticket_info[3], ticket_info[4]))

    def add_ticket(self, ticket):
        if isinstance(ticket, Ticket):
            self.list_of_tickets.append(ticket)
            save_ticket(ticket)
            return True
        else:
            if not isinstance(ticket, Ticket):
                print("Prosleđen objekat nije tipa User")
                return False
