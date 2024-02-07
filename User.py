from datetime import datetime, timedelta
from SoldTicketController import SoldTicketController
from DisplayController import DisplayController

display_controller = DisplayController()
sold_tickets_controller = SoldTicketController()
sold_tickets_controller.load_sold_tickets()
list_of_sold_tickets = sold_tickets_controller.list_of_sold_tickets


class User:
    def __init__(self, username, password, name, surname, role):
        self.username = username
        self.password = password
        self.name = name
        self.surname = surname
        self.role = role

    def check_eligibility_for_discount(self):
        end_date = datetime.now().date()
        start_date = end_date - timedelta(days=365)
        filtered_list = []
        for sold_ticket in list_of_sold_tickets:
            if self.username == sold_ticket.ticket.owner and start_date <= sold_ticket.ticket.date <= end_date:
                filtered_list.append(sold_ticket)

        if not filtered_list:
            return False

        total_price = 0.0
        if filtered_list:
            for sold_ticket in filtered_list:
                total_price += float(sold_ticket.price)
            if total_price >= float(5000):
                return True
            else:
                return False

    def display_user(self):
        display_controller.display_user(self)
