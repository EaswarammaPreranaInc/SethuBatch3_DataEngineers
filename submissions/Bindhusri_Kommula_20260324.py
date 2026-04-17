# Modify  following  program  such  that  every  function  should  be  executed
def  f1():
	print('No-argument  function')

def  f2(x):
	print('Single  argument  function  : ' , x)


def  f3(x , y):
	print('Two  argument  function : ' , x , y)

def  f4(x , y , z):
	print('Three  argument  function : ' , x , y , z)

f1()
f2(10)
f3(10,20)
f4(10,20,30)



from prog3a import prime
def prime_numbers(n):
    l=[]
    for i in range(2,n+1):
        if prime(i):
             l.append(i)
    return l

n = int(input('Enter  any  integer  number  :  ')) 
res=prime_numbers(n)
print(res)
print(len(res))