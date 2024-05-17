from DataAccessLayer.DataAccess import DataAccess
from CommonLayer.performance import performanceRecorder


class userManagement:
    @performanceRecorder
    def get_all_users(self):
        GetALLTHEUSERS = DataAccess()
        users = GetALLTHEUSERS.get_all_users()
        return users

