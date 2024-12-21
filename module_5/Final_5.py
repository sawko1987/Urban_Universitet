import time
class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)

    def __str__(self):
        return self.nickname

    def __eq__(self, other):
        if isinstance(other, User):
            return self.nickname


    def get_info(self): #возвращаем nickname и password
        return self.nickname,hash(self.password)


class Video:
    time_now = 0
    def __init__(self,title, duration, adult_mode = False):

        self.title = title
        self.duration = duration
        self.adult_mode = adult_mode

    def __str__(self):
        return self.title

    def __repr__(self):
        return self.title


class UrTube:
    users = []
    videos = []
    def __init__(self, current_user = None):
        self.current_user = current_user

    def log_in (self, login, password):
        for user in self.users:
            if login  == User.get_info():
                if hash(password) == User.get_info():
                    self.current_user = user
                    return user

    def register(self,nickname, password,age):
        new_users = User(nickname, password, age)
        if new_users not in self.users:
            self.users.append(new_users)
            self.current_user = new_users
        else:
            print ( "Пользователь уже существует")

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if not video in videos:
                videos.append(video)

    def get_videos(self, search ):
        titles = []
        for video in titles:
            if search.lower() in titles.lower():
                titles.append(video)
                return titles

    def watch_video(self, title):
        if self.current_user is None:
            print("Войдите в аккаунт")
            return

        for video in self.videos:
            if video.title.lower() == title.lower():
                if Video.adult_mode == True and User.age >= 18:
                    while video.time_now < video.duration:
                        video.time_now = video.time_now + 1
                        print(video.time_now)
                        time.sleep(1)
                    video.time_now = 0
                    print("Конец видео")
                else:
                    print("Вам нет 18 лет")
                break
                




# Код для проверки:

ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)



# Добавление видео

ur.add(v1, v2)



# Проверка поиска

print(ur.get_videos('лучший'))

print(ur.get_videos('ПРОГ'))



# Проверка на вход пользователя и возрастное ограничение

ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'lolkekcheburek', 13)

ur.watch_video('Для чего девушкам парень программист?')

ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')



# Проверка входа в другой аккаунт

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)

print(ur.current_user)



# Попытка воспроизведения несуществующего видео

ur.watch_video('Лучший язык программирования 2024 года!')





ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)

ur.watch_video('Для чего девушкам парень программист?')



