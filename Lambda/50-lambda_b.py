'''To check the input number is divisible by 5'''

a=int(input("Enter a number:"))
b = lambda x: 'Is' if x%5==0 else 'Is not'
print('{0} {1} divisible by 5'.format(a,b(a)))

'''
-------------------------------------------------
output
------
Enter a number:70

70 Is divisible by 5
--------------------------------------------------
'''
