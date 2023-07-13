import tkinter as tk

# Function to book the hotel
def book_hotel():
    hotel_name = entry_hotel_name.get()
    check_in = entry_check_in.get()
    check_out = entry_check_out.get()
    price_per_day = entry_price.get()

    # Perform the booking logic here
    
    # Display a confirmation message
    confirmation_message = f"Hotel: {hotel_name}\nCheck-in: {check_in}\nCheck-out: {check_out}\nPrice per day: {price_per_day}"
    lbl_confirmation.config(text=confirmation_message)


# Create the main window
window = tk.Tk()
window.title("Hotel Booking Service")

# Hotel Name
lbl_hotel_name = tk.Label(window, text="Hotel Name:")
lbl_hotel_name.pack()
entry_hotel_name = tk.Entry(window)
entry_hotel_name.pack()

# Check-in Date
lbl_check_in = tk.Label(window, text="Check-in Date:")
lbl_check_in.pack()
entry_check_in = tk.Entry(window)
entry_check_in.pack()

# Check-out Date
lbl_check_out = tk.Label(window, text="Check-out Date:")
lbl_check_out.pack()
entry_check_out = tk.Entry(window)
entry_check_out.pack()

# Price per Day
lbl_price = tk.Label(window, text="Price per Day:")
lbl_price.pack()
entry_price = tk.Entry(window)
entry_price.pack()

# Book Button
btn_book = tk.Button(window, text="Book", command=book_hotel)
btn_book.pack()

# Confirmation Label
lbl_confirmation = tk.Label(window)
lbl_confirmation.pack()

# Run the main event loop
window.mainloop()