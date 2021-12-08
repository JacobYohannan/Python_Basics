'''To remove all strings with length < 5 from a list of strings'''

s=input("Enter the string").split()
b=list( filter( lambda x: len(x)>5, s))
print(b)

'''
----------------------------------------------------
Output
------
Enter the string: apple orange grape pineapple guva

['orange', 'pineapple']
----------------------------------------------------
'''
