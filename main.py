import addition
import subtraction
import multiplication
import division

print('This is an Arithmetic Calculator which can perform basic algebraic operations!')
print('Choose an operation from below: ')
print('1) Addition')
print('2) Subtraction')
print('3) Multiplication')
print('4) Division')
operation = input("Enter choice (1/2/3/4): ")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

def result(a, b):
    if operation == '1':
        return addition.add(a, b)
    elif operation == '2':
        return subtraction.subtract(a, b)
    elif operation == '3':
        return multiplication.multiply(a, b)
    elif operation == '4':
        return division.divide(a, b)
    else:
        return 'Invalid Operation Selected! Try again!!!'
    
print("Result:", result(a, b))