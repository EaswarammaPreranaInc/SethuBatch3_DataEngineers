a = "Rama Rao"

print(a) #print the value of object A.
print(id(a)) #print id or reference of an object A.
print(type(a)) # class 'Str'

b = 'hyd'
print(b) #print the value of object B.
print(id(b)) #print id or reference of an object.


c = '''Hyderabad is green city.
       Hyderabad is Hi-tech city.
       Hyderabad is beautiful city.'''

print(c) # prints the string values of object C on screen.
print(type(c)) # class 'str'.
print(id(c)) # id or reference of an object C is printed.


a = """Hyd"""
print(a) # prints values of an object A on screen.
print(len(a)) #prints lenght of an object on screen len is a built-ins module which gives counts number of charater of a string and gives length of string.

print(a[0]) # prints H on screen because in python string is indexed and is a sequence. a[0] = H, a[1] = y, a[2] = d.

print("""hyd""")  #prints hyd on screen 

b = """"hyd""" # Here we have extra double quotes.
print(b) # prints "hyd on because if we have double quotes on front it counts as a string and prints on screen.
print(len(b)) # 3 , len prints the number character on screen.


a = 'Hyd'  

'0 1 2'
'h y d'  

print('How to print "H" of object "a"')
print(a[0]) # print H on screen because a[0] is H indexed.

print('how to print "y" of object "a" ')
print(a[1]) # prints Y on screen because a[1] is Y indexed.

print('how to print "d" of object "a" ')
print(a[2]) #prints d on screen because a[2] is D indexed.


#print(a[3]) # a[3] is out of bond because we don't have no character at a[3].


'h   y   d'
'-3  -2  -1'

print('how to print "d" of object "a" ')
print(a[-1]) #prints 'D' on screen because a[-1] is D , we are access using negative index string supports both positive and negative indexing.


print('How to print "Y" of object "a" ')
print(a[-2]) # prints Y on screen we are accessing with negative index a[-2] is Y.
print(a[-3]) #prints "H" on screen , we are accessing with negative index a[-3] is H.
#print(a[-4]) # prints out of bound Error, because we have index a[-4]

'''0  1  2'''
'''h  y  d'''
'''-3 -2 -1'''
print(a[0] == a[-3]) #True because a[0] is and a[-3] is pointing to H that why it's true and we used comparsion operator.

#a[2] = 'c' #Error because str will not to replace 
#print(25[0]) #int 25[0] cannot support to index or get a value  int is not subscriptable.

print('25'[0]) # prints 2 because [0] index value is 2.
#print(True[1]) # bool is not subscriptable
print('True'[1]) # [1] is 'r' str is subscriptable. 


a = 'A'
#print(a[1]) #print no element it gives out bound error because a[1] not value present at index.
print(a[1:]) # prints empty string slicing will not be giving error.


a = 'hyd'
print(a,id(a)) # prints value of object A, and id or reference of an object.
a = a * 3 # hydhydhyd is printed because if we use * operator with a object values it gives or repeats the values.
print(a, id(a)) #prints value of an object A, and id or reference of an object.

print(len('hyd')) #prints length of the string on screen 3.
print(len('Rama Rao')) #prints length of the string on screen 8 even the space is also counted.
print(len('')) #prints 0
print(len(' ')) #prints length 0 because space is counted.
#print(len(689)) #the len() function will not count the int or non string Error int as no length.

a = 'hyd'
print(a*3) # * with a str it repeat the number time that we mention.

print(a*1) # str prints or repeats it no.of times we specific.

print(a*0) # No result 0 times is 0 

print(a*-1) #no result a times -1 is nothing.

print('25' * 3) #prints 252525 on screen, repeats * is used.
#print('25' *4.0)#print error because repeat take only int values to times repeat not float.

print('25'*True) #print once because True is 1 --> 25.



a = 'sankar dayal sarma'

print(a[7:12]) # prints dayal on screen we started at 7 till 12 in step of 1 default but in slicing the 12 is not added means that 12-1 = 11 or y-1. --> dayal


print(a[7:]) # start at 7 go till len(str)-1 in step of one it prints whole string on screen because in indexing it start from 0. --> dayal sarma

print(a[:6]) #start at 0 end at 5 in steps of 1default , --> sankar

print(a[:]) #prints 0 is default if not specified goes till the end length str in steps of 1 default is not specified.
print(a[: : ]) #prints 0 is default if not specified goes till the end length str in steps of 1 default is not specified.
print(a[0: : 2]) # prints 0 to length of str in steps of 2.
print(a[1 : : 2]) #print 1 to end of string in steps of 2.
print(a[-5: -1]) #starts at -5 and till the y+1 is steps of -1 
print(a[-1:-5:-1]) #starts at -1 still -5 in steps of -1.
print(a[: : -2])
print(a[3: -3]) #empty
print(a[2:-5]) #empty because step is positive 
print(a[-1:-5])
