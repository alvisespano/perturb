from abc import ABC, abstractmethod

class Product(ABC):
    def __init__(self, name):
        self.name = name
        self._observers = []  # Lista degli observer registrati
        self._in_stock = False

    def register_observer(self, observer):
        self._observers.append(observer)

    def remove_observer(self, observer):
        self._observers.remove(observer)

    def notify_observers(self):
        for observer in self._observers:
            observer.update(self)

    def set_in_stock(self, in_stock):
        self._in_stock = in_stock
        self.notify_observers()

    def is_in_stock(self):
        return self._in_stock

    def __str__(self):
        return f"Product(name={self.name}, in_stock={self._in_stock})"

# Observer: Interfaccia per ricevere notifiche
class Observer(ABC):
    @abstractmethod
    def update(self, product):
        pass

# Implementazione concreta di Observer
class Customer(Observer):
    def __init__(self, name):
        self.name = name

    def update(self, product):
        if product.is_in_stock():
            print(f"{self.name} has been notified: '{product.name}' is now in stock!")
        else:
            print(f"{self.name} has been notified: '{product.name}' is out of stock.")

def test():
    product = Product("Gaming Laptop")
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    product.register_observer(customer1)
    product.register_observer(customer2)
    print("Changing product status to in stock:")
    product.set_in_stock(True)
    print("\nChanging product status to out of stock:")
    product.set_in_stock(False)
    print("\nRemoving Bob as an observer.")
    product.remove_observer(customer2)
    print("\nChanging product status to in stock again:")
    product.set_in_stock(True)
