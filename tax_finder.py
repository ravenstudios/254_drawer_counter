import tkinter as tk
from tkinter import ttk
# from tkinter.messagebox import showinfo
class Tax_finder:
    def __init__(self, root):
        self.total_price = 0
        self.labor = 55
        self.part_price = 0;
        self.TEXT_ENTRY_LENGTH = 7

        # root window


        self.frame = ttk.Frame(root)
        self.frame.pack(padx=10, pady=10, fill='x', expand=True)

        self.total_entry = ttk.Entry(
            self.frame,
            textvariable=self.total,
            width = self.TEXT_ENTRY_LENGTH,
            justify = "right"
            )

        self.directions = "Enter the quantity of bills and change. Rolls use the exact dollar ammount."

        self.error_label = ttk.Label(self.frame, text = self.directions, font=("Arial", 12))
        self.error_label.config(foreground="black")

        root.bind('<Return>', self.next_entry)


    def invalid_number_error(self, entry):
        entry.focus()
        entry.delete(0, tk.END)
        entry.insert(0, "0")
        entry.selection_range(0, tk.END)
        self.error_label.config(foreground="red")
        self.error_label["text"] = "Must enter a number"






    def next_entry(self, e):
        print("ne")
        self.entries[self.index % len(self.entries)].focus()
        self.entries[self.index % len(self.entries)].selection_range(0, tk.END)
        self.get_total()

    def handle_click(self, e):
        self.index
        self.index = entries.index(e.widget)
        self.entries[index].focus()
        self.entries[index].selection_range(0, tk.END)
        self.index += 1
        print(self.index)


    def setup(self):
        self.error_label.pack(pady=(20, 20))

        # sep = ttk.Separator(frame, orient='horizontal').pack(fill = "x")

        for i in range(len(self.denominations)):
            if i == 6 or i == 7:
                sep = ttk.Separator(self.frame, orient='horizontal').pack(fill = "x")

            self.labels.append(ttk.Label(self.frame, text=self.denominations[i]))
            self.labels[i].pack()

            self.values.append(tk.StringVar())

            self.entries.append(ttk.Entry(
                self.frame,
                textvariable = self.values[i],
                width = self.TEXT_ENTRY_LENGTH,
                justify = "right"
                ))

            self.entries[i].bind("<ButtonPress-1>", self.handle_click)
            if i == 6:
                self.entries[i].insert(0, "0.00")
            else:
                self.entries[i].insert(0, "0")

            self.entries[i].pack()

        self.sep = ttk.Separator(self.frame, orient='horizontal').pack(fill = "x")

        self.total_label = ttk.Label(self.frame, text="Total")
        self.total_entry.insert(0, "0.00")
        self.total_label.pack()

        self.total_entry.pack()

        self.entries[0].focus()
        self.entries[0].selection_range(0, tk.END)

        # sep = ttk.Separator(frame, orient='horizontal').pack(fill = "x")


    def get_total(self):
        self.index, self.error_label
        total = 0
        for i in range(len(self.entries)):
            try:
                total += float(self.entries[i].get()) * self.denom_values[i]

            except Exception as e:
                self.invalid_number_error(self.entries[i])
                return


        self.index += 1
        self.error_label.config(foreground="black")
        self.error_label["text"] = self.directions
        self.total_entry.delete(0, tk.END)
        self.total_entry.insert(0, total)
