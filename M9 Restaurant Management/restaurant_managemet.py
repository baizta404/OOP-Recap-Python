from abc import ABC,abstractmethod
class User(ABC):
    def  __init__(self,name,email,address):
        self.name = name
        self.email = email
        self.address = address

class Admin(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
    def add_items(self,restaurant,item):
        restaurant.menu.add_to_menu(item)
    def add_employee(self,restaurant,employee):
        restaurant.employees.append(employee)

class Employee(User):
    def __init__(self, name, email, address,designation,salary):
        super().__init__(name, email, address)
        self.designatin = designation
        self.salary = salary


class FoodItem:
    def __init__(self,name,price,quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

class Menu:
    def __init__(self):
        self.menu_items= []
    def add_to_menu(self,item):
        self.menu_items.append(item)
    def view_menu(self):
        print('***** MENU ******')
        print('Item\tPrice\tQuantity')
        for item in self.menu_items:
            print(f'{item.name}\t{item.price}\t{item.quantity}')
    def find_item(self,item_name):
        for item in self.menu_items:
            if item.name.lower() == item_name.lower():
                return item
        return None

class Customer(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)
        self.order = Order()
    def view_menu(self,restaurent):
        restaurent.menu.view_menu()
    def add_item(self,restaurent,item_name,qty):
        item = restaurent.menu.find_item(item_name)
        if item:
            if item.quantity >= qty:
                self.order.add_to_cart(item,qty)
                item.quantity -= qty
                print(f'{qty} piceces {item_name} added')
            else:
                print(f'Etodi to nai re kaga, ache hoilo {item.quantity} da')
                return
        else:
            print(f'Kaga {item_name} nai re')
            return
    def view_order(self):
        print(f'{self.name} here is your order list')
        self.order.view_orders()

    def total_price(self):
        total =  self.order.total_price
        print(f'{self.name} your total bill is {total} tk')
    def clear_cart(self):
        self.order.clear_cart()

class Order:
    def __init__(self):
        self.cart= {}
    def add_to_cart(self,item,quantity):
        if item in self.cart:
            self.cart[item]+= quantity
        else:
            self.cart[item] = quantity
    def view_orders(self):
        print(f'Item\tprice\tQuantity\tItem Total')
        for item,quantity in self.cart.items():
            print(f'{item.name}\t{item.price}\t{quantity}\t{quantity*item.price}')
        print('-----------------'*2)
    @property
    def total_price(self):
        return sum(item.price*quantity for item,quantity in self.cart.items() )
    def clear_cart(self):
        self.cart = {}

class Restaurant:
    def __init__(self,name):
        self.name = name
        self.menu = Menu()
        self.employees = []

mamar_dokan = Restaurant('Mamar Dokan')

admin = Admin('Rahim','admin6251@gamil.com','Nijer Basha')

pizza = FoodItem('Pizza',450,17)
burger = FoodItem('Burger',170,25)
pasta = FoodItem('Pasta',320,7)
sevenUp = FoodItem('7UP',35,24)

emp1 = Employee('Ramim','ramih@mail.com','nakhalpara','Executive',15000)
emp2 = Employee('Mahin','mahin@mail.com','madrashar chatro','Chef',17000)
emp3 = Employee('Shovon','gopal@mail.com','uttara','Waiter',12000)
admin.add_employee(mamar_dokan,emp1)
admin.add_employee(mamar_dokan,emp2)
admin.add_employee(mamar_dokan,emp3)

admin.add_items(mamar_dokan,pizza)
admin.add_items(mamar_dokan,burger)
admin.add_items(mamar_dokan,pasta)
admin.add_items(mamar_dokan,sevenUp)

customer = Customer('Towhid','towhid123@gmail.com','Cumilla,Feni')
customer.view_menu(mamar_dokan)
customer.add_item(mamar_dokan,'pizza',1)
customer.add_item(mamar_dokan,'pasta',2)
customer.add_item(mamar_dokan,'burger',2)
customer.add_item(mamar_dokan,'carew',2)
customer.add_item(mamar_dokan,'7Up',2)
customer.view_order()
customer.total_price()
customer.clear_cart()
customer.view_order()
customer.total_price()
customer2 = Customer('Rashed','Rasehd123@gmail.com','Cumilla,Feni')
customer.view_menu(mamar_dokan)
customer2.view_order()
