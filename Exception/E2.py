

class Abnormal(Exception): pass

try:
        a=int(input("Enter a Number"))
        if a < 90 or a > 120:
         raise Abnormal
        else:
            print("Success")
           
except Abnormal:
        print("Abnormal Value")
        
