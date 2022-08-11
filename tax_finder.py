import tkinter as tk
from tkinter import ttk
import clipboard
# from tkinter.messagebox import showinfo
class Tax_finder:
    def __init__(self, root, main_window):

        self.TAX = 1.0825

        self.total_price = 100
        self.labor_price = 55
        self.part_price = 0

        self.TEXT_ENTRY_LENGTH = 7

        self.tax_finder_frame = ttk.Frame(root)
        self.tax_finder_frame.pack(padx=10, pady=10, fill='x', expand=True)

        self.total_price_label = None
        self.labor_price_label = None
        self.part_price_label = None

        self.total_price_entry = None
        self.labor_price_entry = None
        self.part_price_result_lable = None

        self.submit_button = None
        self.main_window = main_window
        self.root = root

    def calc_tax_price(self):
        total = float(self.total_price_entry.get())
        labor = float(self.labor_price_entry.get())
        self.part_price = float((total - labor) / self.TAX)
        self.total_entry.delete(0, tk.END)
        self.total_entry.insert(0, f'{self.part_price:.2f}')



    def setup(self):

        self.tax_directions = ttk.Label(self.tax_finder_frame, text="Enter full ammount and labor to find price for part", font=("Arial", 15))
        self.total_price_label = ttk.Label(self.tax_finder_frame, text="Enter Full Price")
        self.labor_price_label = ttk.Label(self.tax_finder_frame, text="Enter Full Labor Price")
        self.part_price_label = ttk.Label(self.tax_finder_frame, text="Price For Part")
        self.part_price_result_lable = ttk.Label(self.tax_finder_frame, text="")


        self.total_price_entry = ttk.Entry(
            self.tax_finder_frame,
            textvariable = self.total_price,
            width = self.TEXT_ENTRY_LENGTH,
            justify = "right"
            )

        self.labor_price_entry = ttk.Entry(
            self.tax_finder_frame,
            textvariable = self.labor_price,
            width = self.TEXT_ENTRY_LENGTH,
            justify = "right"
            )

        self.total_entry = ttk.Entry(
            self.tax_finder_frame,
            width = self.TEXT_ENTRY_LENGTH,
            justify = "right"
            )

        self.total_entry.insert(0, "0.00")
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

        self.submit_button = ttk.Button(
           self.tax_finder_frame,
           text="Submit",
           command = self.calc_tax_price
        )

        self.tax_directions.pack(pady=20)

        self.total_price_label.pack()
        self.total_price_entry.pack()

        self.labor_price_label.pack()
        self.labor_price_entry.pack()

        self.part_price_label.pack()
        self.total_entry.pack()

        self.submit_button.pack()

        self.labor_price_entry.insert(0, "55.00")
        def handle_enter_button(e):
            self.calc_tax_price()

        self.main_window.bind('<Return>', handle_enter_button)
