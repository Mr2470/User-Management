from DataAccessLayer.DataAccess import DataAccess
class Registerclass:
    def Register(self,fname,lname,username,password):
        print(fname,lname,username,password)
        dataaccess=DataAccess()
        register = dataaccess.Register(fname,lname,username,password)
