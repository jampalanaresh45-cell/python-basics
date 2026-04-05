# def func_name():
#     print("This is function 1")
    
# func_name()

# def mult(a, b, *args, **kwargs):
#     print(f"a={a}, b={b}, args={args}, kwargs={kwargs}")
#     return a * b ## default is none 
    
## a=4, b=5 are keyword arguments, they are passed as a dictionary to the function, and they can be accessed using the keys 'a' and 'b' in the function body.
## '3.0' and 3 are positional arguments, they are passed to the function in the order they are defined, and they can be accessed using the parameter names 'a' and 'b' in the function body.
# res = mult('3.0', 3, 4, 5, c=4, d=5)
# print(res)

"""
when we specify data type in the function definition, it is called type hinting. It is a way to indicate the expected data type of the arguments and the return value of the function. It does not enforce the data type, but it can help with code readability and can be used by static type checkers to catch potential type errors.
"""
# def abc(a:int, b: float) -> float:
#     return a + b
# print(abc(3, 4.5))

def cal(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a % b
    
values = tuple(input("Enter 2 numbers: "))
operator = input("Enter operator to perform:(add, subtract, multiply, divide) ")
print(values)
# res = cal(a, b, operator)
print(map(int, values))