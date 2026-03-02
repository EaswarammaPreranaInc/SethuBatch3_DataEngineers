'''
Write  a  program  to  print  upper  and  lower  case  alphabets

Hint:
chr(65) =  'A'
chr(90) =  'Z'
chr(97) =  'a'
chr(122) =  'z'
'''
# Printing Upper Case Alphabets (A-Z)
print("Upper Case Alphabets:")
for i in range(65, 91):
    print(chr(i), end=" ")

print("\n") # Just adding a line break for clarity

# Printing Lower Case Alphabets (a-z)
print("Lower Case Alphabets:")
for i in range(97, 123):
    print(chr(i), end=" ")