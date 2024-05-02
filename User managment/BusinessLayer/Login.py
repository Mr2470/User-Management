from DataAccessLayer.DataAccess import DataAccess


class Login:
    def __init__(self):
        self.data_access_layer = DataAccess

    def check_username_password(self,username, password):
        if len(username) < 3 or len(password) < 3:
            raise ValueError("Invalid username or password")
        UserDataAccess = DataAccess()
        user = UserDataAccess.get_user(username,password)
        if user and user.Active == 0:
            return user
        else:
            raise ValueError("Invalid Username or Password(not Found)")
