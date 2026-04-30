'''
Write  a  program  to  print  first  'n'  rows  of  emp  table

 emp   table  --------------->   cur  object  --------------->    list   ------------->    tpl   ------------>   monitor
                        execute()                           fetchmany(n)               for  loop                   print()
'''
import mysql.connector
con = mysql.connector.connect("example.db")
cur = con.cursor()
cur.execute("SELECT * FROM emp")
n = int(input("Enter number of rows: "))
rows = cur.fetchmany(n)
for tpl in rows:
    print(tpl)
cur.close()
con.close()



'''
Write  a  program  to  insert  rows  into  emp  table ,  one  at  a  time

1) How  to  call  execute()  method ?  --->															
															cur . execute(F"insert  into  emp  values  ({empno} ,  '{ename}' , {sal})")

2) Are  quotes  mandatory  for  ename ? --->  Yes  becoz  it  is  a  string

3) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  inputs  empno , ename  and  sal

4) cur . execute(F'insert  into  emp  values (25 , "Rama  Rao" , 10000.0)')
    What  is  the  result  of  cur . rowcount ?  ---> 1  becoz  only  one  row  is  inserted  into  emp  table

5) What  happens  when  we  try  to  insert  duplicate  empno ?  --->  Raises  mc . errors . IntegrityError

6) Can  a  tuple  be  inserted  into  MySqlCursor  object ?  --->  No  becoz  it  is  immutable
'''
import mysql.connector
con = mysql.connector.connect("example.db")
cur = con.cursor()
while True:
    try:
        empno = int(input("Enter empno: "))
        ename = input("Enter ename: ")
        sal = float(input("Enter salary: "))
        cur.execute("INSERT INTO emp VALUES (?, ?, ?)", (empno, ename, sal))
        con.commit()
        print("Row inserted successfully")
        print("Rows affected:", cur.rowcount)
    except Exception as e:
        print("Error:", e)
    ch = input("Do you want to insert another row? (yes/no): ")
    if ch.lower() != "yes":
        break
cur.close()
con.close()



'''
Write  a   program  to  delete  rows  of  emp  table  based  on  user  input  condition

1) How  to  call  execute()  method ?  --->  cur . execute(F'delete  from  emp  where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  the  cond
'''
import mysql.connector
con = mysql.connector.connect("example.db")
cur = con.cursor()
while True:
    try:
        empno = int(input("Enter empno to delete: "))
        cur.execute("DELETE FROM emp WHERE empno = ?", (empno,))
        con.commit()
        print("Rows deleted:", cur.rowcount)
    except Exception as e:
        print("Error:", e)
    ch = input("Do you want to delete another row? (yes/no): ")
    if ch.lower() != "yes":
        break
cur.close()
con.close()



'''
Write  a  program to  modify  data  of  emp  table

1) How  to  call  execute()  method ?  --->  cur . execute(F'update  emp  set  {expr}   where  {cond}')

2) What  is  the  pre-requisite  to  call  execute()  method ?  --->  Read  expr  and  cond
'''
import mysql.connector
con = mysql.connector.connect("example.db")
cur = con.cursor()
while True:
    try:
        empno = int(input("Enter empno to update: "))
        new_sal = float(input("Enter new salary: "))
        cur.execute("UPDATE emp SET sal = ? WHERE empno = ?", (new_sal, empno))
        con.commit()
        print("Rows updated:", cur.rowcount)
    except Exception as e:
        print("Error:", e)
    ch = input("Do you want to update another row? (yes/no): ")
    if ch.lower() != "yes":
        break
cur.close()
con.close()



'''
Write  a  program  to  create  student  table

1) How  to  call  execute()  method ?  --->									
								cur . execute(F'create  table  {tablename}(rollno  int  primary  key , sname  char(20) ,  marks  float)')

2) What  is  the  pre-requisite  to  call  execute()  method ?  ---> Read  the  table  name

3) What  action  to  be  made  when  table  already  exists ?  --->																
																	Delete  the  existing  table  and  create  a  new  table  with  same  name
'''
import mysql.connector
con = mysql.connector.connect("example.db")
cur = con.cursor()
tablename = input("Enter table name: ")
try:
    query = f"""
    CREATE TABLE IF NOT EXISTS {tablename} (
        rollno INTEGER PRIMARY KEY,
        sname TEXT,
        marks REAL
    )
    """
    cur.execute(query)
    print("Table created successfully (or already exists).")
except Exception as e:
    print("Error:", e)
finally:
    cur.close()
    con.close()




# parent  and  child  classes  have  different  class  methods
class  parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class  child(parent):
	@classmethod
	def   m2(cls):
		super().m1()	#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1()		#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls.m1()		#How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
		child.m1()		#How  to  call  m1()  method  of  parent  class  in  last  way  without  creating  an  object
		self . m1()  
		m1()
		print('child  Method')
# End  of  the  class
parent.m1()	#How  to  call  m1()  method  of  parent  class
child.m2()	#How  to  call  m2()  method  of  child  class
child . m1()
super() . m1()  
self . m1()




# parent  and  Child  classes  have  same  class   method
class   parent:
	@classmethod
	def   m1(cls):
		print('parent  Method')
class   child(parent):
	@classmethod
	def  m1(cls):
		super().m1()	#How  to  call  m1()  method  of  parent  class  without  creating  an  object
		parent.m1()		#How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
		cls . m1()   
		self . m1()  
		m1() 
		print('child  Method')
# End  of  the  class
parent.m1()		#How  to  call  m1()  method  of  parent  class





# # Parent  and  Child  classes  have  different  static  methods
# class   parent:
# 	@staticmethod
# 	def  m1():
# 		print('parent  method')
# class   child(parent):
# 	@staticmethod
# 	def   m2():
# 		How  to  call  m1()  method  of  parent  class  without  creating  an  object
# 		How  to  call  m1()  method  of  parent  class  in  another  way  without  creating  an  object
# 		How  to  call  m1()  method  of  parent  class  in  one  more  way  without  creating  an  object
# 		super() . m1() 
# 		super(child) . m1() 
# 		self . m1()  
# 		cls . m1()  
# 		print('child  method')
# #end of the class
# How  to  call  m1()  method  of  parent  class
# How  to  call  m2()  method  of  child  class
# child . m1()




# # Parent  and  Child  classes  have  same  static  method
# class   parent:
# 	@staticmethod
# 	def   m1():
# 		print('parent  method')
# class   child(parent):
# 	@staticmethod
# 	def   m1():
# 		How  to  call  m1()  method  of  parent  class  without  creating  an  object
# 		How  to  call  m1()  method  of  parent  class in   another way  without  creating  an  object
# 		super() . m1()  
# 		self . m1()  
# 		cls . m1()   
# 		print('child  method')
# # End  of  the  class
# How  to  call  m1()  method  of  parent  class
# How  to  call  m1()  method  of  child  class




# # Parent  and  child  classes  have   static  variables  with  different  names
# class   parent:
# 	x = 10
# 	def  m1(self):
# 		How  to  print  variable  'x'
# 		How  to  print  variable  'x'  in  another  way  without  creating  an  object
# 		print(x)  
# # End  of  parent  class
# class   child(parent):
# 	y = 20
# 	def  m2(self):
# 		How  to  print  variable  'x'
# 		How  to  print  variable  'x'  in  another  way  without  creating  an  object
# 		How  to  print  variable  'x' in  one  more  way  without  creating  an  object
# 		How  to  print  variable  'x' in  last  way  without  creating  an  object
# 		How  to  print  variable  'y'
# 		How  to  print  variable  'y'  in  another  way  without  creating  an  object
# 		print(super() . y) 
# 		print(y)  
# # End  of child  class
# How  to  call   m1()  method  of  parent  class
# How  to  call   m2()  method  of  child  class





# # Parent  and  Child  classes  have  static  variables  with  same  name
# class   parent:
# 	x = 10
# 	def  m1(self):
# 		How  to  print  variable  'x'  of  parent  class
# 		How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
# class   child(parent):
# 	x = 20
# 	def  m1(self):
# 		How  to  print  variable  'x'  of  parent  class
# 		How  to  print  variable  'x'  of  parent  class  in  another  way  without  creating  an  object
# 		How  to  print  variable  'x'  of  child  class
# 		How  to  print  variable  'x'  of  child  class  in  another  way  without  creating  an  object
# # End  of  the  class
# How  to  call  m1()  method  of  parent  class
# How  to  call  m1()  method  of  child  class




# #  What  are  the  outputs  if  inputs  are  10 , 20 , 30 , 40  , 50 , 60
# class   parent:
# 	def    get(self):
# 		How  to   read  inputs  into   variables  a  and  b  of  object		
# 	def    disp(self):
# 		How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
# # End  of  Parent  class
# class    child(parent):
# 	def    get(self):
# 		How  to   read  inputs  into   variables  a  and  b  of  object
# 		How  to   read  inputs  into   variables  c  and  d  of  object		
# 	def   disp(self):
# 		How  to  print  variables  a  and  b  of  object  in  same  line  separated  by  tab
# 		How  to  print  variables  c  and  d  of  object  in  same  line  separated  by  tab
# 	def  total(self):
# 		return   sum  of  values  in  object  
# # End of child class
# print('parent  object')
# How  to  read  inputs  into  parent  class  object  'p'
# print('child  object')
# How  to  read  inputs  into  child  class  object  'c'
# print('parent  object  :  ' , end = '\t')
# How  to  print  object  'p'
# print()
# print('child  object  :  ' , end = '\t')
# How  to  print  object  'c'
# print('Sum of  the  values  in  child  object :  ' ,  How  to  obtain  sum of  values  of  object  'c')





# '''
# Write  a  program  to  determine  area  and  circumference  of  circle.
# Also  find  area  and  volume  of  cylinder

# 1) What  is  the  area  of  circle ?  ---> 3.14159 * r ^ 2
#     What  is  the  circumference  of  circle ?  --->  2 * 3.14159 * r

# 2) What  is  the  area  of  cylinder ?  --->  2 * 3.14159 * r ^ 2 + 2 * 3.14159 * r * h
#      What  is  the  volume  of  cylinder ?  ---> 3.14159 * r ^ 2 *  h

# 3) Reuse  parent  class  methods  in  child  class  but  do  not  rewrite
# '''
# import  math
# class   circle:
# 	def   get(self):
# 	    How  to  read  radius  into  object
# 	def   area(self):
# 		return  area  of  circle
# 	def   cir(self):
# 		return  circumference  of  circle
# # End  of  circle  class
# class  cylinder(circle):
# 	def   get(self):
# 		How  to  read  radius  into  the  object  
# 		How  to  read  height  into  the  object 
# 	def  area(self):
# 		return  area  of  cylinder
# 	def  volume(self):
# 		return   volume  of  cylinder
# # End of cylinder class
# def    menu():
# 	print('1 . Circle')
# 	print('2 . Cylinder')
# 	print('3 . Exit')
# #end of menu function
# while  True:  
# 	menu()
# 	ch = eval(input('Enter choice : ')) 
# 	match  ch:
# 		case  1:
# 				How  to  read  raidus  into  circle  object
# 				print('Area  :  ' ,  ???)
# 				print('Circumference :  ' ,  ???)
# 		case  2:
# 				How  to  read  raidus  and  height  into  cylinder  object
# 				print('Area : ' ,  ???)
# 				print('Volume :  ' ,  ???)
# 		case  3:
# 				How  to  stop  execution
# 	# End  of  match




# '''
# Write  a  program  to  determine  area  and  perimeter  of  rectangle  and  square.
# Also  find  surface  area  and  volume  of  cube

# 1) What  is  the  area  of  square ?  --->  a ^ 2
#     What  is  the  perimeter  of  square ?  --->  4 *  a

# 2) What  is  the  area  of  rectangle ?  --->  a * b
#     What  is  the  perimeter  of  rectangle ?  ---> 2 * (a + b)

# 3) What  is  the  surface  area  of  cube ? --->  6 * a ^ 2
#      What  is  the  volume  of  cube  ?  --->  a ^ 3

# 4) Reuse  parent  class  methods  in  child   classes  but  do  not  rewrite
# '''
# class   square:
# 	def   get(self):
# 		How  to  read  side  of  square
# 	def   area(self):
# 		return  area  of  square
# 	def   peri(self):
# 		return   perimeter  of  square
# class   rectangle(square):
# 	def   get(self):
# 		How  to  read  length  of  rectangle
# 		How  to  read  breadth  of  rectangle
# 	def   area(self):
# 		 return  area  of  rectangle
# 	def   peri(self):
# 		return   perimeter  of   rectangle
# class   cube(square):
# 	def   get(self):
# 		 How  to  read  side  of  cube
# 	def   area(self):
# 		return  area  of  cube
# 	def   volume(self):
# 		return  volume  of  cube
# def  menu():
# 	print('1 . Square')
# 	print('2 . Rectangle')
# 	print('3 . Cube')
# 	print('4 . Exit')
# # End  of  the  function
# while  True:
# 	menu()
# 	ch = int(input('Enter  choice : ')) 
# 	match   ch:
# 		case   1:
# 			How  to  read  side  into   square  object  's'
# 			print('Area   :  ' ,  ???)
# 			print('Perimeter  :  ' , ???)
# 		case   2:
# 			How  to  read  length  and  breadth  into   rectangle  object  'r'
# 			print('Area  :  ' ,  ???)
# 			print('Perimeter  :  ' ,  ???)
# 		case   3:
# 			How  to  read  side  into  cube  object  'c'
# 			print('Area  :   ' ,  ???)
# 			print('Volume  :  ' ,  ???)
# 		case  4:
# 			How  to  stop  execution





# # Find  outputs
# class  c1:
# 	def  m1(self):
# 		print('m1  method  of  class  c1')
# class  c2:
# 	def  m1(self):
# 		print('m1 method of class c2')
# class  c3:
# 	@classmethod
# 	def  m1(cls):
# 		print('m1 method of  class c3')
# class  c4:
# 	@staticmethod
# 	def  m1():
# 		print('m1 method of  class c4')
# class  c5(c1):
# 	def  m1(self):
# 		print('m1 method of class c5')
# 	def  m2(self):
# 		How  to  call  m1()  method  of  class  c3
# 		How  to  call  m1()  method  of  class  c4
# 		How  to  call  m1()  method  of  class  c2
# 		How  to  call  m1()  method  of  class  c1
# 		How  to  call  m1()  method  of  class  c5
# 		How  to  call  m1()  function
# # End  of  class  c5
# def  m1():
# 	print('m1 function')
# # End  of  the  function
# How  to  call  m2()  method  of  class  c5




# '''
# Write  a  program  to  delete  a  directory.
# Input  is  either  directory  name  (or)  path  of  the  directory
# '''




# '''
# Write  a  program  to  delete  a  group  of  directories
# Input  is  directory  path
# '''




# #  Write  a  program  to  rename  a  file




# # Write  a  program  to  rename  a  directory




# '''
# Write  a  program  to  print  all  the  files  and  sub-directories  of  input  directory
# Input :  Directory  (or)  path
# Output:  Print  Two  lists  where  1st  list  is  all  the  files  and  2nd  list  is  all  the  directories
# '''





# # Write  a  program  to  iterate  thru  sairam  directory  present  in  current  working  directory
