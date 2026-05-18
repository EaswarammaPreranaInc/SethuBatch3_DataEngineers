#1
def prefix_to_postfix(prefix_exp):
    stack = []
    operators = set('+-*/^')
    
    for char in reversed(prefix_exp):
        if char in operators:
            op1 = stack.pop()
            op2 = stack.pop()
            temp = op1 + op2 + char
            stack.append(temp)
        else:
            stack.append(char)
    
    return stack[0] if stack else ""

if __name__ == "__main__":
    test_cases = [
        "*-A/BC-/AKL",
        "+AB",
        "*+ABC",
        "+*ABC",
    ]
    
    print("Prefix to Postfix Conversion Program")
    print("=" * 50)
    
    for prefix in test_cases:
        postfix = prefix_to_postfix(prefix)
        print(f"Prefix:  {prefix}")
        print(f"Postfix: {postfix}")
        print("-" * 50)

#2
def f1(arr , target):
	left = 0 
	right = len(arr) - 1
	while left < right: 
		s = arr[left] + arr[right]  
		if s == target: 
			return [left , right] 
		elif s < target:
			left += 1 
		elif s > target: 
			right -= 1 
	return False
a = eval(input('Enter a List : '))  
target = int(input('Enter a Target : ')) 
print(f'Output : {f1(a , target)}')
'''
Output :
Enter a List : [1, 2, 3, 4, 5]
Enter a Target : 5
Output : [0, 3]'''

# longest substring without repeating characters 
def f1(a): 
	left = 0 
	maxlen = 0 
	s = set()
	for i in range(len(a)): 
		while a[i] in s: 
			s.remove(a[left])  
			left += 1 
		s.add(a[i]) 
		maxlen = max(maxlen , i - left + 1) 
	return maxlen
a = input('Enter a String : ') 
print(f'Output : {f1(a)}')
'''
Output :
Enter a String : HelloWorld
Output : 7'''