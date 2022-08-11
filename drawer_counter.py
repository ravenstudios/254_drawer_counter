import tkinter as tk
from tkinter import ttk
import clipboard
# from tkinter.messagebox import showinfo
class Drawer_counter:
    def __init__(self, root, main_window):
        self.denominations = ["Hundreds", "Fifties", "Twentys", "Tens", "Fives", "Ones", "Rolls", "Quarters", "Dimes", "Nickels", "Pennies"]
        self.denom_values = [100, 50, 20, 10, 5, 1, 1, 0.25, 0.1, 0.05, 0.01]
        self.labels = []
        self.entries = []
        self.values = []
        self.root = root
        self.total = 0
        self.index = 0
        self.TEXT_ENTRY_LENGTH = 7

        # root window


        self.frame = ttk.Frame(root)
        self.frame.pack(padx=10, pady=0, fill='x', expand=True)

        self.total_entry = ttk.Entry(
            self.frame,
            textvariable=self.total,
            width = self.TEXT_ENTRY_LENGTH,
            justify = "right"
            )

        self.directions = "Enter the quantity of bills and change. Rolls use the exact dollar ammount."

        self.error_label = ttk.Label(self.frame, text = self.directions, font=("Arial", 10))
        self.error_label.config(foreground="black")

        main_window.bind('<Return>', self.next_entry)


    def invalid_number_error(self, entry):
        entry.focus()
        entry.delete(0, tk.END)
        entry.insert(0, "0")
        entry.selection_range(0, tk.END)
        self.error_label.config(foreground="red")
        self.error_label["text"] = "Must enter a number"



    def next_entry(self, e):
        self.entries[self.index % len(self.entries)].focus()
        self.entries[self.index % len(self.entries)].selection_range(0, tk.END)
        self.get_total()



    def handle_click(self, e):
        self.index = entries.index(e.widget)
        self.entries[index].focus()
        self.entries[index].selection_range(0, tk.END)
        self.index += 1



    def setup(self):
        self.error_label.pack(pady=(20, 0))

        # sep = ttk.Separator(frame, orient='horizontal').pack(fill = "x")

        for i in range(len(self.denominations)):
            # if i == 6 or i == 7:
                # sep = ttk.Separator(self.frame, orient='horizontal').pack(fill = "x")

            self.labels.append(ttk.Label(self.frame, text=self.denominations[i]))
            self.labels[i].pack()

            self.values.append(tk.StringVar())

            self.entries.append(ttk.Entry(
                self.frame,
                textvariable = self.values[i],
                width = self.TEXT_ENTRY_LENGTH,
                justify = "right"
                ))

            m = tk.Menu(self.entries[i], tearoff=0)
            m.add_command(label="Cut")

            def do_popup(event):
                try:
                    m.tk_popup(event.x_root, event.y_root)
                finally:
                    m.grab_release()
            self.entries[i].bind("<Button-3>", do_popup)


            self.entries[i].bind("<ButtonPress-1>", self.handle_click)





            if i == 6:
                self.entries[i].insert(0, "0.00")
            else:
                self.entries[i].insert(0, "0")

            self.entries[i].pack()

        # self.sep = ttk.Separator(self.frame, orient='horizontal').pack(fill = "x")

        self.total_label = ttk.Label(self.frame, text="Total")
        self.total_entry.insert(0, "0.00")
        self.total_label.pack()

        self.total_entry.pack()

        m = tk.Menu(self.root, tearoff=0)
        m.add_command(label="Copy", command=lambda: copy())

        def copy():
            clipboard.copy(self.total_entry.get())

        def do_popup(event):
            try:
                m.tk_popup(event.x_root, event.y_root)
            finally:
                m.grab_release()
        self.total_entry.bind("<Button-2>", do_popup)


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
