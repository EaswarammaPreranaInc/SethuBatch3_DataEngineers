# Find outputs  (Home  work)
print( 'green'   in   'Hyd  is  green  city')		#True
print('day'   in   'Sankar  dayal  sarma')		#True
print('Green'   in   'Hyd  is  green  city')		#False
print('d  is'   in   'Hyd  is  green  city')		#True
print('dis'   in   'Hyd  is  green  city')		#False
print('iniv'   in   'Srinivas')				#True
print('iniv'   not   in   'Srinivas')			#False



'''  (Home  work)
Slice  demo  program
0      1       2        3      4       5       6       7
R      a      m        a               R       a       o
-8    -7     -6      -5     -4      -3     -2      -1
'''
a = 'Rama Rao'
print(a [ : 7 : 2]) #a[0:6:2]---> string from indexes 0 to 6 in steps of 2 i.e. Rm<space>a
print(a [ : 7])	    #a[0:7:1]---> string from indexes 0 to 6 in steps of 1 i.e. Rama<space>Rao 
print(a [2 : 4]     #a[2:4:1]---> string from indexes 2 to 3 in steps of 1 i.e. ma
print(a [2 : ])	    #a[2:8:1]---> strinf from indexes 2 to 7 in steps of 1 i.e. ma<space>Rao 
print(a [ : 4 ])    #a[0:4:1]---> string from indexes 0 to 3 in steps of 1 i.e. Rama
print(a [ : : 2])  #a[0:8:2]--->  string  from  indexes  0  to  7  in  steps  of  2  i.e. Rm<space>a
print(a [-6 : -1])  #a[-6:-1:1]---> string from indexes -6 to -2 in steps of -1 i.e. ma<space>Ra 
print(a [-6 : ])     #a[-6:-9:1]---> string from indexes -6 to -8 in steps of -1 i.e. ma<space>Rao
print(a [: -4 : -1]) #a[-1:-4:1]---> string from indexes -1 to -3 in steps of 1 i.e. oaR
print(a [-3 : -1])   #a[-3:-1:1]---> string from indexes -3 to -2 in dsteps of 1 i.e. Ra
print(a [-3 : ])	#a[-3:-9:1]--->string from indexes -3 to-8 in steps of 1 i.e. Rao
print(a [ : : ])	#a[-1:-9:-1]--->string from indexes -1 to-8 in steps of 1 i.e. Rama<space>Rao 
print(a [ : ])		#a[-1:-9:1]--->string from indexes -1 to-8 in steps of 1 i.e.Rama<space>Rao
print(a [ : : -1])	#a[-1:-9:-1]--->string from indexes -1 to-8 in steps of 1 i.e.oaR<space>amaR
print(a [ : : -2])      #a[-1 : -9 : -2]  --->  string  from  indexes  -1  to  -8  in  steps  of  -2  i.e.  oRaa
print(a [ -2 : : -2])	#a[-2:-9:-2]---> string  from  indexes  -2  to  -8  in  steps  of  -2  i.e.  a<space>mR 
print(a [2 : 8])	#a[2:8:1]---> string from indexes 2 to 7 iin steps of 1 i.e. ma<space>Rao
print(a [2 : 8 : -1])	#a[2:8:-1]---> sting from 1 to 7 in steps of -1 i.e. empty string
print(a [ : -6 : -1])	#a[-1:-6:-1]---> string from indexes -1 to -7 in steps of -1 i.e. oaR<space>a
print(a [2 : -3])	#a[2:-3:1]--->string from indexes 2 to -3 in steps of 1 i.e ma 
print(a [1 : 6 : 2])	#a[1:6:2]--->string from indexes 1 to 5 in steps of 2 i.e. aaR
print(a [ : -5 : -5])	#a[-1:-5:-5]--->string from indexes -1 to -4 in steps of -5 i.e. o
print(a [2 : -5])	#a[2:-5:1]--->string from indexes 2 to -4 in steps of 1 i.e. m 
print(a [2 : -5 : 2])	#a[2:-5:2]--->string from indexes 2 to -4 in steps of 2 i.e. m
print(a [ : 0 : -1])	#a[-1:0-1]--->string from indexes -1 to 1 in steps of -1 i.e. 0aR<space>ama
print(a [-5 : 0 : -2])	#a[-5:0:-2]--->string from indexes -5 to 1 in steps of -2 i.e. aa



str_1=input("Enter 1st string: ")
str_2=input("Enter 2nd string: ")
new_str1=str_2[:2]+str_1[2:]
new_str2=str_1[:2]+str_2[2:]
result=new_str1+" "+new_str2
print(f"result: {result}")

         


user_string=input("Enter any string: ")
str_len=len(user_string)
if str_len<4:
    print("")
else:
    first=user_string[:2]
    second=user_string[-2:]
    result=first+second
    print(f"Result: {result}")    
    


text="VAMSI"
n=len(text)
print("string from left to right:")
for i in range(n):
    print(f"character at index {i} : {text[i]}")
print("striing from right to left:")
for i in range(-1,-n-1,-1):
    print(f"character at index {i} : {text[i]}")    
    


n=input("Enter the input: ")
even=[]
odd=[]
for i in range(len(n)):
    if i%2==0:
        even.append(n[i])
    else:
        odd.append(n[i])
print(f"string at even indexes: {even}")        
print(f"string at odd indexes: {odd}")        


s=input("Enter any string with alternate digit and character: ")
output=""
try:
    for i in range(0,len(s),2):
        
        char=s[i]
        count=int(s[i+1])
        output=output+(char*count)   
    print(f"Result: {output}")
except:      
        print("string should have alternate digit and character")



str_1=input("Enter first string: ")
str_2=input("Enter first string: ")
output=""
i=0
while i<len(str_1) and i<len(str_2):
    output=output+str_1[i]+str_2[i]
    i+=1
if i<len(str_1):
   output=output+str_1[i:]
if i<len(str_2):
    output=output+str_2[i:] 
print(f"Result: {output}") 


s=input("Enter the string: ")
output=""
for char in s:
    if char not in output:
        output+=char
    else:
        print("")
print(f"without duplicates: {output}")        



# len()  function  demo  program  (Home  work)
print(len('Hyd'))	#3 
print(len('Rama Rao'))	#8
print(len('9247'))	#4
print(len('+-$'))	#3
print(len(''))		#0
print(len(' '))		#1
print(len('A2#'))	#3
print(len(3456))	#error len() does not work on integers
print('Sec'. len())	#error because str is outside of len() function len('sec')


# chr()  function  demo  program
print(chr(65))	#A
print(chr(90))	#Z			
print(chr(97))	#a
print(chr(122))	#z
print(chr(48))	#0
print(chr(57))	#9
print(chr(36))	#$
print(chr(32))	#' '



'''
What  does  chr()  function  do ?  --->  Converts  unicode  value  to  character
'''
# ord()  function  demo  program
print(ord('A'))	        #65
print(ord('Z'))	        #90	
print(ord('a'))		#97
print(ord('z'))		#122
print(ord('0'))		#48
print(ord('9'))		#57
print(ord('$'))		#36
print(ord(' '))		#32


a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
while  (index := a.find('is')!=-1:
	print(index)
	a = a .[index + 1:]
print('End')


'''  (Home  work)
index()  method  demo  program'''

a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
try:
   index = a .index('is')
   while  True:
	print(index)
	index = a . index('is' , index + 1)
except ValueError:
    print('End')



'''(Home  work)
rfind()  method  demo  program'''
a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
index = a . rfind('is')
print(index)
index = a . find('is' , index + 1)
print('End') 



a = 'Hyd is green city. Hyd is hitec city. Hyd is his cityi'
try:
   index = a . rindex('is')
   print(index)
except ValueError:
    print("substrinf not found")
print('End')


#  count()  method  demo  program (Home  work)
a = 'Hyd is green city. Hyd is hitec city. Hyd is his city'
print(a . count('is'))			#4
print(a . count('is' , 19 , 48))	#3
print(a . count('was'))			#0


#  Find  outputs  (Home  work)
a = 'Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity'
print(a . count(' '))	#3
print(a . count('\t'))	#3
print(a . count('\n'))	#3


