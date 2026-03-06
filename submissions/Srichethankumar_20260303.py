import math
n = int(input("Enter number: "))
def isPerfectSquare(x):
    s = int(math.sqrt(x))
    return s * s == x
if isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4):
    print("Found")
else:
    print("Not found")


import sys
if len(sys.argv) != 2:
    print("Pls send an integer input")
else:
    try:
        num = int(sys.argv[1])
        if num % 2 == 0:
            print("Even number")
        else:
            print("Odd number")    
    except:
        print("Pls send an integer input")

        


import sys
if len(sys.argv) == 1:
    print("Pls send number inputs")
else:
    try:
        a = []
        
        for value in sys.argv[1:]:
            if value == "True":
                a.append(True)
            elif value == "False":
                a.append(False)
            else:
                if "." in value:
                    a.append(float(value))
                else:
                    a.append(int(value))
        total = sum(a)
        count = len(a)
        avg = total / count
        
        print("Average =", avg)
    
    except:
        print("Pls send number inputs")