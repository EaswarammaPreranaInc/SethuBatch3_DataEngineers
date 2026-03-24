'''
(Home  work)
Write  a  program  to  determine  frequency  of  each  vowel  in  the  string  in  alphabetical  order 
(Ignoring the case)

Let  input  be  RamA    raO
What  is  the  output ?  --->  {'A' : 3 , 'O' : 1}

Hint:  Same  as  prog23a  with  minor  changes
'''
# s = input().upper()
# s=sorted(s)
# print(s)
# freq = {}

# for ch in s:
#     if ch in "AEIOU":
#         freq[ch] = freq.get(ch, 0) + 1
#         print(freq)

# print(dict(sorted(freq.items())))





#  # Find outputs  (Home  work)
# def   f1():
# 	print('Hyd')
# 	print('Sec')
# 	print('Cyb')
# # End  of  the  function
# print('Begin')#Begin
# x = f1() 
# # Hyd
# # Sec
# # Cyb
# print(x)#None
# print(type(x)) #<Class Nonetype>
# print('End') #End


# # Find  outputs  (Home  work)
# def  f1():
# 	return   10 , 20 , 30
# # End  of  the  function
# x = f1()
# print(x) #(10 , 20 , 30)
# print(type(x)) #<Class 'tuple'>
# a , b , c =  f1()   
# print(a)#10
# print(b)#20
# print(c)#30
# print('for  loop') #for loop
# for  k   in   f1():
# 	print(k) # 10 20 30
	

#  # Find  outputs
# def    f1():
# 	return  10
# 	return  20
# 	return  30
# # End  of  the  function
# print('Begin')
# x = f1()  
# print(x)
# # only one return is allowed in a function so only 10 prints
# #begin
# #10
# #End
# print('End')
# return 100 # Error return should be used only inside the function



#  #  Find  outputs
# # f1() #Error as line by line execution and before initialising the function it cannot be called  
# def   f1():
#         print('Hello') 
# print(f1())  #calls function f1 Hello and returns None then prints None  
# print(f1) # prints the type and address of the object


#  # Find  outputs  (Home  work)
# print('Hello') #Hello
# def  f1():
#         print('f1  function')
# #End  of   function
# print('Hi') #Hi
# print(f1()) # f1 function, None
# print(f1) #class type and address of the object
# print('Bye') #Bye


#  #  Find  outputs
# def    f1():
#         print('Hyd')
#         print('Sec')
#         print('Cyb')
# #End  of  the  function
# print('Begin') #Begin
# print(type(f1)) # <Class 'function'>
# print(id(f1))# address of the function 
# print('End')#End