
# Write  a  program  to  print  upper  and  lower  case  alphabets
i=0
for i in range(65+i+1):
    print(chr(64+i+1),end=" ")
    if i==25:
        break
print()    
for i in range(97+i+1):
        print(chr(96+i+1),end=" ")
        if i==25:
            break



#  Write  a  program  to  print  first  'n'  terms  of  fibonacci  series

n = int(input("Enter no-of value: "))
a=0
b=1

if n==0:
     print(a)
else:
    print(a)
    for i in range(n-1):
        
         c=a+b
         a=b
         b=c

         print(a)
         if i==n:
              break
         
# Write  a  program  to  search  for  'x'  in  fibonacci  series
         
n = int(input("Enter int number: "))
a=0
b=1

if n==0:
     print("Found")
elif n==1 or n==2:
    print("Found")

elif n>=3:

    while a<=n:
        
         c=a+b
         a=b
         b=c
         if a==n:
              print("found")
              break
    else:
              
              print("Not found")

else:
     print("Not found")


# Write  a  program  to  search  for  an  element  in  the  list  and  print  index  of  each  elementand  also  number  of  times  it  is  found

a = [10, 20, 15, 12, 18, 15, 19, 14, 15, 14]

key = 15
count = 0

for i in range(len(a)):
    if a[i] == key:
        print(key, "is found at index", i)
        count += 1

print(key, "is found", count, "times")      
       



# Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z(without  walrus  operator)


sum = 0
ctr = 0

try:
    while True:
        x = eval(input("Enter input: "))
        sum = sum + x
        ctr = ctr + 1
except EOFError:
    pass

if ctr != 0:
    avg = sum / ctr
    print("Average =", avg)
else:
    print("No inputs given")