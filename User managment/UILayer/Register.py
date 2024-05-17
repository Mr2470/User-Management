from ttkbootstrap import Frame, Label, Entry, Button, END
from BusinessLayer.RegisterBusiness import Registerclass


class Register(Frame):
    def __init__(self, window, mainviewer):
        super().__init__(window)
        self.mainviewer = mainviewer
        self.grid_columnconfigure(1, weight=1)
        self.firstNameLabel = Label(self, text="please insert your first name : ")
        self.firstNameLabel.grid(row=0, column=0, pady=10, padx=10)
        self.firstNameEntry = Entry(self)
        self.firstNameEntry.grid(row=0, column=1, pady=10, padx=(0, 10), sticky="we")

        self.lastNameLabel = Label(self, text="please insert your last name : ")
        self.lastNameLabel.grid(row=1, column=0, pady=(0, 10), padx=10)
        self.lastNameEntry = Entry(self)
        self.lastNameEntry.grid(row=1, column=1, pady=(0, 10), padx=(0, 10), sticky="we")

        self.userNameLabel = Label(self, text="please insert your username : ")
        self.userNameLabel.grid(row=2, column=0, pady=(0, 10), padx=10)
        self.userNameEntry = Entry(self)
        self.userNameEntry.grid(row=2, column=1, pady=(0, 10), padx=(0, 10), sticky="we")

        self.passwordLabel = Label(self, text="please insert your password : ")
        self.passwordLabel.grid(row=3, column=0, pady=(0, 10), padx=10)
        self.passwordEntry = Entry(self)
        self.passwordEntry.grid(row=3, column=1, pady=(0, 10), padx=(0, 10), sticky="we")

        self.RegisterBTN = Button(self, text="Register", command=self.Register)
        self.RegisterBTN.grid(row=4, column=1, sticky="w")

    def Register(self):
        if len(self.userNameEntry.get()) > 3 and len(self.lastNameEntry.get()) > 3 and len(
                self.userNameEntry.get()) > 3 and len(self.passwordEntry.get()) > 3:
            RegisterInstance = Registerclass()
            register = RegisterInstance.Register(self.firstNameEntry.get(), self.lastNameEntry.get(),
                                                 self.userNameEntry.get(), self.passwordEntry.get())
            self.firstNameEntry.delete(0, END)
            self.lastNameEntry.delete(0, END)
            self.userNameEntry.delete(0, END)
            self.passwordEntry.delete(0, END)
            self.mainviewer.switch("login")
