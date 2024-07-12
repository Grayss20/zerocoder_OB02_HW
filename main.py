class User():
    def __init__(self, idn, name):
        self.__idn = idn
        self.name = name
        self.level = 'user'

    def get_id(self):
        return self.__idn

    def set_id(self, idn):
        self.__idn = idn


class Admin(User):
    def __init__(self, idn, name, access_level):
        super().__init__(idn, name)
        self.level = 'admin'
        self.access_level = access_level

    def add_user(self):
        pass

    def remove_user(self):
        pass



ad1 = Admin(1, 'Grayss', 'admin')
ad1.add_user()