'''
The goal:
Destroy the mountains before your starship collides with one of them. For that, shoot the highest mountain on your path.

Rules:
At the start of each game turn, you are given the height of the 8 mountains from left to right.
By the end of the game turn, you must fire on the highest mountain by outputting its index (from 0 to 7).

Firing on a mountain will only destroy part of it, reducing its height. Your ship descends after each pass.

Victory Conditions
You win if you destroy every mountain

Lose Conditions
Your ship crashes into a mountain
You provide incorrect output or your program times out
'''


# My solution
while True:
    heights=[]
    for i in range(8):
        height= int(input())
        heights.append(height)

    index_with_max_value = [idx for idx in range(len(heights)) if heights[idx] == max(heights)]

    # Basically I just want to print the element inside the list
    # Since the output should type of int and not list
    for i in index_with_max_value:
        result= i
    print(i)


# Solution provided by CodinGame:
import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

# game loop
while 1:
    max = 0
    imax = 0
    for i in range(8):
        mountain_h = int(input()) # represents the height of one mountain, from 9 to 0. Mountain heights are provided from left to right.
        if mountain_h > max:
            max = mountain_h
            imax = i

    print(imax)