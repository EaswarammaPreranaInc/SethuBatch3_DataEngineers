#1
'''
(Homework)
Write a program to determine frequency of each vowel in the string in alphabetical order (Ignoring the case)

Let input be RamA raO
What is the output? ---> {'A' : 3 , 'O' : 1}
'''
def cv(ipstr):
    vowels = 'AEIOU'
    res = {}
    
    for char in sorted(ipstr.upper()):
        if char in vowels:
            res[char] = res.get(char, 0) + 1
    return res

ipdata = input("Enter a string: ")
output = cv(ipdata)
print(output)


#2
# Find outputs (Homework)
def f1():
    print('Hyd')
    print('Sec')
    print('Cyb')
# End of the function
print('Begin') #Begin
x = f1()
print(x) #Hyd /n Sec /n Cyb /n None
print(type(x)) #class 'NoneType'
print('End') #End



#3
# Find outputs (Homework)
def f1():
    return 10 , 20 , 30
# End of the function
x = f1()
print(x) #(10, 20 , 30)
print(type(x)) #class 'tuple'
a , b , c = f1()   
print(a) #10
print(b) #20
print(c) #30
print('for loop') #for loop
for k in f1():
    print(k) #10 /n 20 /n 30



#4
# Find outputs
def f1():
    return  10
    return  20
    return  30
# End of the function
print('Begin') #Begin
x = f1()  
print(x) #10
print('End') #End
return 100 #Error as return statment can't used outside a function



#5
# Find outputs
f1() #Error as no fucntion f1() is defined above
def f1():
    print('Hello')
print(f1()) #Hello /n None
print(f1) #Hello and hexadecimal address of function f1



#6
# Find outputs (Homework)
print('Hello') #Hello
def f1():
    print('f1  function')
#End of function
print('Hi') #Hi
print(f1()) #fi function /n None
print(f1) #function f1 and hexadecimal address of function f1
print('Bye') #Bye



#7
# Find outputs
def f1():
    print('Hyd')
    print('Sec')
    print('Cyb')
#End of the function
print('Begin') #Begin
print(type(f1)) #class function
print(id(f1)) #Address of the function
print('End') #End