units = int(input('Enter  units :   '))   #   175
match  units // 100:
	case  0:   #   units  between  0  and  99
			cost = units * 3.00
	case  1:  #  units  between  100 and  199
			cost =  100 * 3.00 + (units - 100) * 3.50
	case  2:  # units between  200 and 399
			cost =  100 * 3.00 + (units - 100) * 3.50 + (units - 200) * 4.00
	case  4:  # units between 400 and 699
			cost = 100 * 3.00 + (units - 100) * 3.50 + (units - 200) * 4.00 +(units - 300)*4.50
	case  7: # units between 700			
			cost = 100 * 3.0 +(units -100) *3.50 +(units- 200) *4.0 +(units-300)*4.50+(units-700)*5.00
print('Bill  amount  :  ' , cost)




x = int(input("Enter value of x:  "))

a , b = 0 , 1
i = 0
while i < x:
    print(a)
    a , b = b , a + b
    i += 1


How  to  print  each  element  of  list  [10 , 20 , 15 , 18]  with  for  loop
a = [10 , 20 , 15 , 18]
for x in a:
  print(x)
   
How  to  print  each  character  of   string  'Hyd'  with  for  loop
a = 'Hyd'
for x in a:
    print(x)

How  to  print  each  element  of   range(5)  with  for  loop
for x in range(5):
    print(x)




# Find  outputs  (Home  work)
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . keys():
	print(x) #10
                  30
                  50
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . values():
	print(x)  #20
                   40
                   60
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60} . items():
	print(x) #(10 , 20)
                  (30 , 40)
                  (50 , 60)
print()
for  x  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x) #10
                  30
                  50



# Find outputs  (Home  work)
a = {10 : 20 , 30 : 40 , 50 : 60}
for  x , y  in   a . items():
	print(x , y , sep = '...') #10...20
                                    30...40
                                    50...60
for  x ,  y  in   a:
	print(x , y) # (10 , 20)
                       (30 , 40)
                       (50 , 60)
for  x , y  in  {10 : 20 , 30 : 40 , 50 : 60}:
	print(x , y , sep = '...') #10...20
                                    30...40
                                    50...60



# Identify  error  (Home  work)
for  x  in   123:
        print(x) #Error because for loop iterates the sequences but not non seqences here 123 is integer and stores single element.




# Find  outputs  (Home  work)
for  x   in   ():
        print(x)
for  x   in  []:
        print(x)
for  x   in   {}:
        print(x)
for  x   in   set():
        print(x)
for  x   in   '':
        print(x)
for  x  in  range(10 , 10):
	print(x)
for  x  in   range():
	print(x) #Type Error 
for  x  in   (25):
	print(x) #Error because 25 is integer which is not iterable.



  Nested  Loop  demo  program
for  i  in  range(1 , 4):
	for  j  in  range(1 , 5):
			print(i ,  j)  #1 1
                                        1 2
                                        1 3
                                        1 4
                                        Hello
                                        2 1
                                        2 2
                                        2 3
                                        2 4
                                        Hello
                                        3 1
                                        3 2
                                        3 3
                                        3 4
                                        
                                        
	print('Hello') #Hello
print('Bye') #Bye



a = [25 , 10.8 , 'Hyd' , True]
for i in range(len(a)):
    print(a[i])
  
a = [25 , 10.8 , 'Hyd' , True]
for x in a:
    print(a)


a = [25 , 10.8 , 'Hyd' , True]
for item in reversed(a):
    print(item)


a = eval(input('Enter 1st list :  '))
b = eval(input('Enter 2 nd list:  '))
c = []
for i in range(len(a)):
    c.append(a[i] + b[i])
print('3rd list :' , c)    



a = [25 , 10.8 , 'Hyd' , True , 3 + 4j , None , 'Sec']

for i in range(2,5):
    print(a[i])
    


a = [10 , 20 , 15 , 18]
for  i  in  range(len(a)):
	a[i] +=  1
print('a :  ' , a) #a:  [11 , 21 , 16 , 19]
b = [10 , 20 , 15 , 18]
for  x  in   b:
	x += 1
print('b :  ' ,  b) #[10 , 20 , 15 , 18]



n = int(input('How many lines ?:'   ))
i = 0
for i in range(n):
    print(' ' * (n-i-1),'*' *(2*i+1))




print("First 20 Even numbers")
i = 1 
while i <= 20:
    print(2*i)
    i += 1 
    

print("First 20 odd numbers")
i = 1 
while i<=20:
    print(2*i-1)
    i += 1


n = int(input('Enter value of n:  '))
print("Natural Numbers")
i = 1
while i<=25:
    print(i)
    i += 1



print("Numbers from 10 down to 1 in steps of -1")
i = 10
while i >= 1:
    print(i)
    i -= 1




n = int(input('Enter the number of terms:  '))
sum = 0
for i in range(1, n + 1):
    sum += 1.1*i
    
print('sum:' , sum)    




sum = 0
for i in range(1 , 21):
    sum += 2*i
print(f'sum of first 20 even numbers: {sum}')   



sum = 0
for i in range(1 , 21):
    sum += 2*i-1
print(f'Sum of first 20 odd numbers: {sum}')    



n = int(input('Enter a positive integer:  '))
sum = 0
for i in range(1 , n+1):
    sum += i
print('Sum:' , sum)









# Find  outputs  (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if  i % 3  == 0:
			continue
	else:
			print('Sec')
	print('Hello')
# End of loop
print('Outside loop')    



#0utputs
1
Sec
Hello
2
Sec
Hello
3
4
Sec
Hello
5
Sec
Hello
6
7
Sec
Hello
Outside loop




# Identify Error  (Home  work)
if ():
	print('Hyd')
	continue     #Error syntax error because we use continue statement in for loop and while loop.
	print('Sec')




# Find outputs (Home  work)
for  i   in   range(1 , 8):
	print(i)
	if   i % 3 == 0:
		break
	else:
		print('Sec') #Indendation errors
	print('Hello')
# End  of  the  loop
print('Outside loop') #Outside loop




 Identify Error  (Home  work)
if(10 , 20 , 30):
	print('Hyd')
	break      #Syntax error because break is used in for loop and while loop.
	print('Sec')





















