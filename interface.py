import tkinter as tk

def create_label_entry(window, label_text):
    label = tk.Label(window, text=label_text)
    label.pack()
    entry = tk.Entry(window)
    entry.pack()
    return entry

# Function to book the hotel
def book_hotel():
    hotel_name = entry_hotel_name.get()
    check_in = entry_check_in.get()
    check_out = entry_check_out.get()

    # Get the selected room type and its price
    selected_room_type = room_type_options.get()
    price_per_day = room_prices[selected_room_type]

    confirmation_message = f"Hotel: {hotel_name}\nCheck-in: {check_in}\nCheck-out: {check_out}\nRoom Type: {selected_room_type}\nPrice per day: {price_per_day}"
    lbl_confirmation.config(text=confirmation_message)


# Create the main window
window = tk.Tk()
window.title("Hotel Booking Service")


entry_hotel_name = create_label_entry(window, "Hotel Name:")
entry_check_in = create_label_entry(window, "Check-in Date:")
entry_check_out = create_label_entry(window, "Check-out Date:")

# Room Type Selection
lbl_room_type = tk.Label(window, text="Select Room Type:")
lbl_room_type.pack()

room_type_options = tk.StringVar(window)
room_type_options.set("Standard")  # Set the default room type

room_prices = {
    "Standard": 100,
    "Deluxe": 150,
    "Suite": 200,
    "Executive": 250,
    "Luxury": 300
}

room_type_dropdown = tk.OptionMenu(window, room_type_options, *room_prices.keys())
room_type_dropdown.pack()

# Book Button
btn_book = tk.Button(window, text="Book", command=book_hotel)
btn_book.pack()

# Confirmation Label
lbl_confirmation = tk.Label(window)
lbl_confirmation.pack()


window.mainloop()