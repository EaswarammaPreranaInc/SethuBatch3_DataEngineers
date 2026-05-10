from prog7b import *
while True :
	try:
		s = input("Enter number / string / exit : ")
		data = eval(s)
		a = [data(),data(),data()]
		a[0].get()
		a[1].get()
		a[2].add(a[0],a[1])
		a[2].disp()
	except:
		break
print('Good Bye')

#Write  a  program  to  reverse  a  string  using  stack

from stack import *
inpt = input('Enter any string : ')
s = stack()
for x in inpt:
    s.push(x)
res = ''
while not s.isempty():
    res = res + s.pop()
print('Reverse of the string : ',res)

#Write  a  program  to  perform  parentheses  match

from stack import *
inp = input('Enter parentheses expression : ')
s = stack()
for x in inp:
    if x == '(':
        s.push(x)
    elif x == ')':
        if s.isempty():
            print(f'Invalid : Excess \')\'')
            exit()
        else:
            s.pop()
if s.isempty():
    print('Valid : ( and ) are matching')
else:
    print(f'Invalid :  Excess \'(\'')