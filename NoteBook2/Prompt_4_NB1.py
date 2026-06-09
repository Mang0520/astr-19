# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 00:18:46 2026

@author: alope
"""

class FavoriteAnimal:
    def __init__(self, arm_length, leg_length, number_eyes, has_tail, is_furry):
        self.arm_length = float(arm_length)
        self.leg_length = float(leg_length)
        self.number_eyes = int(number_eyes)
        self.has_tail = bool(has_tail)
        self.is_furry = bool(is_furry)
        
    def describe(self):
        print("Favorite Animal Description:")
        print(f"Arm length: {self.arm_length}")
        print(f"Leg length: {self.leg_length}")
        print(f"Number of eyes: {self.number_eyes}")
        print(f"Has tail: {self.has_tail}")
        print(f"Is furry: {self.is_furry}")
        

def main():
    animal = FavoriteAnimal(
        arm_length=1.2,
        leg_length=2.5,
        number_eyes=2,
        has_tail=True,
        is_furry=True
    )

    animal.describe()


if __name__ == "__main__":
    main()