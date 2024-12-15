class User:
    users = []
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = int(age)


class Video:
    videos = []
    def __init__(self, title, duration, time_now, adult_mode):
        self.title = title
        self.duration = duration.total_seconds
        self.time_now = time_now
        time_now = 0
        self.adult_mode = adult_mode
        adult_mode = False
        print("class - video")



class UrTube:
    def __init__(self, users, videos, current_user):
        self.users = User.users
        self.videos = Video.videos
        self.current_user = User

    def log_in(self):
        self.nickname = User.nickname
        self.password = User.password
        if self.nickname in User.users:
            if self.password in hash(self.password):
                self.current_user = self.nickname
        else:
            print("Пользователь не найден")

    def register(self):
        self.nickname = User.nickname
        self.password = User.password
        self.age = User.age
        if self.nickname in User.nickname:
            print(f"Пользователь {self.nickname} уже существует")
        else:
            User.users.append(self.nickname, self.password)
        UrTube.log_in()
    def __add__(self,other):
        pass

    def get_video(self):
        self.title = Video.videos
        if s.upper(self) in s.upper(Video.videos):
            return Video.videos








ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)

v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)






