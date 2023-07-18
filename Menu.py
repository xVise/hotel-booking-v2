import tkinter as tk
import subprocess
import os
import json

class Regist:
    def __init__(self):
        self.name = ""
        self.surname = ""
        self.email = ""
        self.login = os.environ.get("LOGIN")
        self.phone_number = ""

class Hotel:
    def __init__(self, name, location, price, description):
        self.name = name
        self.location = location
        self.price = price
        self.description = description

def select_hotel():
    subprocess.Popen(["python", "interface.py"])
    pass

def create_hotel_info():
    subprocess.Popen(["python", "proposal.py"])

def search_hotel():
    subprocess.Popen(["python", "funct1.py"])

def all_hotels():
    subprocess.Popen(["python", "GetInfo.py"])

def filter_hotels():
    subprocess.Popen(["python", "Filter.py"])

    

def open_account_form(root):
    account_window = tk.Toplevel(root)
    account_info = f"Name: {user.name}\nSurname: {user.surname}\nEmail: {user.email}\nPhone Number: {user.phone_number}"
    account_label = tk.Label(account_window, text=account_info)
    account_label.pack()

def load_hotels():
    hotels = []
    with open("hotels.txt", "r") as file:
        hotel_info = ""
        for line in file:
            if line.startswith("-" * 30):
                if hotel_info:
                    hotel_data = json.loads(hotel_info)
                    hotel = Hotel(hotel_data['name'], hotel_data['location'], hotel_data['price'], hotel_data['description'])
                    hotels.append(hotel)
                hotel_info = ""
            else:
                hotel_info += line
    return hotels[:5]  # Return the first 5 hotels

def main():
    global user
    user = Regist()

    # Reading account information from file based on the login
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
    root.title("Main menu")
    root.geometry("800x500")
    select_hotel_button = tk.Button(root, text="Select Hotel", command=select_hotel)
    select_hotel_button.pack(side='top')

    create_hotel_info_button = tk.Button(root, text="Create Hotel Info", command=create_hotel_info)
    create_hotel_info_button.pack(side='top')

    search_hotel_button = tk.Button(root, text="Search Hotel", command=search_hotel)
    search_hotel_button.pack(side='top')

    search_hotel_button = tk.Button(root, text="Filter Hotels", command=filter_hotels)
    search_hotel_button.pack(side='top')

    search_hotel_button = tk.Button(root, text="All Hotels", command=all_hotels)
    search_hotel_button.pack(side='top')

    hotels = load_hotels()
    for hotel in hotels:
        hotel_label = tk.Label(root, text=f"Name: {hotel.name}\nLocation: {hotel.location}\nPrice: {hotel.price}")
        hotel_label.pack(side='bottom')

    open_account_form_button = tk.Button(root, text="Open Account Form", command=lambda: open_account_form(root))
    open_account_form_button.pack(side='top')

    root.mainloop()

if __name__ == "__main__":
    main()
