import tkinter as tk
from tkinter import ttk
import drawer_counter
# from tkinter.messagebox import showinfo



root = tk.Tk()
root.geometry("450x650")
root.title('Drawer Cash Counter')

dc = drawer_counter.Drawer_counter(root)

dc.setup()

root.mainloop()
