import tkinter as tk

def create_label_entry(window, label_text):
    label = tk.Label(window, text=label_text)
    label.pack()
    entry = tk.Entry(window)
    entry.pack()
    return entry


def book_hotel():
    hotel_name = entry_hotel_name.get()
    check_in = entry_check_in.get()
    check_out = entry_check_out.get()

   
    selected_room_type = room_type_options.get()
    price_per_day = room_prices[selected_room_type]

    confirmation_message = f"Hotel: {hotel_name}\nCheck-in: {check_in}\nCheck-out: {check_out}\nRoom Type: {selected_room_type}\nPrice per day: {price_per_day}"
    lbl_confirmation.config(text=confirmation_message)

   
    with open("booking.txt", "w") as f:
        f.write(confirmation_message)

  
    with open("register.txt", "r") as f:
        _, surname = f.readline().strip().split()
        user_info = f"Surname: {surname}"
        lbl_user_info.config(text=user_info)



window = tk.Tk()
window.title("Hotel Booking Service")

entry_hotel_name = create_label_entry(window, "Hotel Name:")
entry_check_in = create_label_entry(window, "Check-in Date:")
entry_check_out = create_label_entry(window, "Check-out Date:")


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


btn_book = tk.Button(window, text="Book", command=book_hotel)
btn_book.pack()


lbl_confirmation = tk.Label(window)
lbl_confirmation.pack()


lbl_user_info = tk.Label(window)
lbl_user_info.pack()

window.mainloop()
