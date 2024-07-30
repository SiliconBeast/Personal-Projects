# trying to convert miles to kilometer using tkinter
# making a GUI based program for the first time :)

import tkinter as tk
from tkinter import messagebox

def convert_miles_to_km():
    try:
        miles = float(entry_miles.get())
        kilometers = miles * 1.60934
        label_result.config(text=f"{kilometers:.2f} Kilometers")
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number")

# Create the main window
window = tk.Tk()
window.title("Miles to Kilometers Converter")

# Create a label for miles input
label_miles = tk.Label(window, text="Miles:")
label_miles.grid(column=0, row=0)

# Create an entry widget for miles input
entry_miles = tk.Entry(window)
entry_miles.grid(column=1, row=0)

# Create a button to trigger conversion
button_convert = tk.Button(window, text="Convert", command=convert_miles_to_km)
button_convert.grid(column=0, row=1, columnspan=2)

# Create a label to display the result
label_result = tk.Label(window, text="")
label_result.grid(column=0, row=2, columnspan=2)

# Run the Tkinter event loop
window.mainloop()
