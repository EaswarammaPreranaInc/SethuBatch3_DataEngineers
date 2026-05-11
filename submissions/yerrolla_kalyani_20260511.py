#  Modify  following  program  with  'with'  statement

#  End  of  the  function
fname = input('Enter  filename :  ')
with open(fname,"w")  as f:
	try:
		print('Type  text  terminated  by  ctrl+z')
		while  line :=  input():
				f . write(line + '\n')
	except  EOFError:
		print(F'File  {f . name}  is  created')

# #
'''
Repeat  prog5c(File-Create)  with  writelines()  method

Inputs
--------
Rama  Rao
9247
+-$
Hyd is green city
ctrl+z

List  --->  ['Rama  Rao\n' , '9247\n' , '+-$\n' , 'Hyd is green city\n']

File
-----
Rama  Rao
9247
+-$
Hyd is  green city
    
    
'''
def  create(f):
		lst=[]
		try:
			print('Enter  text  terminated  by  ctrl + z')
			while line :=  input():
				lst.append(line+'\n')#How  to  read  each  line  from  keyboard  and  write  to  the  list  until  user  strikes  ctrl+z
				f . writelines(lst)#How  to  write  list  to  the  file
		except EOFError:
			print(F'File  {f.name}  is  created')
#  End  of  the  function
fname=input("enter file name :")#How  to  read  the  filename
f=open(fname,"w")#How  to  open  the  file
create(f)#How  to  call  create()  function
f.close()#How  to  close  the  file



'''  (Home  work)
Write  a  program  to  print  data  of  the  file
File
-----
Rama  Rao
9247
+-$
Hyd is green city
1) Which  method  is  used  to  read  data  of  the  file  ?  ---> read()
2) Which  function  is  used  to  print  whole  data  of  the  file ?  --->  print()
3) In  which  mode  is  file  opened ?  --->  read  mode
'''
def  disp(f):
	s=f.read()#How  to  read  the  whole  file
	print(F'Data  of  the  file  {f . name}')
	print(s)#How  to  print  the  file
# End  of  the  function
fname=input("Enter file name:")#How  to  read  the  filename
f=open(fname,"r")#How  to  open  the  file
disp(f)#How  to  call  disp()  function
f.close()#How  to  close  the  file

'''  (Home  work)
Write  a  program  to  print  file  pagewise  and  page  length = 20   lines

File
-----
Rama  Rao
9247
+-$
Hyd is green city


1) Which  method  is  used  to  read  each  line  of  the  file  ?  --->  readline()

2) Which  function  is  used  to  print  each  line ?  ---> print()

3) How  long  is  the  procedure  repeated ?  --->  Until  end  of  the  file  is  reached

4) In  which  mode  is  file  opened ?  --->  read  mode

5) How  to  pause  execution  for  every  20  lines ?  --->  os . system('pause')  where  pause  is  a  dos  command

6) How  to  clear  the  20  lines   before  printing   next  20  lines ?  ---> os . system('cls')  where  cls  is  a  dos  command
'''
import os
def  disp(f):
	count=0
	while True:
		while not count==20:
			s=f.readline()
			print(s)#How  to  print  each  line  of  the  file  and  pause  execution  for  every  20  lines
			count+=1
		os.system("pause")
		os.system("cls")
		count=0
#  End  of  the  function
fname=input("enter file name:")#How  to  read  filename
f=open(fname,"r")#How  to  open  the  file
disp(f)#How  to  call  disp()  function
f.close()#How  to  close  the  file



##above program with using "with" statement.
import os
def  disp(f):
	count=0
	while not "":
		while not count==20:
			s=f.readline()
			print(s)#How  to  print  each  line  of  the  file  and  pause  execution  for  every  20  lines
			count+=1
		os.system("pause")
		os.system("cls")
		count=0
#  End  of  the  function
fname=input("enter file name:")#How  to  read  filename
with open(fname,"r") as f:#How  to  open  the  file
	disp(f)#How  to  call  disp()  function
f.close()#How  to  close  the  file


'''
Repeat  prog9b(File-pagewise)  with  for  loop
i.e.  Print  file  pagewise  and  pause  execution  for  every  20  lines
File
-----
Rama  Rao
9247
+-$
Hyd is green city
1) How  to  iterate  thru  the  file ?  --->  With  for  loop
2) Which  function  is  used  to  print  each  line ?  --->  print()
3) How  long  is  the  procedure  repeated ?  ---> Until  end  of  the  file  is  reached
4) In  which  mode  is  file  opened ?  ---> read  mode
'''
import  os
def  disp(f):
    count = 0
    for x in f:
        print(x,end="")
        count += 1
        if count == 20:
            os.system("pause")
            os.system("cls")
            count = 0
# End  of  the  function
fname=input("Enter file name:")#How  to  read  filename
f=open(fname,"r")#How  to  open  the  file
disp(f)#How  to  call  disp()  function
f.close()#How  to  close  the  file


'''
Write  a  program  to  copy  contents  of  a  file  to  a  different  file

1st  File
---------
Rama  Rao
9247
+-$
Hyd  is  green  city
Eof 

2nd  file
----------
Rama  Rao
9247
+-$
Hyd  is  green  city
1) In  which  mode  is  1st  file  opened ?  ---> 'r'  mode
    In  which  mode  is  2nd  file  opened ?  ---> 'w'   mode

2) What  action  to  be  made  when  1st  file  does  not  exist ?  --->  Print  a  message

3) What  action  to  be  made  when  2nd  file  does  not  exist ?  --->  Copy  1st  file  to  2nd  file

4) What  action  to  be  made  when  both  the  files  are  existing ? --->																
																	Copy  file  when  user  input  is  yes  and  print  a  message  when  user  input  is  no
'''
import os

f1name = input("Enter 1st file : ")
f2name = input("Enter 2nd file : ")

try:
    f1 = open(f1name, "r")
except FileNotFoundError:
    print(f'File {f1name} is not found')
else:
    if os.path.exists(f2name):
        ch = input(f'File {f2name} already exists. Overwrite (yes/no)? ')
        if ch.lower() != 'yes':
            print("File is not overwritten")
            f1.close()
            exit()
    f2 = open(f2name, "w")
    s = f1.read()
    f2.write(s)
    print("File copied successfully")
    f1.close()
    f2.close()

