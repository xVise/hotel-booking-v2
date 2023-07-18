import tkinter as tk
import json

class Hotel:
    def __init__(self, name, location, price):
        self.name = name
        self.location = location
        self.price = price

def load_hotels():
    hotels = []
    with open("Hotels.txt", "r") as file:
        hotel_info = ""
        for line in file:
            if line.startswith("-" * 30):
                if hotel_info:
                    hotel_data = json.loads(hotel_info)
                    hotel = Hotel(hotel_data['name'], hotel_data['location'], hotel_data['price'])
                    hotels.append(hotel)
                hotel_info = ""
            else:
                hotel_info += line
    return hotels[:5]  # Return the first 5 hotels

def main():
    root = tk.Tk()
    root.geometry("250x300")  # Set the size of the window

    hotels = load_hotels()
    for hotel in hotels:
        hotel_label = tk.Label(root, text=f"Name: {hotel.name}\nLocation: {hotel.location}\nPrice: {hotel.price}")
        hotel_label.pack(side='top')

    root.mainloop()

if __name__ == "__main__":
    main()
