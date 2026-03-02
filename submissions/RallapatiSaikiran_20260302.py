


# Find  outputs  (Home  work)
for  i  in  range(1 , 8):           ''' 1 
	print(i)                       Sec              7
	if   i % 3 == 0:               Hello            Sec
		continue                2               Hello
	else:                           Sec             else suite
		print('Sec')            Hello           Outsite loop
	print('Hello')                  3
else:                                   4 
	print('else  suite')            Sec
# End  of  the  loop                    Hello
print('Outside  loop')                  5
                                        Sec
                                        Hello   
                                        6'''    
                                        
                      
           


# Find  outputs  (Home  work)
for  i  in  range(1 , 8):
	print(i)                                    '''1
	if  i == 8:                                    Sec
		break                                  Hello
	else:                                           2
		print('Sec')                            Sec                            
	print('Hello')                                  Hello
else:                                                   3'''
	print('else  suite')
# End  of  the  loop
print('Outside loop')




#  Walrus   operator (:=)  demo  program
print(a := 25)               # 25
print(a = 25)                # Error bcz a is not initialised 
print(a)                      # 25
print(a := 6 + 7)              # 13
print(a)                       # 13
print((a := 6) + 7)            # 13
print(a)                      # 13
print((a = 6) + 7)           # Error bcz of invalid syntax
 


# Find Outputs
a = 0
if  a == 0:
	print('Hyd')      # Hyd
else:
	print('Sec')      # prints nothing
if  b := 0:
	print('Hyd')      # 0
else:
	print('Sec : ' , b)   # Sec : 0
if  c = 0:
	print('Hyd')        # Error
else:
	print('Sec')        # prints nothing




#  del  operator  demo program  (Home  work)
a = 25
print(a)  # 25
del   a   
print(a)   # Error bcz Both reference and object are deleted



# Find  outputs  (Home  work)
a = b = c = 25
print(a , b , c)     # 25 25 25
del   a              # 25 25
print(b , c)         # 25 25
print(a)             # Prints nothing
del   b              
print(c)             # 25
print(b)             # Error
del   c
print(c)            # both reference and object is deleted




#  Can  multiple  objects  be  deleted  with  same  del  operator ?
a , b , c = 25 , 10.8 , 'Hyd'      
print(a , b , c)    # 25 10.8 Hyd
del   a , b , c     # 
print(a)            # Error
print(b)            # Error
print(c)            # Error





# Find outputs  (Home  work)
a = [10 , 20 , 15 , 18]
print(a)       #  [10 20 15 18]
del  a[2]        #  [10 20 18]
print(a)      # [10 20 18]
del  a
print(a)       # Referrence is deleted
print(a[0])    # Error


# Find outputs  (Home work)
a = (10 , 20 , 15 , 18)
print(a)      # (10 20 15 18)
print(a[0])   # 10
del  a[2]     # (10 15 18)
del  a 
print(a)    # Error
print(a[0])  # Error



'''
Write  a  program  to  print  upper  and  lower  case  alphabets'''


 print("Uppercase Alphabets:")
for i in range(65,91):
  print(chr(i), end=' '

print("\n\nLowercase alphabets:")
for i in range (97,123):
  print(chr(i),end=' ')



'''
Write  a  program  to  search  for  'x'  in  fibonacci  series

1) Let  input  be   10
    What  is  the  output ? --->	Not  found

2) Let  input  be   21
    What  is  the  output ? --->  Found

3) Do  not  generate  fibonacci  series
'''

x=int(input("Enter a value:"))
a=0
b=1
while a<=x:
    if a==x:
        Found=True 
        temp=a+b
        a=b
        b=temp
if found:
    print('Found')
else:
    print('not found')           


'''
Write  a  program  to  search  for  an  element  in  the  list  without  using  in  operator  and
print  Found  or  Not  Found  message  (Assume  that  there  are  no  duplicates)

Let  list  be   [10 , 20 , 15 , 12 , 18]'''




def search_element(lst, x):
 for i in range(len(lst)):
    if lst[i]==x:
        print(f'found at index of {i}: ')
        return
        print('not found')    





















































         