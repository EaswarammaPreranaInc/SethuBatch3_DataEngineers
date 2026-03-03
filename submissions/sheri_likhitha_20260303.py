'''
Modify  following   program  with  walrus  operator

Hint:  Combine  lines  8   and   9  to a  single  line  with   walrus  operator
'''
try:
	sum =ctr = 0
	while(x:= eval(input('Enter input  (ctrl + z  to  stop)  :  '))) :
		sum += x
		ctr +=1
except  EOFError:
	try:
		print(F'Average :   {sum / ctr}')
	except  ZeroDivisionError:
		print('Enter  at  least  one  input')
except  (NameError , TypeError):
	print('Input  can  not  be  string')



import sys
if len(sys.argv)<2:
    print("pls send an integer input")
else:
    try:
        val=int(sys.argv[1])
        if val%2==0:
            print("even number")
        else:
            print("odd number") 
    except ValueError:
        print("pls send an integer input") 



import sys
argv=sys.argv[1:]
if len(sys.argv)==0:
    print("plse send number inputs")
else:
    try:
        a=[eval(x) for x in argv]
        print(sum (a)/len(a))
    except:
        print("pls send number inputs")


import sys
a=sys.argv[1:]
if len(a)==0:
    print("pls send inputs")
else:
    new_list=[]
    for i in a:
     new_list.append(eval(i)) 
       
     ao=sorted(new_list)
     do=sorted(new_list,reverse=True)
     print(ao)
     print(do)
    try:
       ao=sorted(a)
       do=sorted(a,reverse=True)
       print(ao)
       print(do)
    except:
       print("Do not send number and string")