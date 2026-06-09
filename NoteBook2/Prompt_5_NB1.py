# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 14:27:32 2026

@author: alope
"""

import math

def main():
    num_points = 1000
    start = 0.0
    end = 2.0 * math.pi

    print("   x\t\t sin(x)")
    print("-------------------------")

    for i in range(num_points):
        x = start + (end - start) * i / (num_points - 1)
        y = math.sin(x)
        print(f"{x:.6f}\t {y:.6f}")


if __name__ == "__main__":
    main()