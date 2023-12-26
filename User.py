import re

from tabulate import tabulate


class User:
    def __init__(self, username, password, name, surname, role):
        self.username = username
        self.password = password
        self.name = name
        self.surname = surname
        self.role = role

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
