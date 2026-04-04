# Recursive Function Example (Demonstrates RecursionError)

def f1():
    a = 3
    if a:
        print(a)  # Always prints 3
        a = a - 1
        f1()      # Recursive call (no base condition!)
        print('Hello')
        print('Hi')
        print(a)
    print('Bye')

# Main execution
a = 3
f1()
print('End')

# Expected Behavior:
# This program will keep printing '3' repeatedly
# until it crashes with:
# RecursionError: maximum recursion depth exceeded
