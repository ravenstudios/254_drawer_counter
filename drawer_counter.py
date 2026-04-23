import tkinter as tk
from tkinter import ttk
import clipboard


class DrawerCounter:
    def __init__(self, root, main_window, log):
        self.denominations = ["Hundreds", "Fifties", "Twenties", "Tens", "Fives", "Ones", "Rolls", "Quarters", "Dimes", "Nickels", "Pennies"]
        self.denom_values = [100, 50, 20, 10, 5, 1, 1, 0.25, 0.1, 0.05, 0.01]
        self.labels = []
        self.entries = []
        self.values = []
        self.root = root
        self.total = 0
        self.index = 1
        self.TEXT_ENTRY_LENGTH = 7
        self.main_window = main_window
        self.log = log

        self.log_after_id = None
        self.LOG_DELAY = 60000

        self.frame = ttk.Frame(root)
        self.frame.pack(padx=10, pady=0, fill='x', expand=True)

        self.total_entry = ttk.Entry(
            self.frame,
            width = self.TEXT_ENTRY_LENGTH,
            justify = "right"
            )

        self.directions = "Enter the quantity of bills and change. Rolls use the exact dollar ammount."

        self.error_label = ttk.Label(self.frame, text = self.directions, font=("Arial", 10))
        self.error_label.config(foreground="black")
        self.lbl_log_message = ttk.Label(self.frame, text="")
        self.lbl_log_message.config(foreground="red")
        self.main_window.bind('<Return>', self.next_entry)


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
        self.show_total()



    def handle_click(self, e):
        self.index = self.entries.index(e.widget)
        self.entries[self.index].focus()
        self.entries[self.index].selection_range(0, tk.END)
        self.index += 1



    def setup(self):
        self.error_label.pack(pady=(20, 0))
        self.lbl_log_message.pack()
        for i in range(len(self.denominations)):
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


            self.entries[i].bind("<ButtonPress-1>", self.handle_click)


            if i == 6:
                self.entries[i].insert(0, "0.00")
            else:
                self.entries[i].insert(0, "0")

            self.entries[i].pack()
            self.load()


        self.total_label = ttk.Label(self.frame, text="Total")
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


    def show_total(self):
        self.index += 1
        self.error_label.config(foreground="black")
        self.error_label["text"] = self.directions
        self.total_entry.delete(0, tk.END)
        total = self.get_total()
        self.total_entry.insert(0, total)

        if self.log_after_id is not None:
            self.root.after_cancel(self.log_after_id)

        self.log_after_id = self.root.after(self.LOG_DELAY, lambda: self.save_log(total))



    def get_total(self):
        total = 0
        for i in range(len(self.entries)):
            try:
                total += float(self.entries[i].get()) * self.denom_values[i]
            except Exception as e:
                self.invalid_number_error(self.entries[i])
                return
        return total


    def save_log(self, total):
        self.log_after_id = None
        values = [e.get() for e in self.entries]
        data_dict = dict(zip(self.denominations, values))
        data = self.log.make_entry(data_dict)
        data["total"] = total
        self.log.write_row(data)
        self.show_log_message()


    def load(self):
        log = self.log.read_log()

        if log:
            for i in range(len(self.entries)):
                self.entries[i].delete(0, tk.END)
                self.entries[i].insert(0, log[-1][self.denominations[i]])

            self.total_entry.delete(0, tk.END)
            self.total_entry.insert(0, log[-1]["total"])


    def show_log_message(self):
        self.lbl_log_message.config(text="Log Saved")
        self.root.after(3000, self.hide_log_message)


    def hide_log_message(self):
        self.lbl_log_message.config(text="")
