# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 11:20:50 2019

@author: Anupama Dhir
"""
    
def add(x, y):
    return x + y

def subtract(x, y):
    return x-y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

def default():
    return ("Incorrect input")

print("Select an operation")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
choice = input("Enter the operation you want to perform: " )
print(choice)
x = int(input("Enter the first number "))
print(x)
y = int(input("Enter the second number "))
print(y)

if choice == '1':
   print(x,"+",y,"=", add(x, y))

elif choice == '2':
   print(x,"-",y,"=", subtract(x, y))

elif choice == '3':
   print(x,"*",y,"=", multiply(x, y))

elif choice == '4':
   print(x,"/",y,"=", divide(x, y))
else:
   print("Invalid input")




