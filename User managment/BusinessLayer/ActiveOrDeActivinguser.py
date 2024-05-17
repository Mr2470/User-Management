from DataAccessLayer.DataAccess import DataAccess
from CommonLayer.performance import performanceRecorder


class Active_or_DeActive:
    @performanceRecorder
    def Active(self,user):
        Dataaccess = DataAccess()
        id = []
        for i in user:
            id.append(i[0])

        change = Dataaccess.ActiveUser(id)

    @performanceRecorder
    def DeActive(self,user):
        Dataaccess = DataAccess()
        id = []
        for i in user:
            id.append(i[0])

        change = Dataaccess.DeActiveUser(id)
