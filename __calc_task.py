def calculator(a,b,operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b
    else:
        return 0

print(calculator(3,7,"add"))
print(calculator(25,4,"subtract"))
print(calculator(8,5,"multiply"))
print(calculator(9,3,"divide"))