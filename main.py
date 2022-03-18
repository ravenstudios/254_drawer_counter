import tkinter as tk
from tkinter import ttk
# from tkinter.messagebox import showinfo

denominations = ["Hundreds", "Fifties", "Twentys", "Tens", "Fives", "Ones", "Rolls", "Quarters", "Dimes", "Nickels", "Pennies"]
denom_values = [100, 50, 20, 10, 5, 1, 1, 0.25, 0.1, 0.05, 0.01]
labels = []
entries = []
values = []

total = 0
index = 0
TEXT_ENTRY_LENGTH = 7

# root window
root = tk.Tk()
root.geometry("450x650")
root.title('Drawer Cash Counter')

frame = ttk.Frame(root)
frame.pack(padx=10, pady=10, fill='x', expand=True)

total_entry = ttk.Entry(
    frame,
    textvariable=total,
    width = TEXT_ENTRY_LENGTH,
    justify = "right"
    )

directions = "Enter the quantity of bills and change. Rolls use the exact dollar ammount."

error_label = ttk.Label(frame, text = directions, font=("Arial", 12))
error_label.config(foreground="black")

def get_total():
    global index, error_label
    total = 0
    for i in range(len(entries)):
        try:
            total += float(entries[i].get()) * denom_values[i]

        except Exception as e:
            entries[i].focus()
            entries[i].delete(0, tk.END)
            entries[i].insert(0, "0")
            entries[i].selection_range(0, tk.END)
            error_label.config(foreground="red")
            error_label["text"] = "Must enter a number"
            return


    index += 1
    error_label.config(foreground="black")
    error_label["text"] = directions
    total_entry.delete(0, tk.END)
    total_entry.insert(0, total)



def next_entry(e):

    entries[index % len(entries)].focus()
    entries[index % len(entries)].selection_range(0, tk.END)
    get_total()

def handle_click(e):
    global index
    index = entries.index(e.widget)
    entries[index].focus()
    entries[index].selection_range(0, tk.END)
    index += 1
    print(index)


def setup():
    error_label.pack(pady=(20, 20))

    # sep = ttk.Separator(frame, orient='horizontal').pack(fill = "x")

    for i in range(len(denominations)):
        if i == 6 or i == 7:
            sep = ttk.Separator(frame, orient='horizontal').pack(fill = "x")

        labels.append(ttk.Label(frame, text=denominations[i]))
        labels[i].pack()

        values.append(tk.StringVar())

        entries.append(ttk.Entry(
            frame,
            textvariable = values[i],
            width = TEXT_ENTRY_LENGTH,
            justify = "right"
            ))

        entries[i].bind("<ButtonPress-1>", handle_click)
        if i == 6:
            entries[i].insert(0, "0.00")
        else:
            entries[i].insert(0, "0")

        entries[i].pack()

    sep = ttk.Separator(frame, orient='horizontal').pack(fill = "x")

    total_label = ttk.Label(frame, text="Total")
    total_entry.insert(0, "0.00")
    total_label.pack()

    total_entry.pack()

    entries[0].focus()
    entries[0].selection_range(0, tk.END)

    # sep = ttk.Separator(frame, orient='horizontal').pack(fill = "x")


setup()
root.bind('<Return>', next_entry)
root.mainloop()
