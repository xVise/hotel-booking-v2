import tkinter as tk

def search_city():
    query = entry.get().lower()
    with open("hotels.txt", "r") as file:
        results = [line.strip() for line in file if query in line.lower()]
    
    result_text.delete("1.0", tk.END)
    
    if results:
        result_text.insert(tk.END, "Search results:\n" + "\n".join(results))
    else:
        result_text.insert(tk.END, "No results found.")

def create_and_pack_widget(widget_type, parent, **kwargs):
    widget = widget_type(parent, **kwargs)
    widget.pack()
    return widget

window = tk.Tk()
window.title("City Search")

label = create_and_pack_widget(tk.Label, window, text="Search:")

entry = create_and_pack_widget(tk.Entry, window)

search_button = create_and_pack_widget(tk.Button, window, text="Search", command=search_city)

result_text = create_and_pack_widget(tk.Text, window)

window.mainloop()
