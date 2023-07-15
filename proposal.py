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


fields = [
    ("Price:", tk.Entry(window)),
    ("Location:", tk.Entry(window)),
    ("Name:", tk.Entry(window)),
    ("Description:", tk.Text(window, height=5))
]


for label, input_field in fields:
    label_widget = tk.Label(window, text=label)
    label_widget.pack()
    input_field.pack()

    if label == "Price:":
        price_entry = input_field
    elif label == "Location:":
        location_entry = input_field
    elif label == "Name:":
        name_entry = input_field
    elif label == "Description:":
        description_text = input_field


save_button = tk.Button(window, text="Save", command=save_hotel_info)
save_button.pack()


success_label = tk.Label(window, text="")
success_label.pack()

window.mainloop()