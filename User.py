import re
from datetime import datetime, timedelta

from tabulate import tabulate

from SoldTicketController import SoldTicketController


class User:
    def __init__(self, username, password, name, surname, role):
        self.username = username
        self.password = password
        self.name = name
        self.surname = surname
        self.role = role

    def check_eligibility_for_discount(self):
        sold_tickets_controller = SoldTicketController()
        sold_tickets_controller.load_sold_tickets()
        list_of_sold_tickets = sold_tickets_controller.list_of_sold_tickets
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

    @staticmethod
    def valid_username(username):
        regex_username = r"^[a-z0-9_.]+$"
        if re.match(regex_username, username):
            return True
        else:
            return False

    @staticmethod
    def valid_password(password):
        return len(password) > 6 and any(char.isdigit() for char in password)

    @staticmethod
    def valid_name(name):
        regex_name = r"^[A-Z][a-z]{2,29}$"
        if re.match(regex_name, name):
            return True
        else:
            return False

    @staticmethod
    def valid_surname(surname):
        regex_surname = r"^[A-Z][a-z]{2,29}$"
        if re.match(regex_surname, surname):
            return True
        else:
            return False

    def display_user_staro(self):
        user_info = (f"Username: {self.username}\nPassword: {self.password}\nName: {self.name}\nSurname: {self.surname}"
                     f"\nRole: {self.role}\n")
        print(user_info)

    def display_user(self):
        user_info = [
            ["Username", self.username],
            ["Password", self.password],
            ["Name", self.name],
            ["Surname", self.surname],
            ["Role", self.role]
        ]
        table = tabulate(user_info, headers=["Attribute", "Information"], tablefmt="grid")
        print(table)
