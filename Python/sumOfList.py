#!/usr/bin/python3

def myfun(x):
   result = 0
   for y in x:
      result = result + y
   return result

print (myfun([2, 5, 0, 4]))