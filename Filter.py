import tkinter as tk
import subprocess
#Create functions for buttons
def Price_Sort():
    subprocess.Popen(["python", "price.py"])

def Alphabet_Sort():
    subprocess.Popen(["python", "alphabet.py"])

def City_Sort():
    subprocess.Popen(["python", "filterCity.py"])
#Create window with buttons
window = tk.Tk()
window.title("Фільтри")
window.geometry("200x200")
#Input button setings
button1 = tk.Button(window, text="Price sort", command=Price_Sort)
button2 = tk.Button(window, text="Alphabet sort", command=Alphabet_Sort)
button3 = tk.Button(window, text="City sort", command=City_Sort)

button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)

window.mainloop()