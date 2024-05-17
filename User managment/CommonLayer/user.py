class User:
    def __init__(self, id, firstName, lastName, username, password, isActive, Role):
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.username = username
        self.password = password
        self.Active = isActive
        self.Role = Role
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self,username):
        if len(username) < 3:
            raise ValueError("Invalid username or password(user")
        else:
            self._username = username
