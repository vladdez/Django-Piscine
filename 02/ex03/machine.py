#!/usr/bin/env python3

from random import randint
from beverages import *

class CoffeeMachine:
    def __init__(self):
        self.served = 0

    class EmptyCup(HotBeverage):
        def __init__(self):
            HotBeverage.__init__(self, "empty cup",  '0.40')
        def description(self):
            return "An empty cup?! Gimme my money back!"
   
    class BrokenMachineException(Exception):
        def __init__(self):
            Exception__init__("This coffee machine has to be repaired.")

    def repair(self):
        self.served = 0
    
    def serve(self, param):
        if (self.served == 10):
            return CoffeeMachine.BrokenMachineException
        if (randint(0, 1) == 1):
            self.served += 1
            return param.description()
        else:
            return self.EmptyCup().description()

if __name__ == '__main__':
    machine = CoffeeMachine()
    coffee = Coffee()
    tea = Tea()
    chocolate = Chocolate()
    cappuccino = Cappuccino()
    for i in range(30):
        try:
            a = machine.serve(tea)
            print(a)
        except Exception:
            print(Exception)
    print("<...repairing...>")
    print("___Chuh-Chuh!!!___")
    machine.repair()
    for i in range(25):
        try:
            a = machine.serve(chocolate)
            print(a)
        except Exception:
            print(Exception)