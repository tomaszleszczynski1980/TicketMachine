import tkinter as tk
from machine import Item


items = {
    Item('dwudziestominutowy ulgowy', 1.70): 5,
    Item('dwudziestominutowy normalny', 3.40): 10,
    Item('jednorazowy ulgowy', 2.20): 100,
    Item('jednorazowy normalny', 4.40): 34,
    Item('dwustrefowy ulgowy', 3.50): 45,
    Item('dwustrefowy normalny', 7.00): 2,
}


def increase():
    value = int(item.widget.value["text"])
    if value < 10:
        item.widget.value["text"] = f"{value + 1}"

def decrease():
    value = int(item.widget.value["text"])
    if value > 0:
        item.widget.value["text"] = f"{value - 1}"


window = tk.Tk()

window.rowconfigure(len(items) - 1, minsize=50, weight=1)
window.columnconfigure([0, 1, 2, 3], minsize=50, weight=1)

for index, item in enumerate(items.keys()):

    item.widget.name = tk.Label(master=window, text=item.name)
    item.widget.name.grid(row=index, column=0)

    item.widget.button_decrease = tk.Button(master=window, text="-", command=item.widget.decrease)
    item.widget.button_decrease.grid(row=index, column=1, sticky="nsew")

    item.widget.value = tk.Label(master=window, text="0")
    item.widget.value.grid(row=index, column=2)

    item.widget.button_increase = tk.Button(master=window, text="+", command=item.widget.increase)
    item.widget.button_increase.grid(row=index, column=3, sticky="nsew")

window.mainloop()
