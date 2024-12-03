my_dict = {"Matvey":2018, "Alexander":1987, "Lyda":1968}
print("Dict:",my_dict)
print("Existing value:",my_dict.get("Matvey"))
print("Not existing value:",my_dict.get("Антон"))
my_dict.update({"Artem":2020,"Eva":2017})
delete = my_dict.pop("Eva")
print("Deleted value:",delete)


print("Modified dictionary:",my_dict)
my_set = {1,1,"дом",2,1,6,7,9,"Автомобиль",8,5,6,9,9,89,"дом",47.3,87}
print("Set:",my_set)
my_set.update([99,"Работа",(3,5,7)])
my_set.remove(1)
print("Modified set:", my_set)
