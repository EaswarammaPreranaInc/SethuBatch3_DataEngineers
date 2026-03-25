def f1(x = None,  y = None , z = None):
    if x is None:
        print('No-argument function')
    elif y is None:
        print('Single argument function : ' , x) 
    elif z is None:
        print('Two argument function : ' , x , y) 
    else:
        print('Three argument function : ' , x , y , z) 

f1() 
f1(10)
f1(10 , 20)
f1(10 , 20 , 30) 


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num **0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter any integer number:   "))
print("prime numbers between 2 and n are : ")
for i in range(2 , n+1):
    if is_prime(i):
        print(i , end =' ')
    
