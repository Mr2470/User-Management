from tkinter import Frame, Label, Button


class homeFrame(Frame):
    def __init__(self, window, mainveiwer):
        super().__init__(window)
        self.grid_columnconfigure(1, weight=1)
        self.mainveiwer = mainveiwer
        self.headerLabel = Label(self, text="pleadawd")
        self.headerLabel.grid(row=0, column=0, columnspan=2)
        self.logoutButton = Button(self, text="LOG OUT", command=self.logOut)
        self.logoutButton.grid(row=10, column=1, sticky="we")

    def set_user(self, user):
        self.user_things = user
        self.headerLabel.config(text=f"Welcome {user.firstName} {user.lastName}")
        if self.user_things.Role == 1:
            self.userManagementButton = Button(self, text="USER MANAGEMENT", command=self.UserManagementBTN)
            self.userManagementButton.grid(row=2, column=1)

    def logOut(self):
        self.mainveiwer.switch("login")
        if self.user_things.Role == 1:
            self.userManagementButton.destroy()

    def UserManagementBTN(self):
        self.Frame = self.mainveiwer.switch("UserManagementFrame")
        self.Frame.set_user(self.user_things)
