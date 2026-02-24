{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "62653a1f-ad6b-4edc-924f-a90472243baa",
   "metadata": {},
   "source": [
    "#### Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.\n",
    "#### Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input\n",
    "\n",
    "##### Hint:  Use  F  string  to  print  results\n",
    "\n",
    "#### Let  inputs  be  10  and  7,\n",
    "#### What  is  the  sum ?  --->  17 \n",
    "#### What  is  the  difference ?  --->  3\n",
    "#### What  is  the  product ?  --->  70\n",
    "#### What  is  the  quotient ?  --->  1.42\n",
    "What  is  the  remainder ?  ---> 3\n",
    "What  is  the  largest  number ?  --->  10\n",
    "What  is  the  smallest  number ?  --->  7\n",
    "What  is  the  sqrt  of  1st  input ?  --->  3.16\n",
    "What  is  the  result  of  power ?  --->  10000000\n",
    "What  is  the  gcd  of  2  numbers ?  --->  1\n",
    "What  is  the  factorial   of  1st  input ?  --->  10!'''\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "af47bec5-e52b-494b-8bc2-d828665dd53d",
   "metadata": {},
   "source": [
    "### Write  a  program  to  determine  sum , difference , product , quotient , largest  and  smallest  of  two  numbers.\n",
    "#### Also  find  remainder,  sqrt  of  first  input , power, gcd  and  factorial  of  first  input\n",
    "\n",
    "##### Hint:  Use  F  string  to  print  results"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "a50107e4-d681-46cf-b9ba-16baeafe9750",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter any integer input: 10\n",
      "Enter any integer input: 2\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "10 + 2 = 12\n",
      "10 - 2 = 8\n",
      "10 * 2 = 20\n",
      "10 / 2 = 5.0\n",
      "10 % 2 = 0\n",
      "max(a,b) = 10\n",
      "min(a,b) = 2\n",
      "sqrt(a) = 3.1622776601683795\n",
      "power(a,b) = 100.0\n",
      "gcd(a,b) = 2\n",
      "fact(a) = 3628800\n"
     ]
    }
   ],
   "source": [
    "import math\n",
    "a = int(input(\"Enter any integer input:\"))\n",
    "b = int(input(\"Enter any integer input:\"))\n",
    "c = a+b\n",
    "#print(a,'+', b,'=', c)\n",
    "d = a - b\n",
    "#print(a,'-',b,'=',d)\n",
    "e = a*b\n",
    "f = a/b\n",
    "g = a%b \n",
    "print(a,'+', b,'=', c)\n",
    "print(a,'-',b,'=',d)\n",
    "print(a,'*',b,'=',e)\n",
    "print(a,'/',b,'=',f)\n",
    "print(a,'%',b,'=',g)\n",
    "print('max(a,b)','=',max(a,b))\n",
    "print('min(a,b)','=',min(a,b))\n",
    "print('sqrt(a)','=',math.sqrt(a))\n",
    "print('power(a,b)','=',math.pow(a,b))\n",
    "print('gcd(a,b)','=',math.gcd(a,b))\n",
    "print('fact(a)','=',math.factorial(a))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a0feb531-eb0f-4afa-8e1c-da706aad94dd",
   "metadata": {},
   "source": [
    "#### Write  a  program  to  determine  largest  of  two  inputs  without  using  max()  function\n",
    "\n",
    "### 1) What  is  the  output  if  inputs  are  10  and  20 ?   --->  20\n",
    "\n",
    " #### 2) What  is   the  output  if  inputs  are  35.8  and  27.9 ?  ---> 35.8\n",
    "\n",
    "#### 3) What  is  the  output  if  inputs  are  'RAMA'  and  'RAJESH' ?  --->  'RAMA'  becoz  'M' > 'J'\n",
    "\n",
    "#### 4) What  is  the  output  if  inputs  are  [10 , 20 , 15 , 18 , 19 , 28]  and  [10 , 20 , 25, 17] ?   --->  [10 , 20 , 25 , 17]  becoz  25 > 15\n",
    "\n",
    "#### 5) Inputs  can  be  integers , floats , strings  and  so  on\n",
    "\n",
    "#### 6) Use   ternary  operator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "8d828b00-7bb8-45ee-9072-af63ee052ffd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter 1st input:   [10 , 20 , 15 , 18 , 19 , 28]\n",
      "Enter 2nd input:   [10 , 20 , 25, 17]\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Largest input:  [10, 20, 25, 17]\n"
     ]
    }
   ],
   "source": [
    "a = eval(input(\"Enter 1st input: \"))\n",
    "b = eval(input(\"Enter 2nd input: \"))\n",
    "Largest = a if a > b else b \n",
    "print('Largest input: ',Largest)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3b6c818c-3de9-4cd0-9c27-b085fe663bd9",
   "metadata": {},
   "source": [
    "#### Write  a  program  to  determine  largest  of  three  inputs  without  using  max()  function\n",
    "\n",
    "#### 1) What  is  the  output  if  inputs  are  10 , 20  and  15 ?   --->  20\n",
    "\n",
    "#### 2) What  is  the  output  if  inputs  are  35.8 , 42.8  and  27.9 ?   ---> 42.8\n",
    "\n",
    "#### 3) What  is  the  output  if  inputs  are  'RAMA'  , 'RAKESH'  and  'RAJESH' ?   --->  'RAMA'\n",
    "\n",
    "#### 4) What  is   the  output  if  inputs  are  [10 , 20 , 15 , 18]  , [10 , 20 , 32, 19]  and  [10 , 20 , 25, 17] ?  --->  [10 , 20 , 32 , 19]\n",
    "\n",
    "#### 5) Inputs  can  be  integers , floats , strings  and  so  on\n",
    "\n",
    "#### 6) Use  nested  ternary  operator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "id": "3b5c407f-396c-4f10-89a3-c53599fe3ffb",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter 1st input:  25\n",
      "Enter 2nd input:  12\n",
      "Enter 2nd input:  10\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Largest input:  25\n"
     ]
    }
   ],
   "source": [
    "a = eval(input(\"Enter 1st input: \"))\n",
    "b = eval(input(\"Enter 2nd input: \"))\n",
    "c = eval(input(\"Enter 3rd input: \"))\n",
    "Largest = a if a > b and a > c else b if b > c else c\n",
    "print('Largest input: ',Largest)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1c753d51-96ba-4b61-b9f4-9b4e7925c033",
   "metadata": {},
   "source": [
    "#### Write  a  program  to  print   '>'  if  1st  input  >  2nd  input,\n",
    "                                              #### '<'  if  1st  input  <  2nd  input  and\n",
    "                                               ####'='  if  inputs  are  same\n",
    "\n",
    "#### 1) What  is  the  result  if  inputs  are  10  and  20 ?  --->  <\n",
    "\n",
    "#### 2) What  is  the  result  if  inputs  are  70  and  60 ?  --->  >\n",
    "\n",
    "#### 3) What  is  the  result  if  inputs  are  25  and  25 ?  ---> =\n",
    "\n",
    "#### 4) Inputs  can  be  integers , floats , strings  and  so  on\n",
    "\n",
    "#### 5) Use  nested  ternary  operator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "5108185d-48bb-47e4-b6cb-8933c64dee06",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter 1st input:  20\n",
      "Enter 2nd input:  20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Result:  =\n"
     ]
    }
   ],
   "source": [
    "a = eval(input(\"Enter 1st input: \"))\n",
    "b = eval(input(\"Enter 2nd input: \"))\n",
    "#c = eval(input(\"Enter 3rd input: \"))\n",
    "Result = '>' if a > b  else '<'  if a<b else '='\n",
    "print('Result: ',Result)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5223156a-b772-4218-85a7-f7b782b47c7f",
   "metadata": {},
   "source": [
    "#### Write  a  program  to  print  1  if  input  is  +ve  ,  -1    if  input  is  -ve  and  0  if  input  is  0\n",
    "\n",
    "#### 1) What  is  the  result  if  input  is  -25 ?  ---> -1\n",
    "\n",
    "#### 2) What  is  the  result  if  input  is  75 ?  ---> 1\n",
    "\n",
    "#### 3) What  is  the  result  if  input  is  0 ?  ---> 0\n",
    "\n",
    "#### 4) Use  nested  ternary  operator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "5172409d-2793-4f42-ba9e-8f5d37b040a6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter 1st input:  0\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Result:  0\n"
     ]
    }
   ],
   "source": [
    "a = eval(input(\"Enter 1st input: \"))\n",
    "#b = eval(input(\"Enter 2nd input: \"))\n",
    "#c = eval(input(\"Enter 3rd input: \"))\n",
    "Result = '+1' if a > 0  else '-1'  if a<0 else '0'\n",
    "print('Result: ',Result)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1dd655c6-59a8-4486-8afc-dee6aa3847be",
   "metadata": {},
   "source": [
    "#### Write  a  program  to  test  input  is  even  number  or  odd  number\n",
    "\n",
    "### 1) What  is  an  even  number  ?  ---> Divisible  by  2\n",
    "\n",
    "#### 2) What  is  an  odd  number  ?  ---> Not  divisible  by  2\n",
    "\n",
    "#### 3) Use  ternary  operator"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "33a31014-ff9f-4bcd-b1cc-5c7873adecf5",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter any number:  20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Even Number\n"
     ]
    }
   ],
   "source": [
    "a = eval(input(\"Enter any number: \"))\n",
    "if a % 2 == 0:\n",
    "    print(\"Even Number\")\n",
    "else:\n",
    "    print('Odd number')\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fbff143b-24c0-434d-acb9-800579e1ab31",
   "metadata": {},
   "source": [
    "### Write  a  program  to  swap  values  of  any  two  objects  in  a  single  statement  without  using  3rd  object\n",
    "\n",
    "### Let  'x'  be  25  and  'y'  be   'Hyd'\n",
    "### What  are  'x'  and  'y'  after  swap ?  --->  Hyd  and  25\n",
    "\n",
    "#### Hint:  Swap  references  but  not  objects"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "41c3c948-98a1-4965-a3f8-b0ebe143f461",
   "metadata": {},
   "outputs": [
    {
     "name": "stdin",
     "output_type": "stream",
     "text": [
      "Enter 1st input:  10\n",
      "Enter 2nd input:  20\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Before swap : a = 20        b =  10\n",
      "After swap : a = 10        b =  20\n"
     ]
    }
   ],
   "source": [
    "a = eval(input(\"Enter 1st input: \"))\n",
    "b = eval(input(\"Enter 2nd input: \"))\n",
    "a,b = b,a\n",
    "print('Before swap :','a =',a,'      ','b = ',b)\n",
    "print('After swap :','a =',b ,'      ', 'b = ',a)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fe27d3d6-5d73-43a1-a69b-40ca436ce07c",
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
