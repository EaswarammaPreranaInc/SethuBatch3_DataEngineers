'''
Write  a  program  to  print  distinct  vowels  of  the  string  without  using  set

1) Let  input  be   RaMA  rAo
    What  is  the  output ?  ---> AO

2) Hint  1:  Same  as   prog3e  with  minor  changes

3) What  does  'hyd' . upper()  do ? --->  Returns  'HYD'
'''

try:
	s=input('Enter any mixed case string :')
	st =[]
	check='aeiouAEIOU'
	for i in s:
		if( i in check):
			if(i.upper() not in st):
				st.append(i.upper())
	print('Distinct string :',''.join(st) )
except:
	print('Error')

