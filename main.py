import tkinter as tk
from tkinter import ttk
import drawer_counter
import tax_finder
from log import Log
from show_log import ShowLog

def main():
    root = tk.Tk()
    root.geometry("450x1000")
    root.title('Drawer Cash Counter')

    tabControl = ttk.Notebook(root)
    tabControl.bind("<<NotebookTabChanged>>", lambda event: on_tab_change(event, root))

    count_cash_tab = ttk.Frame(tabControl)
    show_log_tab = ttk.Frame(tabControl)
    find_tax_tab = ttk.Frame(tabControl)

    tabControl.add(count_cash_tab, text="Cash Counter")
    tabControl.add(find_tax_tab, text="Find Tax")
    tabControl.add(show_log_tab, text="Logs")

    tf = tax_finder.TaxFinder(find_tax_tab, root)
    log = Log()
    show_log = ShowLog(show_log_tab, root, log)
    dc = drawer_counter.DrawerCounter(count_cash_tab, root, log)

    tabControl.pack(expand=1, fill='both')

    tf.setup()
    dc.setup()
    show_log.setup()

    root.mainloop()


def on_tab_change(event, root):
    selected_tab = event.widget.select()
    tab_text = event.widget.tab(selected_tab, "text")

    if tab_text == "Logs":
        root.geometry("1300x1000")
    else:
        root.geometry("450x1000")

    root.update_idletasks()


if __name__ == "__main__":
    main()
