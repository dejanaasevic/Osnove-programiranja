from MovieProjectionTermController import MovieProjectionTermController
from SoldTicket import SoldTicket
from TicketController import TicketController

movie_projection_term_controller = MovieProjectionTermController()
movie_projection_term_controller.load_projection_terms()
list_of_projection_terms = movie_projection_term_controller.list_of_projection_terms
ticket_controller = TicketController()
ticket_controller.load_tickets()
list_of_tickets = ticket_controller.list_of_tickets


def save_sold_ticket(sold_ticket):
    with open('sold_tickets.txt', 'a') as file:
        file.write(f"{sold_ticket.sellperson}|{sold_ticket.ticket.owner}|{sold_ticket.ticket.projection_term.code}|"
                   f"{sold_ticket.ticket.seat_label}|{sold_ticket.ticket.date}|{sold_ticket.ticket.status}"
                   f"|{sold_ticket.price}\n")


class SoldTicketController:
    def __init__(self):
        self.list_of_sold_tickets = []

    def load_sold_tickets(self):
        with open('sold_tickets.txt', 'r') as file:
            for line in file:
                ticket_info = line.strip().split('|')
                ticket_code = ticket_info[2] + '|' + ticket_info[3]
                for ticket in list_of_tickets:
                    if (ticket.status == "2" and ticket.projection_term.code == ticket_code and
                            ticket.seat_label == ticket_info[4] and ticket.owner == ticket_info[1]):
                        self.list_of_sold_tickets.append(SoldTicket(ticket_info[0], ticket, ticket_info[7]))

    def add_sold_ticket(self, sold_ticket):
        if isinstance(sold_ticket, SoldTicket):
            print("evo")
            self.list_of_sold_tickets.append(sold_ticket)
            save_sold_ticket(sold_ticket)
            return True
        else:
            print("evo1")
            if not isinstance(sold_ticket, SoldTicket):
                print("Prosleđen objekat nije tipa SoldTicket")
                return False
