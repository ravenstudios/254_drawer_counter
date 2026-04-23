import tkinter as tk
from tkinter import ttk
import clipboard
from tkinter import messagebox


class Tax_finder:
    def __init__(self, root, main_window):

        self.TAX = 1.0825

        self.TEXT_ENTRY_LENGTH = 7

        self.frame = ttk.Frame(root)
        self.frame.pack(padx=10, pady=10, fill='x', expand=True)

        self.lbl_directions = None

        self.lbl_total_before_tax = None
        self.lbl_total_after_tax = None

        self.ent_total_before_tax = None
        self.ent_total_after_tax = None

        self.submit_button = None
        self.root = root

    def calc_tax_price(self):
        try:
            before_tax = float(self.ent_total_before_tax.get())
            after_tax = f"{before_tax / self.TAX:.2f}"

            self.ent_total_after_tax.delete(0, tk.END)
            self.ent_total_after_tax.insert(0, after_tax)

            clipboard.copy(after_tax)

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            self.ent_total_before_tax.delete(0, tk.END)

            self.root.lift()
            self.root.focus_force()
            self.ent_total_before_tax.focus_set()


    def setup(self):
        self.lbl_directions = ttk.Label(
            self.frame,
            text="Enter total price and hit enter or click submit. The discounted price will show below and be copied to clipboard",
            wraplength=200
            )
        self.lbl_total_before_tax = ttk.Label(self.frame, text="Total with tax")
        self.lbl_total_after_tax = ttk.Label(self.frame, text="Discounted price after tax")


        self.ent_total_before_tax = ttk.Entry(
            self.frame,
            width = self.TEXT_ENTRY_LENGTH,
            justify = "right"
            )


        self.ent_total_after_tax = ttk.Entry(
            self.frame,
            width = self.TEXT_ENTRY_LENGTH,
            justify = "right"
            )

        # self.ent_total_before_tax.insert(0, "100")
        self.ent_total_after_tax.insert(0, "0.00")


        # def copy():
        #     clipboard.copy(self.ent_total_after_tax.get())



        self.submit_button = ttk.Button(
           self.frame,
           text="Submit",
           command = self.calc_tax_price
        )

        self.lbl_directions.pack(pady=50)
        self.lbl_total_before_tax.pack()
        self.ent_total_before_tax.pack()

        self.lbl_total_after_tax.pack()
        self.ent_total_after_tax.pack()

        self.submit_button.pack()


        def handle_enter_button(e):
            self.calc_tax_price()

        self.ent_total_before_tax.bind('<Return>', handle_enter_button)
