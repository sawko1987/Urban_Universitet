
#
def  add_everything_up(a,b):
    """ принимает a и b  которые могут быть как числами(int, float), так и строками(str).
     и складывает их
     """
    try:
        result =  a + b
    except TypeError as exc:
        return str(a)+str(b)
    else:
        return round(result,3)



# Пример кода:
#
print(add_everything_up(123.456, 'строка'))

print(add_everything_up('яблоко', 4215))
#
print(add_everything_up(123.456, 7))
