import tkinter as tk
from tkinter import messagebox

class Regist:
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.email = ""
        self.login = ""
        self.phone_number = ""
        self.password = ""

def show_registration_window(parent_window):
    registration_window = tk.Toplevel(parent_window)
    registration_window.title("Registration")
    registration_window.geometry("300x300")

    name_label = tk.Label(registration_window, text="Name:")
    name_label.pack()

    name_entry = tk.Entry(registration_window)
    name_entry.pack()

    surname_label = tk.Label(registration_window, text="Surname:")
    surname_label.pack()

    surname_entry = tk.Entry(registration_window)
    surname_entry.pack()

    email_label = tk.Label(registration_window, text="Email:")
    email_label.pack()

    email_entry = tk.Entry(registration_window)
    email_entry.pack()

    phone_label = tk.Label(registration_window, text="Phone Number:")
    phone_label.pack()

    phone_entry = tk.Entry(registration_window)
    phone_entry.pack()

    login_label = tk.Label(registration_window, text="Login:")
    login_label.pack()

    login_entry = tk.Entry(registration_window)
    login_entry.pack()

    password_label = tk.Label(registration_window, text="Password:")
    password_label.pack()

    password_entry = tk.Entry(registration_window, show="*")
    password_entry.pack()

    password_test_label = tk.Label(registration_window, text="Confirm Password:")
    password_test_label.pack()

    password_test_entry = tk.Entry(registration_window, show="*")
    password_test_entry.pack()

    register_button = tk.Button(registration_window, text="Register", command=lambda: register(user, name_entry, surname_entry, email_entry, phone_entry, login_entry, password_entry, password_test_entry, registration_window))
    register_button.pack()

def register(user, name_entry, surname_entry, email_entry, phone_entry, login_entry, password_entry, password_test_entry, registration_window):
    user.name = name_entry.get()
    user.surname = surname_entry.get()
    user.email = email_entry.get()
    user.phone_number = phone_entry.get()
    user.login = login_entry.get()

    user.password = password_entry.get()
    password_test = password_test_entry.get()

    if user.password == password_test:
        with open("register.txt", "a") as file:
            file.write("Login: " + user.login + '\n')
            file.write("Name: " + user.name + '\n')
            file.write("Surname: " + user.surname + '\n')
            file.write("Email: " + user.email + '\n')
            file.write("Phone Number: " + user.phone_number + '\n')
            file.write("Password: " + user.password + '\n')

        messagebox.showinfo("Registration Successful", "Registration successful!")
        registration_window.destroy()
    else:
        messagebox.showerror("Password Mismatch", "Passwords do not match. Please try again.")

def login():
    login = login_entry.get()
    password = password_entry.get()

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
                    messagebox.showinfo("Login Successful", f"Name: {user.name}\nSurname: {user.surname}\nEmail: {user.email}\nPhone Number: {user.phone_number}")
                    return

        messagebox.showerror("Login Failed", "Invalid login or password.")

def main():
    global login_entry, password_entry, user
    window = tk.Tk()
    window.title("Login/Register")
    window.geometry("300x300")

    choice_label = tk.Label(window, text="Select an option:")
    choice_label.pack()

    login_entry = tk.Entry(window)  # Added login entry field
    login_entry.pack()

    password_entry = tk.Entry(window, show="*")  # Added password entry field
    password_entry.pack()

    login_button = tk.Button(window, text="Login", command=login)
    login_button.pack()

    registration_button = tk.Button(window, text="Registration", command=lambda: show_registration_window(window))
    registration_button.pack()

    user = Regist()

    window.mainloop()

if __name__ == "__main__":
    main()
