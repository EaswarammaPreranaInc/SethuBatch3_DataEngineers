def  f1():
		print('f1  Function')
		f2()
def  f2():
		print('f2  function')
f1()

'''
f1 function
f2 function
'''


def   add(a , b):
        return  a + b
#End  of  the  function
print(add(10 , 20))  #  print(30)
print(add('Hyder' , 'abad'))   #Hyderabad
print(add(10.8 , 20.6))        # 31.000  
print(add(True , False))       # 1
print(add(3 + 4j , 5 + 6j))    # 8 +10j
print(add(25 , 10.8))          # 35.8
print(add([25 , 10.8 , 'Hyd'] , [True , None , 3+4j , 'Sec'])) #[25 , 10.8 , 'Hyd',True , None , 3+4j , 'Sec']
#print(add(10 , '20')) #error


def  f1():
	print('No-argument  function')   
def  f1(x):
	print('Single  argument  function  : ' , x)
def  f1(x , y):
	print('Two  argument  function : ' , x , y)
def  f1(x , y , z):
	print('Three  argument  function : ' , x , y , z)
f1(10 , 20 , 30)
#f1(40 , 50)   # error
#f1(60)        #error
#f1()          #error
'''
Three  argument  function : 10,20,30

'''

def prime(n):
	s=n//2
	for i in range(2,s+1):
		if n%i==0:
			return False
	return True
num=int(input("enter number to check"))
print(f'{num} is prime : {prime(num)}')

def numberSystems(num,units):
	a = ["" , "One" , "Two" , "Three" , "Four" , "Five" , "Six" , "Seven" , "Eight" , "Nine" , "Ten" ,   "Eleven" , "Twelve" ,
           "Thirteen" , "Fourteen" , "Fifteen" , "Sixteen" , "Seventeen" ,  "Eightteen" , "Nineteen"]
	b = [""  , "" , "Twenty" , "Thirty" , "Forty" , "Fifty" , "Sixty" , "Seventy" , "Eighty" , "Ninety"]
	res=""
	if num==0:
		return ""
	elif(num<20):
		res+=a[num]+" "
	elif(num>=20):
		res+=b[num//10]+" "
		res+=a[num%10]+" "
	return (res+units)
n=int(input("enter the number"))
if n==0:
	print("Zero")
else:
	crore=numberSystems((num//10000000),"crores")
	lakhs=numberSystems((num//100000)%100," Lakhs")
	thousands=numberSystems((num//1000)%100,"thousand")
	hundreds=numberSystems((num//100)%10,"Hundred")
	tens=numberSystems(num%100," ")
	word=[crore,lakhs,thousands,hundreds,tens]
	print(" ".join(word))

def    f1(a , b , c):
          print(F'a  :  {a}    \t  b  :  {b}  \t  c :  {c}')
# End  of  the  function
f1(a = 10 , b = 20 , c = 30)
f1(25 , 10.8 , 'Hyd')
f1(b = 40.7 , a = 50.2 , c = 60.5)
f1(c = 'Hyd' , b = 'Sec' , a = 'Cyb')
f1(c = 3 + 4j , a = True , b = None)
f1(25 , c = 10.8 , b = 'Hyd')
#f1(a = 100 , 200 , 300)  #   Error
#f1(True , None , b = 'Hyd') error
#f1(10 , 20 , x = 30) # error
#f1(10 , 20) # error

'''
a  :  10          b  :  20        c :  30
a  :  25          b  :  10.8      c :  Hyd
a  :  50.2        b  :  40.7      c :  60.5
a  :  Cyb         b  :  Sec       c :  Hyd
a  :  True        b  :  None      c :  (3+4j)
a  :  25          b  :  Hyd       c :  10.8

'''
