# Modify  following  program  such  that  every  function  should  be  executed


def  f1():
	print('No-argument  function')
f1()
def  f1(x):
	print('Single  argument  function  : ' , x)
f1(x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
f1(x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
x=int(input("Enter x value : "))
y=int(input("Enter y value : "))
z=int(input("Enter z value : "))
f1(x , y , z)



#Write  a  program  to  generate  list  of  all   prime  numbers  between  2  and  n   and
#also  print  how  many  prime  numbers  are  existing

def prime(n):
    l=[]
    for i in range(2,n+1):
        for j in range(2,(i//2)+1):
            if i%j==0:
                break
        else:
            l.append(i)
    return l
n=int(input("Enter n value : "))
print(prime(n))
