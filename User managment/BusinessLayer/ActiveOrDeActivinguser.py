from DataAccessLayer.DataAccess import DataAccess


class Active_or_DeActive:
    def Active(self,user):
        Dataaccess = DataAccess()
        id = []
        for i in user:
            id.append(i[0])

        change = Dataaccess.ActiveUser(id)
    def DeActive(self,user):
        Dataaccess = DataAccess()
        id = []
        for i in user:
            id.append(i[0])

        change = Dataaccess.DeActiveUser(id)
