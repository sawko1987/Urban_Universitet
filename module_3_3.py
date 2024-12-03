

def print_params(a = 1, b = 'строка', c = True):

    print (a, b, c)
print_params (b = 25)
print_params(c = [1,2,3,])

value_list = (37, "строка 2", True)

values_dict = {"a":55,"b":"Как дела?","c":True}
print_params(*value_list)
print_params(**values_dict)

value_list_2 =[ 5, "строка 3"]
print_params(*value_list_2,42)



