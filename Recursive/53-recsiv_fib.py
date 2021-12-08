''' Finds nth Fibonacci number '''
def fibo(n):

 if not n: return 0
 if n==1: return 1
 else: return fibo(n-1) + fibo(n-2)
n = int(input('Enter number: '))
print('The term in fibonacci series = ',fibo(n))


'''
------------------------------------------------------
output
------
Enter number: 7
The term in fibonacci series =  13
------------------------------------------------------
'''
