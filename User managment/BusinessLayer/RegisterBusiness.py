from DataAccessLayer.DataAccess import DataAccess
from CommonLayer.performance import performanceRecorder

class Registerclass:
    @performanceRecorder
    def Register(self,fname,lname,username,password):
        print(fname,lname,username,password)
        dataaccess=DataAccess()
        register = dataaccess.Register(fname,lname,username,password)
