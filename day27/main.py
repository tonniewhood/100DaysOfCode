
import tkinter


def calculate():
    num_miles = float(entry.get())
    num_km["text"] = f"{num_miles * 1.609344:0.1f}"


# Set window
window = tkinter.Tk()
window.title("Yeet")
window.config(padx=50, pady=35)

# Create the labels
in_miles = tkinter.Label(text="In Miles:")
in_km = tkinter.Label(text="In Kilometers:")
mi = tkinter.Label(text="mi.")
km = tkinter.Label(text="km.")
num_km = tkinter.Label()

# Create the text entry
entry = tkinter.Entry(width=5)

# Create button
button = tkinter.Button(text="Calculate", command=calculate)

# Position all elements in the grid
in_miles.grid(column=0, row=0)
entry.grid(column=1, row=0)
mi.grid(column=2, row=0)
in_km.grid(column=0, row=1)
num_km.grid(column=1, row=1)
km.grid(column=2, row=1)
button.grid(column=1, row=2)
window.mainloop()
