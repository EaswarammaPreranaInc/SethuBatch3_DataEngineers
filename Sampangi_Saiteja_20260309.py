s = input("")
vowels = "AEIOUaeiou"
result = ""
for ch in s:
    if ch in vowels:
        up = ch.upper()
        if up not in result:   
            result += up
print(result)
