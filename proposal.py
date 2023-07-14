import tkinter as tk
import json

def save_hotel_info():
    hotel = {
        "price": price_entry.get(),
        "location": location_entry.get(),
        "name": name_entry.get(),
        "description": description_text.get("1.0", tk.END)
    }

    with open("hotels.txt", "a") as file:
        file.write(json.dumps(hotel) + "\n")
        file.write("-" * 30 + "\n")

    # Clear the input fields after saving
    price_entry.delete(0, tk.END)
    location_entry.delete(0, tk.END)
    name_entry.delete(0, tk.END)
    description_text.delete("1.0", tk.END)

    # Update the success message label
    success_label.config(text="Hotel added successfully!")

# Create the Tkinter window
window = tk.Tk()
window.title("Hotel Information")
window.geometry("400x350")

# Price input field
price_label = tk.Label(window, text="Price:")
price_label.pack()
price_entry = tk.Entry(window)
price_entry.pack()

# Location input field
location_label = tk.Label(window, text="Location:")
location_label.pack()
location_entry = tk.Entry(window)
location_entry.pack()

# Name input field
name_label = tk.Label(window, text="Name:")
name_label.pack()
name_entry = tk.Entry(window)
name_entry.pack()

# Description input field
description_label = tk.Label(window, text="Description:")
description_label.pack()
description_text = tk.Text(window, height=5)
description_text.pack()

# Save button
save_button = tk.Button(window, text="Save", command=save_hotel_info)
save_button.pack()

# Success message label
success_label = tk.Label(window, text="")
success_label.pack()

window.mainloop()