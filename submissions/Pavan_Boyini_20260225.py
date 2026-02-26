{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eec6ad38-ab03-4794-a42b-1392fd207929",
   "metadata": {},
   "outputs": [],
   "source": [
    "#  Write  a  program  to  add ,  subtract , multiply  and  divide  two  complex  numbers\n",
    "\n",
    "c1 = complex(input(\"Enter first complex number  : \"))\n",
    "c2 = complex(input(\"Enter second complex number : \"))\n",
    "\n",
    "print(\"Sum        :\", c1 + c2)\n",
    "print(\"Difference :\", c1 - c2)\n",
    "print(\"Product    :\", c1 * c2)\n",
    "print(\"Division   :\", c1 / c2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "598c99c5-a56a-4fa8-ae73-b6b3b9787e87",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 2\n",
      " 3\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6\n",
      "10\n"
     ]
    }
   ],
   "source": [
    "# Write  a  program  to  determine  area  and  perimeter  of  rectangle\n",
    "\n",
    "l = eval(input())\n",
    "b = eval(input())\n",
    "area = l * b\n",
    "perimeter = 2*(l + b)\n",
    "print(area)\n",
    "print(f' {perimeter}')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "faa683d7-be21-47a2-af61-c2664874f5cf",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      " 3.5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "179.50333333333333 of sphere\n"
     ]
    }
   ],
   "source": [
    "# Write  a  program  to  determine  volume  of  a  sphere\n",
    "r = float(input())\n",
    "pi = 3.14\n",
    "volume = 4 / 3  * (pi *  r ** 3)\n",
    "print(volume ,'of sphere')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "a9418035-ef5a-432b-8e36-d73e29cebb28",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter principle : 10000\n",
      "Enter time : 3\n",
      "Enter rate of interest : 7.5\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "simple_interest : 2250.0\n",
      "compound_interest : 2422.968749999998\n"
     ]
    }
   ],
   "source": [
    "# Write  a  program  to  determine  simple  interest  and  compound  interest\n",
    "\n",
    "p = float(input('Enter principle :'))\n",
    "t = int(input('Enter time :'))\n",
    "r = float(input('Enter rate of interest :'))\n",
    "simple_interest = p*t*r / 100\n",
    "compound_interest = p * (1  +  r  /  100) **  t  -  p\n",
    "print(f'simple_interest : {simple_interest }')\n",
    "print(f'compound_interest : {compound_interest }')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "9fbf7cc6-2636-4b5c-9cf7-2643cb04b383",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter 1st input :  52\n",
      "Enter 2nd input :  36\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Before swap : x = 52  y = 36\n",
      "After swap  : x = 36  y = 52\n"
     ]
    }
   ],
   "source": [
    "# Write  a  program  to  swap  values  of  two   objects   using  3rd  object\n",
    "\n",
    "x = input(\"Enter 1st input : \")\n",
    "y = input(\"Enter 2nd input : \")\n",
    "\n",
    "print(\"Before swap : x =\", x, \" y =\", y)\n",
    "\n",
    "# using third variable\n",
    "temp = x\n",
    "x = y\n",
    "y = temp\n",
    "\n",
    "print(\"After swap  : x =\", x, \" y =\", y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4a0ae69d-1935-4238-a5ca-ffee1c824398",
   "metadata": {},
   "outputs": [],
   "source": [
    "#: Identify  error\n",
    "if  9 > 5 # Here there should a colon\n",
    "\tprint('Hello')  # after that \n",
    "print('Bye')\n",
    "# Identify  error\n",
    "if  9 > 12:\n",
    "\tprint('Hyd')\n",
    "else: # here colon is missing\n",
    "\tprint('Sec')\n",
    " # Identify  error\n",
    "if  (10,20,15):# it is not a condition\n",
    "print('Hyd') # indentation error\n",
    "else:\n",
    "print('Sec') #indentation error\n",
    "# Identify  error\n",
    "if  ():\n",
    "\t\t\tprint('Hyd')  # here indentation error\n",
    "\telse:\n",
    "\t\t\t\t\tprint('Sec')\n",
    "print('Bye')\n",
    " # Identify  error\n",
    "if  { }:\n",
    "{ # in python there is no braces to open a function\n",
    "\tprint('One')\n",
    "\tprint('Two')\n",
    "\tprint('Three')\n",
    "}\n",
    "else:\n",
    "{\n",
    "\tprint('Four')\n",
    "\tprint('Five')\n",
    "\tprint('Six')\n",
    "}\n",
    "print('Bye')\n",
    "# Identify  error\n",
    "if  ():  # Here no condition \n",
    "\tprint('One')\n",
    "\tprint('Two')\n",
    "\tprint('Three')\n",
    "else:\n",
    "if  []:  # indentation error\n",
    "\tprint('Four')\n",
    "\tprint('Five')\n",
    "\tprint('Six')\n",
    "else:\n",
    "if  {}: # # indentation error\n",
    "\tprint('Seven')\n",
    "\tprint('Eight')\n",
    "\tprint('Nine')\n",
    "else:\n",
    "\tprint('Hyd')\n",
    "\tprint('Sec')\n",
    "\tprint('Cyb')\n",
    "print('Bye')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4ee2d023-18a8-45a5-a133-f9b28986838a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object\n",
    "\n",
    "# Hint: One  addition  and  two  subtractions\n",
    "\n",
    "\n",
    "x = int(input(\"Enter x : \"))\n",
    "y = int(input(\"Enter y : \"))\n",
    "\n",
    "print(\"Before swap : x =\", x, \" y =\", y)\n",
    "\n",
    "temp = x\n",
    "x = y\n",
    "y = temp\n",
    "\n",
    "print(\"After swap  : x =\", x, \" y =\", y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "73c34307-ef28-4133-94d3-b3bfa04d6e13",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Write  a  program  to  swap  values  of  two  objects  without  using  3rd  object\n",
    "\n",
    "# Hint: One  multiplication  and  two  divisions\n",
    "\n",
    "x = float(input(\"Enter x : \"))\n",
    "y = float(input(\"Enter y : \"))\n",
    "\n",
    "print(\"Before swap : x =\", x, \" y =\", y)\n",
    "\n",
    "x = x * y\n",
    "y = x / y\n",
    "x = x / y\n",
    "\n",
    "print(\"After swap  : x =\", x, \" y =\", y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "79839093-7e65-422b-95fc-b7dee0ef41e1",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter month number (1-12):  13\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Input should be between 1 and 12\n"
     ]
    }
   ],
   "source": [
    "# Write   a  program  to  print  month  name  for  input  month  number  by  using  if  and  elif \n",
    "\n",
    "try:\n",
    "    num = int(input(\"Enter month number (1-12): \"))\n",
    "\n",
    "    if num < 1 or num > 12:\n",
    "        print(\"Input should be between 1 and 12\")\n",
    "\n",
    "    elif num == 1:\n",
    "        print(\"January\")\n",
    "    elif num == 2:\n",
    "        print(\"February\")\n",
    "    elif num == 3:\n",
    "        print(\"March\")\n",
    "    elif num == 4:\n",
    "        print(\"April\")\n",
    "    elif num == 5:\n",
    "        print(\"May\")\n",
    "    elif num == 6:\n",
    "        print(\"June\")\n",
    "    elif num == 7:\n",
    "        print(\"July\")\n",
    "    elif num == 8:\n",
    "        print(\"August\")\n",
    "    elif num == 9:\n",
    "        print(\"September\")\n",
    "    elif num == 10:\n",
    "        print(\"October\")\n",
    "    elif num == 11:\n",
    "        print(\"November\")\n",
    "    elif num == 12:\n",
    "        print(\"December\")\n",
    "\n",
    "except ValueError:\n",
    "    print(\"Enter numbers only!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "98ba531f-426b-4311-a978-fb130e13b25f",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter a digit (0-9):  10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Invalid\n"
     ]
    }
   ],
   "source": [
    "# Write  a  program  to  print  digit  in  words  with  else  and  if  (do  not  use  elif)\n",
    "''' 0 - Zero\n",
    "1 - One\n",
    "2 - Two\n",
    "....\n",
    "9 - Nine\n",
    "10 - Invalid '''\n",
    "\n",
    "try:\n",
    "    n = int(input(\"Enter a digit (0-9): \"))\n",
    "\n",
    "    if n == 0:\n",
    "        print(\"Zero\")\n",
    "    else:\n",
    "        if n == 1:\n",
    "            print(\"One\")\n",
    "        else:\n",
    "            if n == 2:\n",
    "                print(\"Two\")\n",
    "            else:\n",
    "                if n == 3:\n",
    "                    print(\"Three\")\n",
    "                else:\n",
    "                    if n == 4:\n",
    "                        print(\"Four\")\n",
    "                    else:\n",
    "                        if n == 5:\n",
    "                            print(\"Five\")\n",
    "                        else:\n",
    "                            if n == 6:\n",
    "                                print(\"Six\")\n",
    "                            else:\n",
    "                                if n == 7:\n",
    "                                    print(\"Seven\")\n",
    "                                else:\n",
    "                                    if n == 8:\n",
    "                                        print(\"Eight\")\n",
    "                                    else:\n",
    "                                        if n == 9:\n",
    "                                            print(\"Nine\")\n",
    "                                        else:\n",
    "                                            print(\"Invalid\")\n",
    "\n",
    "except ValueError:\n",
    "    print(\"Enter numbers only\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "1e4e3fd6-a862-4237-abd1-0a58345984ed",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter year:  2025\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Not a Leap Year\n"
     ]
    }
   ],
   "source": [
    "#Write  a  program  to  test  year  is  leap  year  or  not\n",
    "\n",
    "''' 1) What  is  leap  year ?  --->  Divisible  by  4  but  not  by  100   (or)  divisble  by  400\n",
    "\n",
    "2) Are  2016 , 2020 , 2024  leap  years ? --->  Yes  becoz  leap  year  for  every  4  yearrs\n",
    "\n",
    "3) Are  1700 , 1800 , 1900  leap  years ? --->  No  becoz  no  leap  year  for  every  100  years\n",
    "\n",
    "4) Are  1600 , 2000 , 2400  leap  years ?  --->  Yes  becoz  leap  year  for  every  400  years\n",
    "\n",
    "5) Hint:  3  conditions '''\n",
    "\n",
    "try:\n",
    "    year = int(input(\"Enter year: \"))\n",
    "\n",
    "    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):\n",
    "        print(\"Leap Year\")\n",
    "    else:\n",
    "        print(\"Not a Leap Year\")\n",
    "\n",
    "except ValueError:\n",
    "    print(\"Enter numbers only\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "d85276e4-dfa9-4ae6-a60d-d6edc5442ab3",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter first number:  25\n",
      "Enter second number:  3\n",
      "Enter third number:  2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Largest = 25.0\n"
     ]
    }
   ],
   "source": [
    "# Write  a  program  to  determine  largest  of  three  numbers  with  if  and  else\n",
    "\n",
    "# Hint:  Write  multiple  conditions\n",
    "\n",
    "\n",
    "try:\n",
    "    a = float(input(\"Enter first number: \"))\n",
    "    b = float(input(\"Enter second number: \"))\n",
    "    c = float(input(\"Enter third number: \"))\n",
    "\n",
    "    if a >= b and a >= c:\n",
    "        print(\"Largest =\", a)\n",
    "    else:\n",
    "        if b >= a and b >= c:\n",
    "            print(\"Largest =\", b)\n",
    "        else:\n",
    "            print(\"Largest =\", c)\n",
    "\n",
    "except ValueError:\n",
    "    print(\"Enter numbers only\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "65822f7a-350d-45c4-b19a-95623c9a7787",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter 1 for Celsius→Fahrenheit and 2 for Fahrenheit→Celsius:  2\n",
      "Enter Fahrenheit temperature:  25\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Celsius Equivalent : -3.888888888888889\n"
     ]
    }
   ],
   "source": [
    "# Write  a  program  to  convert  celsius  temperature  to  farenheit  and  vice-versa\n",
    "\n",
    "# 1) What  is  the  formula  to  convert  celsius  to  farenheit ? --->  1.8 * temp + 32\n",
    "\n",
    "# 2) What  is  the  formula  to  convert  farenheit  to  celsius ?  --->  (temp - 32) / 1.8\n",
    "\n",
    "try:\n",
    "    choice = int(input(\"Enter 1 for Celsius→Fahrenheit and 2 for Fahrenheit→Celsius: \"))\n",
    "\n",
    "    if choice == 1:\n",
    "        c = float(input(\"Enter Celsius temperature: \"))\n",
    "        f = 1.8 * c + 32\n",
    "        print(\"Fahrenheit Equivalent :\", f)\n",
    "\n",
    "    else:\n",
    "        if choice == 2:\n",
    "            f = float(input(\"Enter Fahrenheit temperature: \"))\n",
    "            c = (f - 32) / 1.8\n",
    "            print(\"Celsius Equivalent :\", c)\n",
    "        else:\n",
    "            print(\"Invalid Choice\")\n",
    "\n",
    "except ValueError:\n",
    "    print(\"Enter valid numbers only\")\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "47e88116-3ef9-4f53-8b23-5fb178a6073b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter value of x co-ordinate :  -2\n",
      "Enter value of y co-ordinate :  6\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "2nd Quadrant\n"
     ]
    }
   ],
   "source": [
    "'''Write  a  program  to  test  a  point  (x , y)  lies  in  1st  quadrant , 2nd  quadrant , 3rd  quadrant ,\n",
    "4th  quadrant , x - axis , y - axis   or  origin\n",
    "\n",
    "1) What  are  the  values  of  x  and  y  in  1st  quadrant ?  --->  Both  are  +ve\n",
    "\n",
    "2) What  are  the  values  of  x  and  y  in  2nd  quadrant ?  --->  'x'  is  -ve  and  'y'  is  +ve\n",
    "\n",
    "3) What  are  the  values  of  x  and  y  in  3rd  quadrant ?  --->  Both   are  -ve\n",
    "\n",
    "4) What  are  the  values  of  x  and  y  in  4th  quadrant ?  --->  'x'  is   +ve  and  'y'  is  -ve\n",
    "\n",
    "5) What  are  the  values  of  x  and  y  on  x - axis ?  ---> 'x'  is  non-zero  and  'y'  is  0\n",
    "\n",
    "6) What  are  the  values  of  x  and  y  on  y - axis ?  --->  'x'  is  0  and  'y'  is  non-zero\n",
    "\n",
    "7) What  are  the  values  of  x  and  y  if  point  is  origin ?  --->  Both  are  zeroes\n",
    "\n",
    "8) Hint:  Use  if  ..   elif '''\n",
    "\n",
    "\n",
    "try:\n",
    "    x = float(input(\"Enter value of x co-ordinate : \"))\n",
    "    y = float(input(\"Enter value of y co-ordinate : \"))\n",
    "\n",
    "    if x > 0 and y > 0:\n",
    "        print(\"1st Quadrant\")\n",
    "\n",
    "    elif x < 0 and y > 0:\n",
    "        print(\"2nd Quadrant\")\n",
    "\n",
    "    elif x < 0 and y < 0:\n",
    "        print(\"3rd Quadrant\")\n",
    "\n",
    "    elif x > 0 and y < 0:\n",
    "        print(\"4th Quadrant\")\n",
    "\n",
    "except ValueError:\n",
    "    print(\"Invalid input\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "02c668ad-0bd8-429e-89f8-5b1a38f4daf6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter first input  :  25\n",
      "Enter second input :  40\n",
      "Enter third input  :  20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Largest input  : 40.0\n",
      "Smallest input : 20.0\n",
      "Middle input   : 25.0\n"
     ]
    }
   ],
   "source": [
    "# Write  a  program  to  determine  largest , smallest  and  middle  of  three  numbers\n",
    "\n",
    "'''a = 10\n",
    "b = 20\n",
    "c = 7\n",
    "max = 20\n",
    "min = 7\n",
    "mid =   (10 + 20 + 7) - (20 + 7) = 10\n",
    "\n",
    "1) What  is  the  initial  value  of  max  ?  --->  a\n",
    "\n",
    "2) Whichever  input >  max,  assign  that  input  to  max\n",
    "\n",
    "3) What  is  the  initial  value  of  min  ?  --->  'a'\n",
    "\n",
    "4) Whichever  input  <  min,  assign  that  input  to  min\n",
    "\n",
    "5) How  to  obtain  middle  number ?  ---> Eliminate  max  and  min  from  a , b , c\n",
    "\n",
    "6) Hint : Do  not  use  else  in  the  program ''' \n",
    "\n",
    "try:\n",
    "    a = float(input(\"Enter first input  : \"))\n",
    "    b = float(input(\"Enter second input : \"))\n",
    "    c = float(input(\"Enter third input  : \"))\n",
    "\n",
    "    # Step 1: Assume first value is max and min\n",
    "    max_val = a\n",
    "    min_val = a\n",
    "\n",
    "    # Step 2: Find maximum\n",
    "    if b > max_val:\n",
    "        max_val = b\n",
    "    if c > max_val:\n",
    "        max_val = c\n",
    "\n",
    "    # Step 3: Find minimum\n",
    "    if b < min_val:\n",
    "        min_val = b\n",
    "    if c < min_val:\n",
    "        min_val = c\n",
    "\n",
    "    # Step 4: Find middle\n",
    "    mid_val = (a + b + c) - (max_val + min_val)\n",
    "\n",
    "    print(\"Largest input  :\", max_val)\n",
    "    print(\"Smallest input :\", min_val)\n",
    "    print(\"Middle input   :\", mid_val)\n",
    "\n",
    "except ValueError:\n",
    "    print(\"Enter valid numbers only\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "87f8e6ba-110a-4f8f-b341-4a286b4877a5",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
