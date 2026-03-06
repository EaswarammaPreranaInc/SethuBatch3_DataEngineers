
# write a program to search for x in Finonacci series
try:
    x=int(input('Enter the value: '))
    a=0
    b=1
    if x<0:
        print('Enter +ve integer')
    if x==0 or x==1 or x==2:
        print('found')

    if x>=3:
        while a<=x:
            c=a+b
            a=b
            b=c
            if x==a:
                print("Found")
                break
        else:
            print("Not found")

except ValueError :
    print("Enter only +ve integer")


#   Write  a  program to  determine  average  of  inputs  which  are  terminated  with  ctrl + z(with  walrus  operator)
try:

    sum=ctr=0
    while (x:=eval(input("enter input(ctrl+z is stop): "))):
        sum +=x
        ctr +=1
except EOFError:
    if ctr!=0:
        print("Avarage= ",(sum/ctr))
    else:
        print("no input given")

except NameError:
    print("Enter input should not be string") 


# use argv function input is even or odd
from sys import argv

if len(argv) >=2:
    print("Please enter only one integer")
else:
    try:
        a =int(sys.argv[1])
       
        if a % 2 == 0:
             print("Even number")
        else:
            print("Odd number")
    except ValueError:
        print("Enter only integer value")

    except NameError:
        print('Enter input should not be a string')

# 