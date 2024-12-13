class Database:
    def __init__(self):
        self.data = {}
    def add_useer(self,username, password):
        self.data[username] = password





class User:
    """"
    Касс пользователя, содержащий в атрибутах логин и пароль
    """

    def __init__(self,username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password

if __name__ == '__main__':
    database = Database()
    user = User(input("Введите логин: "), input("Ввдетие пароль: "), input("Введите парольЖ"))
    database.add_useer(user.username, user.password)