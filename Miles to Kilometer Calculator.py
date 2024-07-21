# trying to convert miles to kilometer using tkinter
# making a GUI based program for the first time :)

import tkinter
window = tkinter.Tk()
window.title("Miles to Kilometer Converter")
window.minsize(width=500, height=300)

# Label
my_label = tkinter.Label(text="is equal to", font=("Arial", 24, "bold"))
my_label.pack()


def add(*args):
    print(args[0] + args[1] + args[2])


add(3,5,6) 