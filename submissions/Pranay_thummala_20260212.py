
1) int() Function Outputs:

int(10.8)  # 10
int(True)  # 1
int(False)  # 0
int('25')  # 25
int('0075')  # 75
int(0B11010)  # 26
int(0O6247)  # 3239
int(0XA7B9)  # 42937
int(3 + 4j)  # TypeError
int('25.4')  # ValueError
int('Ten')  # ValueError

2) float() Function Outputs:

float(25)  # 25.0
float(True)  # 1.0
float(False)  # 0.0
float('92')  # 92.0
float('36.4')  # 36.4
float('0075')  # 75.0
float(0B1010101)  # 85.0
float(0O6247)  # 3239.0
float(0XA7B9)  # 42937.0
float(3 + 4j)  # TypeError
float('Ten')  # ValueError

3) complex() Function Outputs:

complex(3,4)  # (3+4j)
complex(0,4)  # 4j
complex(3)  # (3+0j)
complex(3.8,4.6)  # (3.8+4.6j)
complex(True,False)  # (1+0j)
complex('3')  # (3+0j)
complex('3.8')  # (3.8+0j)
complex(3,'4')  # TypeError
complex('3',4)  # TypeError
complex('3','4')  # TypeError
complex('Ten')  # ValueError

4) bool() Function Outputs:

bool(0)  # False
bool(10)  # True
bool(-25)  # True
bool(0.0)  # False
bool(0+0j)  # False
bool(10+20j)  # True
bool('False')  # True
bool('')  # False
bool('Hyd')  # True
bool(' ')  # True

5) str() Function Outputs:

str(25)  # '25'
str(10.8)  # '10.8'
str(3+4j)  # '(3+4j)'
str(True)  # 'True'
str(False)  # 'False'
str(None)  # 'None'

6) oct() Function Outputs:

oct(195)  # 0o303
oct(0B10101110010)  # 0o1272
oct(0xA7B9)  # 0o247671

7) hex() Function Outputs:

hex(25)  # 0x19
hex(0B10101111010111)  # 0x2bd7
hex(0O6247)  # 0xcaf
