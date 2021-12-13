"""ZeroDivisionError And ValueError"""

try:
  a = int(input("Enter a Integer"))
  b = int(input("Enter another number"))
  c=a/b
except ValueError:
  print("Enter only Integers")
except ZeroDivisionError:
  print("Zero Division Error")
 
"""
---------------------------------------------------------------------------
Output
------
Enter a Integer:6
Enter another number:0
Zero Division Error
"""
