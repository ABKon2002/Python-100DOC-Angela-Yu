
from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width = 300, height = 120)
window.config(padx = 50, pady = 50)

# TODO: Component 1 - The entry field [r = 0, c = 1]
miles_entry = Entry(width = 12)
miles_entry.grid(row = 0, column = 1)

# TODO: Component 2 - The label to the right of the entry field (miles) [r = 0, c = 2]
miles_label = Label(text = "miles")
miles_label.grid(row = 0, column = 2)


# TODO: Component 3 - The label to the bottom left of the entry field (is equal to) [r = 1, c = 0]
equal_to_label = Label(text = "is equal to")
equal_to_label.grid(row = 1, column = 0)

# TODO: Component 4 - The output label in the bottom of the entry field (Km value) [r = 1, c = 1]
km_value_label = Label(text = "")
km_value_label.grid(row = 1, column = 1)

# TODO: Component 5 - The label to the right of the output label (Km) [r = 1, c = 2]
km_label = Label(text = "km")
km_label.grid(row = 1, column = 2)


# TODO: Component 6 - The calculate button [r = 2, c = 1]
def convert_to_km():
    """
    Converts the value entered in miles_entry from miles to kilometers,
    rounds the result, and updates the km_value_label with the converted value.
    """
    miles = float(miles_entry.get())
    km = round(miles * 1.609)
    km_value_label.config(text = km)

calculate_button = Button(text = "Calculate", command = convert_to_km)
calculate_button.grid(row = 2, column = 1)


window.mainloop()