class Database:
    def __init__(self):
        self.data = {}

    def add_user(self,username, password):
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
    while True:
        choice = int(input("Приветствую! Выберите действие: \n1 - Вход\n2 - Регистрация\n"))
        if choice==1:
            login = input("Введите логин:")
            password = input("Введите пароль:")
            if login in database.data:
                if password == database.data[login]:
                    print(f"{login}, добро пожаловать!")
                    break
                else:
                    print("Пользователь не найден")
            else:
                print("Пользователь не найден")
        if choice==2:

            user = User(input("Введите логин: "), password := input("Ввдетие пароль: \nпароль дожен содержать не меннее 8 симвоов, хотябя "
                                                                    "одну заглавную букву и один из знаков(!, @, %, ?, -, =, $)"),
                        password2 := input("Введите пароль еще раз"))
            if password !=password2:
                "пароли не совпадают, попробуйте еще раз"
                continue
            database.add_user(user.username, user.password)

        print(database.data)
