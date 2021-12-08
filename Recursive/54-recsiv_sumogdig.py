'''Sum of digits'''

def sum(n):

 if n==0:
     return 0
 else: return (n%10) + sum(n//10)

n=int(input("Enter the number"))
print('Sum of elements = ',sum(n))


'''
------------------------------------------------------
output
------
Enter number: 5
Factorial of  5  = 120
------------------------------------------------------
'''
