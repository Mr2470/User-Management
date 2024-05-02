from .Window import Window
from .login import login
from .homeFrame import homeFrame
from .UserManagementTable import usermanagement
from .Register import Register
class mainveiwer:
    def __init__(self):
        self.window=Window()
        self.Frames = {}
        self.AddFrame("Register",Register(self.window,self))
        self.AddFrame("UserManagementFrame",usermanagement(self.window,self))
        self.AddFrame("Home",homeFrame(self.window,self))
        self.AddFrame("login", login(self.window,self))
        self.window.show()
    def AddFrame(self, FrameName, Frame):
        self.Frames[FrameName] = Frame
        self.Frames[FrameName].grid(row=0,column=0,sticky="wnes")

    def switch(self,FrameName):
        Frame = self.Frames[FrameName]
        Frame.tkraise()
        return Frame
