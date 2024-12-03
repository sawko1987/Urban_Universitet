def send_email (message,recipient,*,sender = "university.help@gmail.com"):
    sob = "@" in (recipient or sender)
    ru = ("." + "r" + "u") in (recipient or sender)
    net = ("." + "n" + "e" + "t") in (recipient or sender)
    com = ("." + "c" +"o" + "m") in (recipient or sender)

    if recipient == sender:
        return message, "Нельзя отправить письмо самому себе!"
    elif sob and (ru or net or com):
        return message, f'Письмо успешно отправлено с адреса <{sender} на адрес <{recipient}>.'
    else:
        return message, f'Невозможно отправить письмо с адреса <{sender}> на адрес <{recipient}>'


print(send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com'))
print(send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com'))
print(send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk'))
print(send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru'))




