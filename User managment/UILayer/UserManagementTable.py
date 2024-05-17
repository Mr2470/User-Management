from ttkbootstrap import Frame, Button, END
from tkinter import messagebox
from tkinter.ttk import Treeview
from BusinessLayer.UserManagement import userManagement
from BusinessLayer.ActiveOrDeActivinguser import Active_or_DeActive

class usermanagement(Frame):
    def __init__(self, window, mainviewer):
        super().__init__(window)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.mainviwer = mainviewer
        self.ActiveButton = Button(self, text="ACTIVE",command=self.ActiveBTN)
        self.ActiveButton.grid(row=0, column=0, sticky="w", columnspan=2)
        self.DeActiveButton = Button(self, text="DEACTIVE",command=self.DeActiveBTN)
        self.DeActiveButton.grid(row=0, column=1, columnspan=2, sticky="e")

    def set_user(self, user):
        self.user_things = user
        self.CreateTable()

    def CreateTable(self):
        self.columnss = (
            self.user_things.firstName, self.user_things.lastName, self.user_things.username, self.user_things.Active,
            self.user_things.Role)
        self.Table = Treeview(self, columns=self.columnss)
        self.Table.grid(row=1, column=1, sticky="news")
        self.Table.heading("#0", text="NO")
        self.Table.heading(self.columnss[0], text="firstName")
        self.Table.heading(self.columnss[1], text="lastName")
        self.Table.heading(self.columnss[2], text="username")
        self.Table.heading(self.columnss[3], text="is Active")
        self.Table.heading(self.columnss[4], text="Role")
        self.Table.column("#0", width=30, anchor="w")
        self.Table.column(self.columnss[0], width=100, anchor="center")
        self.Table.column(self.columnss[1], width=100, anchor="center")
        self.Table.column(self.columnss[2], width=100, anchor="center")
        self.Table.column(self.columnss[3], width=100, anchor="center")
        self.Table.column(self.columnss[4], width=100, anchor="center")
        self.USMANAGEMENT = userManagement()
        self.users = self.USMANAGEMENT.get_all_users()
        self.row = 1
        for i in self.users:
            self.Table.insert("", END, iid=f"{i[0]}", text=f"{self.row}", values=(
                i[1], i[2], i[3], "Active" if i[4] == 0 else "Not Active", "Admin" if i[5] == 1 else "Default"))
            self.row += 1

    def ActiveBTN(self):
        users = []
        for i in self.Table.selection():
            for z in self.users:
                if int(i) == z[0]:
                    users.append(z)
                    break
        for i in users:
            if i[4] == 0:
                messagebox.showerror(title="wrong people",message="wrong input(you chose the wrong people)")
                raise ValueError("error")
        print(users)
        self.choice = Active_or_DeActive()
        self.change = self.choice.Active(users)
        self.CreateTable()
    def DeActiveBTN(self):
        users = []
        for i in self.Table.selection():
            for z in self.users:
                if int(i) == z[0]:
                    users.append(z)
                    break
        for i in users:
            if i[4] == 1:
                messagebox.showerror(title="wrong people", message="wrong input(you chose the wrong people)")
                raise ValueError("error")
        print(users)
        self.choice2 = Active_or_DeActive()
        self.change2 = self.choice2.DeActive(users)
        self.CreateTable()
