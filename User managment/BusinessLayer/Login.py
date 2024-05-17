from DataAccessLayer.DataAccess import DataAccess
from CommonLayer.performance import performanceRecorder

class Login:
    def __init__(self):
        self.data_access_layer = DataAccess
    @performanceRecorder
    def check_username_password(self,username, password):
        print(username,password)
        UserDataAccess = DataAccess()
        user = UserDataAccess.get_user(username,password)
        print(user.firstName,user.lastName)
        if user and user.Active == 0:
            return user
        else:
            raise ValueError("Invalid Username or Password(not Found)")
