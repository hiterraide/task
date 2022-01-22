class User:
    def __init__ (self, first_name, last_name, age, birthday):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.birthday = birthday
        self.login_attempts = 0
    def describe_user(self):
        print(f"Имя: {self.first_name}\nФамилия: {self.last_name}\nВозраст: {self.age}\nДата рождения: {self.birthday}")
    def greeting_user(self):
        print(f"Здравствуйте {self.first_name} {self.last_name}")
    def reset_login_attempts(self):
       while self.login_attempts > 0:
           self.login_attempts -=1
           print(f"Количество попыток входа успешно обнулилось: {my_user.login_attempts}")
    def increment_login_attempts(self, increment_login):
        self.login_attempts += increment_login
        






my_user = User("Kirill", "Antonov", 15, "23.01.2006")
my_user.describe_user()
my_user.greeting_user()
##дада у меня в воскресенье др)
increment_login =+ 1
my_user.increment_login_attempts(increment_login)
my_user.increment_login_attempts(increment_login)
my_user.increment_login_attempts(increment_login)
print(f"Количество попыток входа: {my_user.login_attempts}")
my_user.reset_login_attempts()






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
