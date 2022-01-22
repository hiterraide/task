from class_user import User
class Admin(User):
    def __init__ (self, first_name, last_name, age, birthday, privileges):
        User.__init__(self, first_name, last_name, age, birthday)
        self.privileges = privileges
    def show_privileges(self):
        print("Админ:")
        print(f"Привилегии админа: {self.privileges}")




my_admin = Admin("Kirill", "Antonov", 15, "23.01.2006", "Разрешено добавлять пользователей, разрешено удалять пользователей, разрешено банить пользователей")
my_admin.show_privileges()



    

class Privileges:
    def __init__(self, privileges):
        Admin.__init__(privileges)
        Super().__init__(show_privileges)


priv = Admin("Kirill", "Antonov", 15, "23.01.2006", "Разрешено добавлять пользователей, разрешено удалять пользователей, разрешено банить пользователей")
priv.show_privileges()
