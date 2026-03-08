print('green' in 'Hyd  is  green  city')
print('day' in 'Sankar  dayal  sarma')
print('Green' in 'Hyd  is  green  city')
print('d  is' in 'Hyd  is  green  city')
print('dis' in 'Hyd  is  green  city')
print('iniv' in 'Srinivas')
print('iniv' not in 'Srinivas')

a = 'Rama Rao'
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
print(a[::])
print(a[:])
print(a[::-1])
print(a[::-2])
print(a[-2::-2])
print(a[2:8])
print(a[2:8:-1])
print(a[:-6:-1])

a = input()
b = input()
c = b[:2] + a[2:] + " " + a[:2] + b[2:]
print(c)

s = input()
if len(s) < 4:
    print("")
else:
    print(s[:2] + s[-2:])

s = input()
for i in range(len(s)):
    print("Character at index", i, ":", s[i])

for i in range(-1, -len(s)-1, -1):
    print("Character at index", i, ":", s[i])
s = input()

print(s[:2] + s[-2:] if len(s) >= 4 else "")

s = input()
i = 0
while i < len(s):
    print("Character at index", i, ":", s[i])
    i += 1
i = -1
while i >= -len(s):
    print("Character at index", i, ":", s[i])
    i -= 1

s = input()
even = ""
odd = ""
for i in range(len(s)):
    if i % 2 == 0:
        even = even + s[i]
    else:
        odd = odd + s[i]
print(even)
print(odd)

a = input()
out = ""
i = 0
while i < len(a):
    out = out + a[i] * int(a[i+1])
    i = i + 2
print(out)

a = input()
b = input()
c = ""
i = 0
while i < len(a) and i < len(b):
    c = c + a[i] + b[i]
    i += 1
c = c + a[i:] + b[i:]
print(c)

s = input()
out = ""
for ch in s:
    if ch not in out:
        out = out + ch
print(out)

print(len('Hyd'))
print(len('Rama Rao'))
print(len('9247'))
print(len('+-$'))
print(len(''))
print(len(' '))
print(len('A2#'))

print(chr(65))
print(chr(90))
print(chr(97))
print(chr(122))
print(chr(48))
print(chr(57))
print(chr(36))
print(chr(32))

print(ord('A'))
print(ord('Z'))
print(ord('a'))
print(ord('z'))
print(ord('0'))
print(ord('9'))
print(ord('$'))
print(ord(' '))