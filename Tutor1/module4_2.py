def test_function ():
    def inner_function():
        'Я нахожусь в области видимости функции test_function'
        return inner_function




print (test_function())