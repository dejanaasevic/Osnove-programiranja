import re


class ValidationController:

    def user_valid_username(self, username):
        regex_username = r"^[a-z0-9_.]+$"
        if re.match(regex_username, username):
            return True
        else:
            return False

    def user_valid_password(self, password):
        return len(password) > 6 and any(char.isdigit() for char in password)

    def user_valid_name(self, name):
        regex_name = r"^[A-Z][a-z]{2,29}$"
        if re.match(regex_name, name):
            return True
        else:
            return False

    def user_valid_surname(self, surname):
        regex_surname = r"^[A-Z][a-z]{2,29}$"
        if re.match(regex_surname, surname):
            return True
        else:
            return False