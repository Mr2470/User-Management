from DataAccessLayer.DataAccess import DataAccess


class userManagement:
    def get_all_users(self):
        GetALLTHEUSERS = DataAccess()
        users = GetALLTHEUSERS.get_all_users()
        return users

