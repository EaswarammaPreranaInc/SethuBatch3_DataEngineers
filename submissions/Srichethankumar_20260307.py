s = input()
first = s[0]
print(first + s[1:].replace(first,'*'))

a = '15:36:48'
print(a.split(':'))
print(a)

a = 'Hyd\nis green\tcity'
print(a.split(' '))
print(a.split())
print(a.split('green'))

a = 'Hyd	is	green	city'
print(a.split('\t'))
print(a.split())
print(a.split(' '))

a = 'Hyd   is   green   city'
print(a.split())
print(a.split(' '))

a = 'www.gmail.com'
print(a.split('.'))

exp = input()
parts = exp.split('+')
s = 0
for x in parts:
    s = s + int(x.strip())
print(s)

a = ['15','36','48']
print(':'.join(a))
b = ('Hyd','is','green','city')
print(' '.join(b))
c = {'10','20','15','25','52'}
print(','.join(c))
d = ['www','gmail','com']
print('.'.join(d))
f = ['Sankar','Dayal','Sarma']
print(''.join(f))

a = 'hyD  iS  grEen  cITy'
print(a.upper())
print(a.lower())
print(a.capitalize())
print(a.title())
print(a.swapcase())
print(a)
print('A7$a'.upper())

a = 'Hyd is green city'
print(a.endswith('city'))
print(a.endswith('town'))
print(a.endswith('green',3,12))
print(a.endswith('green',3,13))
print(a.endswith(' ',3,13))

s = input()
if len(s) < 3:
    print(s)
elif s.endswith('ing'):
    print(s + 'ly')
else:
    print(s + 'ing')

print('Hyd'.isalpha())
print('Rama Rao'.isalpha())
print('Hyd4'.isalpha())
print('Hyd$'.isalpha())
print('9247'.isalpha())
print('+-$'.isalpha())
print('A2#'.isalpha())
print(''.isalpha())
print(' '.isalpha())

print('9247'.isdigit())
print('92a47'.isdigit())
print('92$47'.isdigit())
print('Hyd'.isdigit())
print('+-$'.isdigit())
print('A2#'.isdigit())
print(''.isdigit())
print(' '.isdigit())

print('\n  A\t'.isspace())
print('\n  \t'.isspace())
print('\n  7\t'.isspace())
print('\n'.isspace())
print('\n  $\t'.isspace())
print('\t'.isspace())
print(''.isspace())
print(' '.isspace())

print('hyD'.islower())
print('hyd'.islower())
print('9247'.islower())
print('rama  rao'.islower())
print('+-$'.islower())
print('hyd+-$'.islower())
print('abc123'.islower())
print(''.islower())
print('a2#'.islower())