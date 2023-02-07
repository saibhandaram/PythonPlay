from tkinter import *


def mile_to_km():
    miles = float(mile_input.get())
    km = miles * 1.609
    km_result_label.config(text=f"{km}")


window = Tk()
window.title("Mile to KM converter")
window.config(padx=20, pady=20)

mile_input = Entry(width=7)
mile_input.grid(column=1, row=0)

mile_label = Label(text="Mile")
mile_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=1, row=1)

km_result_label = Label(text="0")
km_result_label.grid(column=2, row=1)

km_label = Label(text="Km")
km_label.grid(column=3, row=1)

calculate_button = Button(text="Calculate", command= mile_to_km)
calculate_button.grid(column=3, row=3)

window.mainloop()
