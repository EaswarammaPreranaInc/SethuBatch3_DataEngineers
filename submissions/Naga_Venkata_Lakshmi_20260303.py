n = int(input('Enter search element: '))
a,b = 0,1
c = a+b
while c <= n:
    if c == n:
        print("Found")
        break;
    a = b
    b = c
    c = a+b
else:
    print("Not found")



try:
    
 n = int(input('Enter any number:  '))
 if  n % 2 == 0:
   print("Even")
 else:
   print("odd")
except :
    print("send an integer input")



from sys import argv

x = int(input('Enter inputs :    ')
  a =[]
  for x in argv[1:]:
     a.append(eval(x))

print(f'Average: {sum(a)/len(a)}')




from sys import argv
try:
x = int(input('Enter inputs :    ')
  a =[]
  for x in argv[1:]:
     a.append(eval(x))

  a = sorted(a) # prints the list in ascending order.
  sorted(a , reverse = True)#prints the list in descending order.
print([a])
except:
  print("Do not send  number and string")











   
 
  