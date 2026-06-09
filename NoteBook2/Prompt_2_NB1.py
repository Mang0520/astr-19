# -*- coding: utf-8 -*-
"""
Created on Sun Apr 19 21:44:42 2026

@author: alope
"""
Intro = "Enter the what opertation youd like to do\n1:Addition\n2:Subtraction\n3:Multiplication\n4:Exit\n: "



unable = "Not a choice\n"

first = "Enter the first value: "

second = "Enter the second value: "

done = "Have a good day."
def Product(x, y):
    a = x * y
    print (f'The value of the product is {a}')
    print (type(a), "\n")

def Sub(x,y):
    a = x - y
    print (f'The difference of {x} and {y} is {a}')
    print (type(a), "\n")
    
def Sum(x, y):
    a = x + y
    print (f'The sum of the {x} and {y} is {a}')
    print (type(a), "\n")

def main():
    while True:
        operation = input(Intro)
        if operation == "1":
            x = float(input(first))
            y = float(input(second))
            Sum(x,y)

        elif operation == "2":
            x = int(input(first))
            y = int(input(second))
            Sub(x,y)
            
        elif operation == "3":
            x = float(input(first))
            y = int(input(second))
            Product(x,y)
    
        elif operation == "4":
            print (done)
            break
        
        else:
            print (unable)
        
    
            
        
    
    
if __name__ == "__main__":
    main()
    