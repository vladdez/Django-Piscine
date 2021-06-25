#!/usr/bin/env python3


class HotBeverage:
    def __init__(self, name = 'hot beverage', price = '0.30'):
        self.price = price
        self.name = name
    
    def __str__(self):
        a = "name: " + self.name + "\n"
        b = "price: " + self.price + "\n"
        c = "description: " + str(self.description()) 
        res = a + b + c
        return res

    def description(self):
        return "Just some hot water in a cup."

class Coffee(HotBeverage):
    def __init__(self):
        HotBeverage.__init__(self, "coffee",  '0.40')
    def description(self):
        return "A coffee, to stay awake."

class Tea(HotBeverage):
    def __init__(self):
        HotBeverage.__init__(self, "tea",  '0.40')

class Chocolate(HotBeverage):
    def __init__(self):
        HotBeverage.__init__(self, "chocolate",  '0.50')
    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(HotBeverage):
    def __init__(self):
        HotBeverage.__init__(self, "cappuccino",  '0.45')
    def description(self):
        return "“Un po’ di Italia nella sua tazza!"

if __name__ == '__main__':
    hb = HotBeverage()
    print(hb)
    coffee = Coffee()
    print(coffee)
    tea = Tea()
    print(tea)
    chocolate = Chocolate()
    print(chocolate)
    cappuccino = Cappuccino()
    print(cappuccino)