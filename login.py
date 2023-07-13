class Regist:
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.email = ""
        self.login = ""
        self.phone_number = ""
        self.password = ""

def login():
    login = input("Enter your login: ")
    password = input("Enter your password: ")

    with open("register.txt", "r") as file:
        for line in file:
            if line.startswith("Login:"):
                user = Regist()
                user.login = line.split("Login:")[1].strip()
                user.name = file.readline().split("Name:")[1].strip()
                user.surname = file.readline().split("Surname:")[1].strip()
                user.email = file.readline().split("Email:")[1].strip()
                user.phone_number = file.readline().split("Phone Number:")[1].strip()
                user.password = file.readline().split("Password:")[1].strip()
                if user.login == login and user.password == password:
                    print("Login successful!")
                    print("Name:", user.name)
                    print("Surname:", user.surname)
                    print("Email:", user.email)
                    print("Phone Number:", user.phone_number)
                    return

        print("Login failed. Invalid login or password.")

def register():
    user = Regist()
    try:
        with open("register.txt", "a") as file:
            user.name = input("Enter your first name: ")
            user.surname = input("Enter your last name: ")
            user.login = input("Enter your login: ")
            user.email = input("Enter your email: ")
            user.phone_number = input("Enter your phone number: ")

            # Loop until passwords match
            while True:
                user.password = input("Enter your password: ")
                password_test = input("Enter your password again: ")

                if user.password == password_test:
                    break  # Passwords match, exit the loop
                else:
                    print("Passwords do not match. Please try again.")

            # Save user data to file
            file.write("Login: " + user.login + '\n')
            file.write("Name: " + user.name + '\n')
            file.write("Surname: " + user.surname + '\n')
            file.write("Email: " + user.email + '\n')
            file.write("Phone Number: " + user.phone_number + '\n')
            file.write("Password: " + user.password + '\n')

        print("Registration successful!")
    except IOError:
        print("Error opening file!")
        exit(1)

def main():   
    while True:
        print("Enter 1 to log in")
        print("Enter 2 to register")
        print("Enter 3 to exit")
        choice = input()

        if choice == "1":
            login()
            break
        elif choice == "2":
            register()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
