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


def remove_sold_ticket_from_file(sold_ticket):
    with open('sold_tickets.txt', 'r') as file:
        lines = file.readlines()
    with open('sold_tickets.txt', 'w') as file:
        for line in lines:
            sold_ticket_info = line.strip().split('|')
            ticket_code = sold_ticket_info[2] + '|' + sold_ticket_info[3]
            if (sold_ticket_info[0] == sold_ticket.sellperson and
                    sold_ticket_info[1] == sold_ticket.ticket.owner and
                    ticket_code == sold_ticket.ticket.projection_term.code and
                    sold_ticket_info[4] == sold_ticket.ticket.seat_label and
                    sold_ticket_info[5] == sold_ticket.ticket.date and
                    sold_ticket_info[6] == sold_ticket.ticket.status and
                    sold_ticket_info[7] == sold_ticket.price
            ):
                continue
            file.write(line)


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
            self.list_of_sold_tickets.append(sold_ticket)
            save_sold_ticket(sold_ticket)
            return True
        else:
            if not isinstance(sold_ticket, SoldTicket):
                print("Prosleđen objekat nije tipa SoldTicket")
                return False

    def remove_sold_ticket(self, ticket):
        for sold_ticket in self.list_of_sold_tickets:
            if (sold_ticket.ticket.projection_term.code == ticket.projection_term.code and
                    sold_ticket.ticket.seat_label == ticket.seat_label and
                    sold_ticket.ticket.owner == ticket.owner and
                    sold_ticket.ticket.date == ticket.date):
                remove_sold_ticket_from_file(sold_ticket)
                self.list_of_sold_tickets.remove(sold_ticket)
                return True
        return False

    @staticmethod
    def update_sold_ticket_in_file(file_ticket, updated_ticket):
        with open('sold_tickets.txt', 'r') as file:
            lines = file.readlines()
        with open('sold_tickets.txt', 'w') as file:
            for line in lines:
                sold_ticket_info = line.strip().split('|')
                ticket_code = sold_ticket_info[2] + '|' + sold_ticket_info[3]
                if (sold_ticket_info[1] == file_ticket.owner and
                        ticket_code == file_ticket.projection_term.code and
                        sold_ticket_info[4] == file_ticket.seat_label and
                        sold_ticket_info[5] == file_ticket.ticket.date
                ):
                    formatted_date = updated_ticket.date.strftime('%d.%m.%Y.')
                    updated_line = "|".join([
                        sold_ticket_info[0], updated_ticket.owner, updated_ticket.projection_term.code,
                        updated_ticket.seat_label, formatted_date, str(updated_ticket.status), sold_ticket_info[7]
                    ]) + "\n"
                file.write(updated_line)
            else:
                file.write(line)
