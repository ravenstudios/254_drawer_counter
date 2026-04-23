import tkinter as tk
from tkinter import ttk
import clipboard
from tkinter import messagebox


class ShowLog:
    def __init__(self, root, main_window, log):
        self.frame = ttk.Frame(root)
        self.frame.pack(padx=10, pady=10, fill='x', expand=True)

        self.dom_lables = []
        self.value_lables = []
        self.log = log
        self.root = root




    def setup(self):
        log = self.log.read_log()

        if not log:
            self.dom_lables.append(ttk.Label(self.frame, text="No log yet"))
        else:
            logs = log[-20:]

            for item in logs:
                self.dom_lables.append(ttk.Label(self.frame, text=str(item)))

        for lbl in self.dom_lables:
            lbl.pack()


        # self.lbl_directions = ttk.Label(
        #     self.frame,
        #     text="Enter total price and hit enter or click submit. The discounted price will show below and be copied to clipboard",
        #     wraplength=200
        #     )
        # self.lbl_total_before_tax = ttk.Label(self.frame, text="Total with tax")
        # self.lbl_total_after_tax = ttk.Label(self.frame, text="Discounted price after tax")
        #
        #
        # self.ent_total_before_tax = ttk.Entry(
        #     self.frame,
        #     width = self.TEXT_ENTRY_LENGTH,
        #     justify = "right"
        #     )
        #
        #
        # self.ent_total_after_tax = ttk.Entry(
        #     self.frame,
        #     width = self.TEXT_ENTRY_LENGTH,
        #     justify = "right"
        #     )
        #
        # # self.ent_total_before_tax.insert(0, "100")
        # self.ent_total_after_tax.insert(0, "0.00")
        #
        #
        # # def copy():
        # #     clipboard.copy(self.ent_total_after_tax.get())
        #
        #
        #
        # self.submit_button = ttk.Button(
        #    self.frame,
        #    text="Submit",
        #    command = self.calc_tax_price
        # )
        #
        # self.lbl_directions.pack(pady=50)
        # self.lbl_total_before_tax.pack()
        # self.ent_total_before_tax.pack()
        #
        # self.lbl_total_after_tax.pack()
        # self.ent_total_after_tax.pack()
        #
        # self.submit_button.pack()


        # def handle_enter_button(e):
        #     self.calc_tax_price()
        #
        # self.ent_total_before_tax.bind('<Return>', handle_enter_button)

        def load(self):
            log = self.log.read_log()

            if log:
                for i in range(len(self.entries)):
                    self.entries[i].delete(0, tk.END)
                    self.entries[i].insert(0, log[-1][self.denominations[i]])

            self.total_entry.delete(0, tk.END)
            self.total_entry.insert(0, log[-1]["total"])
