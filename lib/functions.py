#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")
    pass
    

def greet(name):
    print(f"Hello, {name}!")
    pass

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")
    pass

def add(num1, num2):
    return num1 + num2
    result = add(45, 55)
    print(result)
    pass

def halve(number):
    return number / 2
    result = halve(100)
    print(result)
    pass
