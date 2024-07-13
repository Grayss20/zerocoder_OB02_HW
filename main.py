class User():
    def __init__(self, idn, name):
        self.__idn = idn
        self._name = name
        self._level = 'user'

    def get_id(self):
        return self.__idn

    def set_id(self, idn):
        self.__idn = idn

    def info(self):
        print(f'ID: {self.__idn}, Name: {self._name}, Level: {self._level}')


class Admin(User):
    def __init__(self, idn, name, access_level):
        super().__init__(idn, name)
        self._level = 'admin'
        self.__access_level = access_level

    def _add_user(self,  user_list, idn, name):
        user = User(idn, name)
        user_list.append(user)

    def _remove_user(self, user_list, idn):
        for user in user_list:
            if user.get_id() == idn:
                user_list.remove(user)

    def get_access_level(self):
        return self.__access_level

    def set_access_level(self, access_level):
        self.__access_level = access_level

    def info(self):
        print(f'ID: {self._User__idn}, Name: {self._name}, Level: {self._level}, Access level: {self.__access_level}')


#   Test
admin = Admin(1, 'Admin', '5')
admin.info()

user = User(5, 'User1')
user.info()

user_list = []
admin._add_user(user_list, 2, 'User2')
admin._add_user(user_list, 3, 'User3')
admin._add_user(user_list, 4, 'User4')

user_list[2].set_id(33)
admin._remove_user(user_list, 3)


for user in user_list:
    user.info()
