'''def arabic_roman(n):
    roman = ""

    data = [
        (1000, "M"), (900, "CM"),
        (500, "D"),  (400, "CD"),
        (100, "C"),  (90, "XC"),
        (50, "L"),   (40, "XL"),
        (10, "X"),   (9, "IX"),
        (5, "V"),    (4, "IV"),
        (1, "I")
    ]

    for value, symbol in data:
        while n >= value:
            roman += symbol
            n -= value

    return roman


n = int(input("Enter arabic number: "))
print("Roman number:", arabic_roman(n))'''


'''
def denom(n):
    a = [500, 200, 100, 50, 20, 10, 5, 2, 1]
    for d in a:
        count = n // d
        if count != 0:
            print(d, "-", count)
        n %= d
n = int(input("Enter any number: "))
denom(n)    
'''


def transpose(a):
    b = []
    for j in range(len(a[0])): 
        row = []
        for i in range(len(a)): 
            row.append(a[i][j])
        b.append(row)
    return b
a = eval(input("Enter nested list: "))
t = transpose(a)      
print("Transpose:")
print(t)


