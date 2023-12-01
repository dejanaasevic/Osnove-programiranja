from UserController import UserController
from User import User

current_user = None


def display_menu():
    print("MENI")
    print("_____")
    print("Izaberite opciju:")
    print("1. Registrujte se")
    print("2. Prijavite se")
    print("3. Izlaz iz aplikacije")
    choice = input("Unesite broj opcije: ")
    print()
    return choice


def display_user_menu():
    global current_user
    if current_user is None:
        print("Niste prijavljeni.")
        return
    choice = str(current_user.role)
    if choice == "1":
        display_menu_for_registered_customer()
    elif choice == "2":
        display_menu_for_registered_salesperson()
    else:
        display_menu_for_registered_menager()


def display_menu_for_registered_customer():
    print("MENI KORISNIKA:")
    print("_______________")
    print("IZABERITE OPCIJU:")
    print("1. Odjava sa sistema: ")
    print("2. Izmena licnih podataka")
    print("3. Izlaz iz aplikacije")
    choice = input("Unesite broj opcije: ")
    if choice == "1":
        log_out()
    elif choice == "2":
        change_personal_information()
    elif choice == "3":
        exit_application()
    else:
        print("Nevažeća opcija. Molimo pokušajte ponovo.")


def display_menu_for_registered_salesperson():
    print("MENI PRODAVCA")
    print("______________")
    print("Izaberite opciju:")
    print("1. Odjava sa sistema: ")
    print("2. Izmena licnih podataka")
    print("3. Izlaz iz aplikacije")
    choice = input("Unesite broj opcije: ")
    if choice == "1":
        log_out()
    elif choice == "2":
        change_personal_information()
    elif choice == "3":
        exit_application()
    else:
        print("Nevažeća opcija. Molimo pokušajte ponovo.")


def display_menu_for_registered_menager():
    print("MENI MENADZERA")
    print("______________")
    print("Izaberi opciju:")
    print("1. Odjava sa sistema: ")
    print("2. Izmena licnih podataka")
    print("3. Izlaz iz aplikacije")
    print("4. Registracija novih prodavaca")
    print("5. Registracija novih menadzera")
    choice = input("Unesite broj opcije: ")
    if choice == "1":
        log_out()
    elif choice == "2":
        change_personal_information()
    elif choice == "3":
        exit_application()
    elif choice == "4":
        register_new_sellperson()
    elif choice == "5":
        register_new_menager()
    else:
        print("Nevažeća opcija. Molimo pokušajte ponovo.")


def login():
    global current_user
    print("PRIJAVA NA SISTEM")
    print("_________________")
    print("Unesite -1 za povratak nazad")
    while True:
        username = input("Unesite korisničko ime: ")
        if username == "-1":
            main()
            return
        password = input("Unesite lozinku: ")
        if password == "-1":
            main()
            return
        if user_controller.authenticate_user(username, password):
            print("Uspešno ste se prijavili!")
            current_user = user_controller.get_user(username)
            display_user_menu()
        else:
            print("Pogrešno korisničko ime ili lozinka. Molimo pokušajte ponovo.")


def log_out():
    global current_user
    current_user = None
    print("Uspešno ste se odjavili")
    print()
    main()


def exit_application():
    print("Hvala što ste koristili aplikaciju. Doviđenja!")
    exit()


def change_personal_information():
    global current_user
    while True:
        print("IZMENA LICNIH INFORMACIJA:")
        print("_______________________")
        print("Unesite -1 za povratak nazad")
        print("1. Ime")
        print("2. Prezime")
        print("3. Lozinka")
        choice = input("Unesite odgovarajuci broj: ")
        if choice == "-1":
            display_user_menu()
            return

        elif choice == "1":
            new_name = input("Unesite novo ime:")
            if new_name == "-1":
                display_user_menu()
                return
            elif not User.valid_name(new_name):
                print("Nevažeće ime. Molimo pokušajte ponovo.")
                continue
            else:
                current_user.name = new_name
                if user_controller.update_user_in_list(current_user):
                    print('Ušepsno ste izmenili ime')
                    current_user.display_user()

        elif choice == "2":
            new_surname = input("Unesite novo prezime:")
            if new_surname == "-1":
                display_user_menu()
                return
            if not User.valid_surname(new_surname):
                print("Nevažeće prezime. Molimo pokušajte ponovo.")
                continue
            else:
                current_user.surname = new_surname
                if user_controller.update_user_in_list(current_user):
                    print('Usepsno ste izmenili prezime')
                    current_user.display_user()
        elif choice == "3":
            new_password = input("Unesite novu lozinku (minimum 6 karaktera sa bar jednom cifrom): ")
            if new_password == "-1":
                display_user_menu()
                return
            if not User.valid_password(new_password):
                print("Nevažeće lozinka. Molimo pokušajte ponovo.")
                continue
            else:
                current_user.password = new_password
                if user_controller.update_user_in_list(current_user):
                    print('Usepsno ste izmenili lozinku')
                    current_user.display_user()
                else:
                    print("Niste uspesno promenili lozinku, molimo probajte ponovo")
        else:
            print("Nevažeća opcija. Molimo pokušajte ponovo.")
    print()


def registration():
    global current_user
    print("REGISTRACIJA NA SISTEM:")
    print("_______________________")
    while True:
        print("Unesite -1 za povratak nazad")
        username = input("Unesite Vaše korisničko ime: ")
        if username == '-1':
            main()
            return
        elif not User.valid_username(username):
            print("Nevažeće korisničko ime. Molimo pokušajte ponovo.")
            continue

        password = input("Unesite željenu lozinku: ")
        if password == '-1':
            main()
            return
        elif not User.valid_password(password):
            print("Nevažeća lozinka. Molimo pokušajte ponovo.")
            continue

        name = input("Unesite Vaše ime: ")
        if name == '-1':
            main()
            return
        elif not User.valid_name(name):
            print("Nevažeće ime. Molimo pokušajte ponovo.")
            continue

        surname = input("Unesite Vaše prezime: ")
        if surname == '-1':
            main()
            return
        elif not User.valid_surname(surname):
            print("Nevažeće prezime. Molimo pokušajte ponovo.")
            continue

        role = 1

        new_user = User(username, password, name, surname, role)
        current_user = new_user
        if user_controller.add_user(new_user):
            print("Uspešno ste se registrovali!!!")
            display_user_menu()
            break
        else:
            print("Registracija nije uspela. Molimo pokušajte ponovo.")
    print()


def register_new_sellperson():
    while True:
        print("Za povratak na meni unesite: -1")
        username = input("Unesite korisničko ime: ")
        if username == "-1":
            display_user_menu()
            return
        elif not User.valid_username(username):
            print("Nevažeće korisničko ime. Molimo pokušajte ponovo.")
            continue

        password = input("Unesite lozinku: ")
        if password == "-1":
            display_user_menu()
            return
        elif not User.valid_password(password):
            print("Nevažeća lozinka. Molimo pokušajte ponovo.")
            continue

        name = input("Unesite ime: ")
        if name == "-1":
            display_user_menu()
            return
        elif not User.valid_name(name):
            print("Nevažeće ime. Molimo pokušajte ponovo.")
            continue

        surname = input("Unesite prezime: ")
        if surname == "-1":
            display_user_menu()
            return
        elif not User.valid_surname(surname):
            print("Nevažeće prezime. Molimo pokušajte ponovo.")
            continue

        role = 2

        register_new_sellperson = User(username, password, name, surname, role)
        if user_controller.add_user(register_new_sellperson):
            print("Uspesno ste registrovali novog prodavca")
            display_user_menu()
        else:
            print("Registracija nije uspela. Molimo pokušajte ponovo.")


def register_new_menager():
    while True:
        print("Za povratak na meni unesite: -1")
        username = input("Unesite korisničko ime: ")
        if username == "-1":
            display_user_menu()
            return
        elif not User.valid_username(username):
            print("Nevažeće korisničko ime. Molimo pokušajte ponovo.")
            continue

        password = input("Unesite lozinku: ")
        if password == "-1":
            display_user_menu()
            return
        elif not User.valid_password(password):
            print("Nevažeća lozinka. Molimo pokušajte ponovo.")
            continue

        name = input("Unesite ime: ")
        if name == "-1":
            display_user_menu()
            return
        elif not User.valid_name(name):
            print("Nevažeće ime. Molimo pokušajte ponovo.")
            continue

        surname = input("Unesite prezime: ")
        if surname == "-1":
            display_user_menu()
            return
        elif not User.valid_surname(surname):
            print("Nevažeće prezime. Molimo pokušajte ponovo.")
            continue
        role = 3
        register_new_sellperson = User(username, password, name, surname, role)
        if user_controller.add_user(register_new_sellperson):
            print("Uspesno ste registrovali novog menadzera")
            display_user_menu()
        else:
            print("Registracija nije uspela. Molimo pokušajte ponovo.")


def main():
    while True:
        choice = display_menu()
        if choice == "1":
            registration()
        elif choice == "2":
            login()
        elif choice == "3":
            exit_application()
        else:
            print("Uneta je neispravna opcija. Molimo pokušajte ponovo.")


if __name__ == '__main__':
    user_controller = UserController()
    user_controller.load_users()
    main()
