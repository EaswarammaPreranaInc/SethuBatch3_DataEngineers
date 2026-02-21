# Find  outputs
How  to  import   kw  list      # from keyword import kwlist
How  to  print  kwlist  i.e.  [and , or , not , is , in , None , True , False , .....]      #import keyword	# print(keyword.kwlist)
How  to  print  number  of  keywords  i.e.  35       # print(len(keyword.kwlist))
How  to  print  type  of kwlist  i.e.  <class 'list'>        # print(type(keyword.kwlist))
print(keyword . kwlist)    #  ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 
			 	'break', 'class', 'continue', 'def', 'del', 'elif', 'else', 'except', 
 				'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 
 				'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 
 				'try', 'while', 'with', 'yield']



 #  Find  outputs  (Home  work)
How  to  import   keyword  module 	# import keyword module
How  to  print  kwlist 	# print(keyword.kwlist)
How  to  print  number  of  keywords 	# print(len(keyword.kwlist))
How  to  print  type  of kwlist 	# print(type(keyword.kwlist))
print(kwlist) 	# error must be print(keyword.kwlist)


 # How  to  read  complex  input ?
x = complex(input('Enter  complex  number  :  ')) # 3+5j
print(type(x)) # <class 'complex'>
print(x)  # 3+5j


 #  Tricky  program
# Find  outputs  (Home  work)
print(eval("    'hyd'   ")) # hyd
hyd = 'Sec'
print(eval('hyd')) # Sec
sec = '25'
print(eval('sec'))  # 25
print(eval(sec)) # 25
cyb = 10.8
print(eval('cyb')) # 10.8
print(eval(cyb)) # Error float cannot be evaluated


 #  Most  tricky  program
#  Find  output  (Home  work)
print(eval('print("Hyd")')) # Hyd
							# None


#  Find  outputs  (Home  work)
print(bool('False')) # True
print(eval('False')) # False
print(bool('')) # False 
print(eval('  ""  ')) # empty string
print(eval('')) # Error 
print(eval('  " "   ')) # string with one space
print(eval(' ')) # Error


# What  is  the  advantage  of  eval(input()) ? # It automatically converts input into correct datatype.
x = eval(input('Enter  any  input  :  ')) # 3 + 4j
print(type(x)) # <class 'complex'>
print(x)  # 3 + 4j


 # What  is  a  better  approach  to  read  string  input ? # input() because 'keerthi' can be given as string for eval() should be given as ' "keerthi" '
a = input('Enter  any  string  :  ') # "keerthi"
print(len(a)) # 7
print(a) # keerthi
b = eval(input('Enter   any  string  : ')) # "radha" -> ""radha""-> "radha"
print(len(b)) # 5
print(b) # radha
