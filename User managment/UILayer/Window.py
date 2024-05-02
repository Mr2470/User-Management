from tkinter import Tk


class Window(Tk):
    def __init__(self, size="600x300"):
        super().__init__()

        self.title("User Management Application")


        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.geometry(size)

    def show(self):
        self.mainloop()