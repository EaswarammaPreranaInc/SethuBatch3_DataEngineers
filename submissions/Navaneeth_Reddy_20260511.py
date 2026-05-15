#  Modify  following  program  with  'with'  statement
def   create(f):
	try:
		print('Type  text  terminated  by  ctrl+z')
		while  line :=  input():
				f . write(line + '\n')
	except  EOFError:
		print(F'File  {f . name}  is  created')
#  End  of  the  function
fname = input('Enter  filename :  ')

with open(fname , 'w') as fname :
    create(fname)

'''
output:
Enter  filename :  c.txt
Type  text  terminated  by  ctrl+z
Nava
Chait
Lans
78
^Z
File  c.txt  is  created
'''

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
def   create(f):
	try:
		print('Type  text  terminated  by  ctrl+z')
		while  line :=  input():
				f . write(line + '\n')
	except  EOFError:
		print(F'File  {f . name}  is  created')
#  End  of  the  function
fname = input('Enter  filename :  ')

with open(fname , 'w') as fname :
    create(fname)
