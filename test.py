import tkinter as tk
from tkinter import ttk

class TabbedInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Tabbed Interface")

        self.tabControl = ttk.Notebook(self.master)

        self.tab1 = ttk.Frame(self.tabControl)
        self.tab2 = ttk.Frame(self.tabControl)
        self.tab3 = ttk.Frame(self.tabControl)

        self.tabControl.add(self.tab1, text="Tab 1")
        self.tabControl.add(self.tab2, text="Tab 2")
        self.tabControl.add(self.tab3, text="Tab 3")

        self.tabControl.pack(expand=1, fill="both")

        self.create_content_in_tab1()
        self.create_content_in_tab2()
        self.create_content_in_tab3()

    def create_content_in_tab1(self):
        label1 = tk.Label(self.tab1, text="Content for Tab 1")
        label1.pack(pady=10)

    def create_content_in_tab2(self):
        label2 = tk.Label(self.tab2, text="Content for Tab 2")
        label2.pack(pady=10)

    def create_content_in_tab3(self):
        label3 = tk.Label(self.tab3, text="Content for Tab 3")
        label3.pack(pady=10)

def main():
    root = tk.Tk()
    app = TabbedInterface(root)
    root.mainloop()

if __name__ == "__main__":
    main()
