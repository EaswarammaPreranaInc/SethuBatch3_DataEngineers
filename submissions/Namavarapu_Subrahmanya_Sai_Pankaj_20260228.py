n = int(input("enter number of lines: "))

for i in range(1, n + 1):
    # printing leading spaces
    print(" " * (n - i), end="")

    ch = 'A'
    for j in range(i):
        print(ch, end=" ")
        ch = chr(ord(ch) + 1)

    print()


# find outputs home work

for i in range(1, 8):
    print(i)
    if i % 3 == 0:
        # pass does nothing here
        pass
        print('Hyd')
    else:
        print('Sec')
    print('Hello')

# expected output for above loop
# 1
# Sec
# Hello
# 2
# Sec
# Hello
# 3
# Hyd
# Hello
# 4
# Sec
# Hello
# 5
# Sec
# Hello
# 6
# Hyd
# Hello
# 7
# Sec
# Hello

# end of the loop
print('Outside loop')

# outside loop


# find outputs home work

for i in range(1, 8):
    print(i)
    if i % 3 == 0:
        # program stops here because of exit
        exit()
    else:
        print('Sec')
    print('Hello')

# expected output
# 1
# Sec
# Hello
# 2
# Sec
# Hello
# 3

# program terminates here because exit is executed

# end of the loop
print('Outside loop')

# outside loop not printed
