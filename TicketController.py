from datetime import datetime

from Ticket import Ticket
from MovieProjectionTermController import MovieProjectionTermController

movie_projection_term_controller = MovieProjectionTermController()
movie_projection_term_controller.load_projection_terms()
list_of_projection_terms = movie_projection_term_controller.list_of_projection_terms


def save_ticket(ticket):
    with open('tickets.txt', 'a') as file:
        file.write(f"{ticket.owner}|{ticket.projection_term.code}|{ticket.seat_label}|{ticket.date}|{ticket.status}\n")


def remove_ticket_from_file(ticket):
    with open('tickets.txt', 'r') as file:
        lines = file.readlines()

    with open('tickets.txt', 'w') as file:
        for line in lines:
            ticket_info = line.strip().split('|')
            ticket_code = ticket_info[1] + '|' + ticket_info[2]
            if (
                    ticket_info[0] == ticket.owner and
                    ticket_code == ticket.projection_term.code and
                    ticket_info[3] == ticket.seat_label
            ):
                continue

            file.write(line)


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
                                                           ticket_info[3], ticket_info[5]))
                        list_of_projection_terms[-1].date = ticket_info[4]

    def add_ticket(self, ticket):
        if isinstance(ticket, Ticket):
            self.list_of_tickets.append(ticket)
            save_ticket(ticket)
            return True
        else:
            if not isinstance(ticket, Ticket):
                print("Prosleđen objekat nije tipa User")
                return False

    def remove_ticket(self, ticket_item):
        for ticket in self.list_of_tickets:
            if (
                    ticket.owner == ticket_item.owner and
                    ticket.projection_term.code == ticket_item.projection_term.code and
                    ticket.seat_label == ticket_item.seat_label and
                    ticket.date == ticket_item.date and
                    ticket.status == ticket_item.status
            ):
                remove_ticket_from_file(ticket)
                self.list_of_tickets.remove(ticket)

                return True
        return False
