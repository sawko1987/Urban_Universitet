
password = "12Aa123$33%3"
if len(password) <= 8:
    print("Количество символов должно быть минимум 8")
elif  (not "@" in password) or (not "$" in password) or (not "%" in password):
    print("В пароле отсутсвуют спец символы")
elif not ("0" or "1" or "2" or "3" or "4" or"5" or "6" or "7" or "8" or "9") in password:
    print("Введите хотя бы одну цифру")




    # k = []
    # if i == str("!") or i ==str("@") or i==str("%") or i==str("?") or i==str("-"):
    #     k.append(i)
    # if not k:
    #     print("не верный пароль")
    # else:
    #     if
    #
    #
    # elif:
    #     if i.isupper():
    #         print("Пароль успешно принят")
    #         continue
    #
    #     continue
    # else:
    #     print("не корректный пароль")
    #
