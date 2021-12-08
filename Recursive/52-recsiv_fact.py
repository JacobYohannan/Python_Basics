'''Factorial of a number'''

def factorial(n):
 if n==1: return 1
 else: return n * factorial(n-1)
 
n = int(input('Enter number: '))
print('Factorial of ',n, ' =',factorial(n))

'''
------------------------------------------------------
output
------
Enter number: 5
Factorial of  5  = 120
------------------------------------------------------
'''
