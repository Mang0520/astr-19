# -*- coding: utf-8 -*-
"""
Created on Tue Apr  7 12:14:28 2026

@author: alope
"""

YAY = "YAY!"
NAH = "Not greater than 27"


def f(x):
    y = x**3 + 8
    return y
    
def main():
    x = 9
    value = f(x)
    print(value)

    if value > 27:
        print(YAY)
    else:
        print(NAH)
    
if __name__ == "__main__":
    main()