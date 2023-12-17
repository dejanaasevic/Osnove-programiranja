from User import User


def save_user(user):
    with open('users.txt', 'a') as file:
        file.write(
            f"{user.username},{user.password},{user.name},{user.surname},{user.role}\n")


def update_user_in_file(updated_user):
    with open('users.txt', 'r') as file:
        lines = file.readlines()

    with open('users.txt', 'w') as file:
        for line in lines:
            data = line.strip().split(',')
            if data[0] == updated_user.username:
                updated_line = ",".join([
                    updated_user.username, updated_user.password,
                    updated_user.name, updated_user.surname,
                    str(updated_user.role)
                ]) + "\n"
                file.write(updated_line)
            else:
                file.write(line)


class UserController:
    def __init__(self):
        self.list_of_users = []

    def load_users(self):
        with open('users.txt', 'r') as file:
            for line in file:
                new_user = line.strip().split(',')
                self.list_of_users.append(User(*new_user))

    def unique_username(self, username):
        for user in self.list_of_users:
            if username == user.username:
                return False
        return True

    def add_user(self, user):
        if isinstance(user, User) and self.unique_username(user.username):
            self.list_of_users.append(user)
            save_user(user)
            return True
        else:
            if not isinstance(user, User):
                print("Prosleđen objekat nije tipa User")
                return False
            if not self.unique_username(user.username):
                print("Korisničko ime već postoji")
                return False

    def get_user(self, username):
        for user in self.list_of_users:
            if user.username == username:
                return user
        return None

    def update_user_in_list(self, updated_user):
        for user in self.list_of_users:
            if user.username == updated_user.username:
                if User.valid_password(updated_user.password) and User.valid_name(
                        updated_user.name) and User.valid_surname(updated_user.surname):
                    user.name = updated_user.name
                    user.surname = updated_user.surname
                    user.password = updated_user.password
                    user.role = updated_user.role
                    update_user_in_file(updated_user)
                    return True
                else:
                    return False

    def authenticate_user(self, username, password):
        for user in self.list_of_users:
            if user.username == username and user.password == password:
                return True
        return False
