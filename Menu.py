import tkinter as tk
import subprocess
import os

class Regist:
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.email = ""
        self.login = os.environ.get("LOGIN")
        self.phone_number = ""

def select_hotel():
    # Код для вибору готелю
    # subprocess.Popen(["python", "proposal.py"])
    pass

def create_hotel_info():
    subprocess.Popen(["python", "proposal.py"])
def search_hotel():
    # Код для пошуку готелю
    # subprocess.Popen(["python", "proposal.py"])
    pass

def open_account_form(root):
    account_window = tk.Tk()
    account_info = f"Name: {user.name}\nSurname: {user.surname}\nEmail: {user.email}\nPhone Number: {user.phone_number}"
    account_label = tk.Label(account_window, text=account_info)
    account_label.pack()

    account_window.mainloop()

def main():
    global user
    user = Regist()

    # Зчитування інформації про обліковий запис з файлу на основі логіну
    with open("register.txt", "r") as file:
        for line in file:
            if line.startswith("Login:"):
                login = line.split("Login:")[1].strip()
                if login == user.login:
                    user.name = file.readline().split("Name:")[1].strip()
                    user.surname = file.readline().split("Surname:")[1].strip()
                    user.email = file.readline().split("Email:")[1].strip()
                    user.phone_number = file.readline().split("Phone Number:")[1].strip()
                    break

    root = tk.Tk()

    select_hotel_button = tk.Button(root, text="Select Hotel", command=select_hotel)
    select_hotel_button.pack()

    create_hotel_info_button = tk.Button(root, text="Create Hotel Info", command=create_hotel_info)
    create_hotel_info_button.pack()

    search_hotel_button = tk.Button(root, text="Search Hotel", command=search_hotel)
    search_hotel_button.pack()

    open_account_form_button = tk.Button(root, text="Open Account Form", command=lambda: open_account_form(root))
    open_account_form_button.pack()

    root.mainloop()

if __name__ == "__main__":
    main()