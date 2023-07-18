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
    return hotels

def main():
    root = tk.Tk()
    root.title("All Hotelts")
    root.geometry("1200x700")  # Set the size of the window

    hotels = load_hotels()

    row_index = 0
    column_index = 0

    for i, hotel in enumerate(hotels):
        hotel_label = tk.Label(root, text=f"Name: {hotel.name}\nLocation: {hotel.location}\nPrice: {hotel.price}")

        # Place the hotel label using grid
        hotel_label.grid(row=row_index, column=column_index, padx=10, pady=10)

        if i % 5 == 4:
            row_index += 1
            column_index = 0  # Start from the first column
        else:
            column_index += 1  # Move to the next column

    root.mainloop()

if __name__ == "__main__":
    main()