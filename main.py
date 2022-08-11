import tkinter as tk
from tkinter import ttk
import drawer_counter
import tax_finder
import inventory

# from tkinter.messagebox import showinfo



root = tk.Tk()
root.geometry("450x1000")
root.title('Drawer Cash Counter')

tabControl = ttk.Notebook(root)
count_cash_tab = ttk.Frame(tabControl)
find_tax_tab = ttk.Frame(tabControl)
inventory_tab = ttk.Frame(tabControl)
tabControl.add(count_cash_tab, text="Cash Counter")
tabControl.add(find_tax_tab, text="Find Tax")
tabControl.add(inventory_tab, text="Inventory")

inv = inventory.Inventory(inventory_tab)
tf = tax_finder.Tax_finder(find_tax_tab, root)
dc = drawer_counter.Drawer_counter(count_cash_tab, root)


tabControl.pack(expand=1, fill='both')


tf.setup()
dc.setup()

root.attributes('-topmost',True)




root.mainloop()
stay_on_top()
