#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  File: Tower.py

#  Description: Calculates the number of moves it takes to move n discs in a 4 peg
# tower of hanoi

#  Student Name: Gaytri Vasal

#  Course Name: CS 313E 

#  Unique Number: 51120

#  Date Created: 3/7/2022

#  Date Last Modified: 3/8/2022
    
import sys
import math

# Input: n the number of disks
# Output: returns the number of transfers using four needles
def num_moves (n):
    # base case
    if n <= 1:
        return n
    else:
        k = round(n - math.sqrt(2*n + 1) + 1)
        # recurse thorugh k --> access to 4 pegs
        # n-k-1 --> regular tower of hanoi
        return 2*num_moves(k) + 2**(n-k-1) + 2**(n-k-1) - 1

def main():
  # read number of disks and print number of moves
  for line in sys.stdin:
    line = line.strip()
    num_disks = int (line)
    print (num_moves (num_disks))

if __name__ == "__main__":
  main()

