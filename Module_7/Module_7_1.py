from pprint import pprint
class Product:
    def __init__(self, name, weight, category):
        self.name = name
        self.weight = float(weight)
        self.category = category

    def __str__(self):
        return f"{self.name}, {self.weight}, {self.category}"

class Shop():
    __file_name = 'product.txt'

    def get_products(self):
        file = open (self.__file_name, 'r')
        pprint(file.read())
        file.close()
        return file


    def add(self, *products):
        existing_products = self.get_products()
        open (self.__file_name,'a')
        for product in products:
            if product.name in existing_products:
                print(f"Продукт {product.name} уже есть в магазине")
            else:
                existing_products.write(f" {product.name} + '\n'")
                print (f"Продукт {product.name}")





s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')
print(p2) # __str__
s1.add(p1, p2, p3)
print(s1.get_products())
