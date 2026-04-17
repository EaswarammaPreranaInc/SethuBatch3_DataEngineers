units=int(input("Enter units: "))
match units//100 :
    case 0:
        cost=units*3.0
    case 1:
        cost=100*3.0+(units-100)*3.50
    case 2 | 3:
        cost=100*3.0+100*3.5+(units-200)*4.0
    case 4| 5 | 6:
        cost=(100*3.0)+(100*3.5)+(200*4.0)+(units-400)*4.50
    case _:
        cost=(100*3.00)+(100*3.50)+(200*4.00)+(300*4.50)+(units-700)*5.00
print(f"Bill amount : Rs.{cost}") 



x=int(input("Enter the value of x: "))
print("Fibonacci series")
a=0
b=1
count=0
while a < x:
    print(a)
    next_term=a+b
    a=b
    b=next_term
    count+=1


x=int(input("Enter the value of x: "))
print("Fibonacci series")
a=0
b=1
count=0
while a <= x:
    print(a)
    next_num=a+b
    a=b
    b=next_num


# Find  outputs  (Home  work)
numbers=[10,20,15,18]
for x in numbers:
     print(x)
string='Hyd'
for x in string:
   print(x)
for x in range(5):
    print(x)


# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x)      #10\n30\n50
print()            #empty string<space>
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)       #20\n40\n60
print()             #empty string<space>
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x)        #10:20\n30:40\n50:60
print()             #empty string<space>
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x)        #10\n30\n50



a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...')          #10...20\n30...40\n50...60
for  x ,  y  in   a:
	print(x , y                         #error because no parenthesis also cannot unpack the dictionary
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...')          #error cannot unpack the dictionary


# Identify  error  (Home  work)
for  x  in   123:
        print(x)       #error int object is not iterable'''


'''        
# Find  outputs  (Home  work)
for  x   in   ():
        print(x)        #empty tuple
for  x   in  []:
        print(x)        #empty list
for  x   in   {}:
        print(x)        #empty dictionary
for  x   in   set():
        print(x)        #empty set
for  x   in   '':
        print(x)        #empty string
for  x  in  range(10 , 10):
	print(x)
for  x  in   range():
	print(x)               #error expected atleast one element in range function
for  x  in   (25):
	print(x)                #error because int object is not iterable'''
        
       
#  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j) 			#1  1  
	print('Hello')                                  #1  2 --->repeated three times
print('Bye')      #Bye
                                                         #1  3
                                                         #1  4
                                                         #Hello



a=[25,10.8,'Hyd',True]
for i in range(len(a)):
        print(f"index : {i} , Element : {a[i]}")

#for each loop
for item  in enumerate(a):
        print(f"index and element : {item}") 



a=[25,10.8,'Hyd',True]
#indexed based loop
for i in range(len(a)-1,-1):
    print(a[i])
    
#for each loop
a=[25,10.8,'Hyd',True]
for i in reversed(a):
    print(i) 



a=eval(input("Enter 1st list: "))
b=eval(input("Enter 2nd list: "))
c=[]
#using indexed for loop
for i in range(len(a)):
    sum_val=a[i]+b[i]
    c.append(sum_val)
print(f"c : {c}") 
#using for-each loop
index=0
for val_a in a:
    val_b=b[index]
    c.append(val_a+val_b)
    index+=1
print(c)    



a=[25,10.8,'Hyd',True,3+4j,None,'Sec']
for i in range(2,5):
    print(a[i])
for index, value in enumerate(a):
    if 2<=index <=4:
        print(value)    

#  Tricky  program
#  Find  outputs  (Home  work)
a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a)          #[11,21,16,19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b)         #[10,20,15,18]


try:
    n=int(input("How many lines ? : "))
    for i in range(1,n+1):
        spaces=" "*(n-i)
        stars="*"*(2*i-1)
        print(f"{spaces}{stars}")
except :
    print("please enter a numeric value")        


#For even numbers
print("First 20 even numbers")
i=1
while i<=20:
    even_number=2*i
    print(even_number)
    i+=1
print("Bye") 


#For odd numbers
print("First 20 odd numbers")
i=1
while i<=20:
    odd_number=(2*i)-1
    print(odd_number)
    i+=1
print("Bye")


#natural numbers
n=int(input("Enter value of n: "))
print("Natural numbers")
i=1
while i<=n:
    print(i)
    i+=1



#Reverse order
print("numbers from 10 down to 1 in steps of -1")
i=10
while i>=1:
    print(i)
    i-=1


total_sum=0
for i in range(1,21):
    even_number=2*i
    total_sum+=even_number
print(f"sum of first 20 even numbers : {total_sum}")


total_sum=0
for i in range(1,21):
    odd_number=(2*i-1)
    total_sum+=odd_number
print(f"sum of first 20 odd numbers : {total_sum}")    


n=int(input("How many terms would you like to add ? : "))
total_sum=0
for i in range(1,n+1):
    total_sum+=i
print(f"The sum is : {total_sum}")    



# Find  outputs  (Home  work)
for  i   in   range(1 , 8):     #1\nsec\nHello
	print(i)                    #2\nsec\nHello
	if  i % 3  == 0:            #3\nsec\nHello
			continue            #4\nsec\nHello
	else:                       #5\nsec\nHello
			print('Sec')        #6\nsec\nHello
	print('Hello')              #7\nsec\nHello
# End of loop                   #8\nsec\nHello
print('Outside loop')           #outside the loop


# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue
	print('Sec')  		#indentation error


# Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break
	print('Sec')    	#error break statement should only used for loops


# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec')        #1\nsec\nHello
	print('Hello')          #2\nsec\nHello
# End  of  the  loop        #3
print('Outside loop')       #outside the loop


   
       
