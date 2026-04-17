# -------------------------------
# 1) in and not in operator demo
# -------------------------------


print('green' in 'Hyd is green city') # True
print('day' in 'Sankar dayal sarma') # True
print('Green' in 'Hyd is green city') # False
print('d is' in 'Hyd is green city') # True
print('dis' in 'Hyd is green city') # False
print('iniv' in 'Srinivas') # True
print('iniv' not in 'Srinivas') # False


# in operator → checks if substring exists
# not in operator → checks if substring does not exist




# -------------------------------
# 2) Slice demo program
# -------------------------------


a = "Rama Rao"


print(a[:7:2])
print(a[:7])
print(a[2:4])
print(a[2:])
print(a[:4])
print(a[::2])
print(a[-6:-1])
print(a[-6:])
print(a[:-4:-1])
print(a[-3:-1])
print(a[-3:])
print(a[:])
print(a[::-1])
print(a[::-2])
print(a[-2::-2])
print(a[2:8])
print(a[2:8:-1])
print(a[:-6:-1])
print(a[2:-3])
print(a[1:6:2])
print(a[:-5:-5])
print(a[2:-5])
print(a[2:-5:2])
print(a[:0:-1])
print(a[-5:0:-2])




# -------------------------------------------
# 3) Concatenate two strings after swapping
# -------------------------------------------


h = input("Enter first string: ")
p = input("Enter second string: ")


x = p[:2] + h[2:] + " " + h[:2] + p[2:]


print("Result:", x)




# ----------------------------------------------------
# 4) Print first two and last two characters of string
# ----------------------------------------------------


x = input("Enter any string: ")


if len(x) >= 4:
    print(x[:2] + x[-2:])
else:
    print("")




# ----------------------------------------------------
# 5) Print characters forward and reverse (no slicing)
# ----------------------------------------------------


x = input("Enter the string: ")


for i in range(len(x)):
    print(f"Character at index {i} : {x[i]}")


for i in range(1, len(x)+1):
    print(f"Character at index {-i} : {x[-i]}")




# ----------------------------------------------------
# 6) Separate characters at even and odd indexes
# ----------------------------------------------------


x = input("Enter a string: ")


even = ""
odd = ""


for i in range(len(x)):
    if i % 2 == 0:
        even += x[i]
    else:
        odd += x[i]


print("String at even indexes:", even)
print("String at odd indexes:", odd)




# ----------------------------------------------------
# 7) Character and digit expansion
# Example input: A4B3C2$5
# Output: AAAABBBCC$$$$$
# ----------------------------------------------------


try:
    x = input("Enter string with alternate character and digit: ")
    y = ""


    for i in range(0, len(x), 2):
        y += x[i] * int(x[i+1])


    print("RESULT:", y)


except ValueError:
    print("Invalid input format")




# ----------------------------------------------------
# 8) Merge two strings
# Example: HYD and VAMSI → HVYADMSI
# ----------------------------------------------------


x = input("Enter first string: ")
y = input("Enter second string:")


z = ""
i = 0


while i < len(x) and i < len(y):
    z += x[i] + y[i]
    i += 1


z = z + x[i:] + y[i:]


print("Result:", z)




# ----------------------------------------------------
# 9) Remove duplicate characters
# ----------------------------------------------------


x = input("Enter any string: ")


y = ""


for ch in x:
    if ch not in y:
        y += ch


print("String without duplicates:", y)




# ----------------------------------------------------
# 10) len() function demo
# ----------------------------------------------------


print(len("Hyd"))
print(len("Rama Rao"))
print(len("9247"))
print(len("+-$"))
print(len(""))
print(len(" "))
print(len("A2#"))


# print(len(3456)) → error
# print("Sec".len()) → error




# ----------------------------------------------------
# 11) chr() function demo
# ----------------------------------------------------


print(chr(65))
print(chr(90))
print(chr(97))
print(chr(122))
print(chr(48))
print(chr(57))
print(chr(36))
print(chr(32))




# ----------------------------------------------------
# 12) ord() function demo
# ----------------------------------------------------


print(ord("A"))
print(ord("Z"))
print(ord("a"))
print(ord("z"))
print(ord("0"))
print(ord("9"))
print(ord("$"))
print(ord(" "))




# ----------------------------------------------------
# 13) Character shift program
# Example input: A4M3Z5D2
# Output: AEMPZ_DF
# ----------------------------------------------------


try:
    x = input("Enter string with alternate character and digit: ")


    z = ""


    for i in range(0, len(x), 2):
        z += x[i] + chr(ord(x[i]) + int(x[i+1]))


    print("Result:", z)


except ValueError:
    print("Invalid format")




# ----------------------------------------------------
# 14) Walrus operator demo
# ----------------------------------------------------


a = "Hyd is green city. Hyd is hitec city. Hyd is his cityi"


index = -1


while (index := a.find("is", index + 1)) != -1:
    print(index)


print("End")




# ----------------------------------------------------
# 15) index() method demo
# ----------------------------------------------------


try:
    a = "Hyd is green city. Hyd is hitec city. Hyd is his cityi"


    index = a.index("is")


    while index >= 0:
        print(index)
        index = a.index("is", index + 1)


except:
    print("End")




# ----------------------------------------------------
# 16) rfind() method demo
# ----------------------------------------------------


a = "Hyd is green city. Hyd is hitec city. Hyd is his cityi"


index = a.rfind("is")


while index != -1:
    print(index)
    index = a.rfind("is", 0, index)


print("End")




# ----------------------------------------------------
# 17) rindex() method demo
# ----------------------------------------------------


try:
    a = "Hyd is green city. Hyd is hitec city. Hyd is his cityi"


    index = a.rindex("is")


    while index >= 0:
        print(index)
        index = a.rindex("is", 0, index)


except:
    print("End")




# ----------------------------------------------------
# 18) count() method demo
# ----------------------------------------------------


a = "Hyd is green city. Hyd is hitec city. Hyd is his city"


print(a.count("is"))
print(a.count("is", 19, 48))
print(a.count("was"))




# ----------------------------------------------------
# 19) Count spaces, tabs and new lines
# ----------------------------------------------------


a = "Hyd is\tgreen\ncity.Hyd is\thitec\ncity.Hyd is\this\ncity"


print(a.count(" "))
print(a.count("\t"))
print(a.count("\n"))