
name = input("write your name: ")

def greet(name):
    print("hello ", name)
greet(name)    
number = int(input("input number: "))
 
def square(number):
    print(number*number)
square(number)

_number1 = int(input("input first number: "))
_number2 = int(input("input second number: "))

def max_of_two(x, y):
    if x>y:
        print("biggiest ",x)
    else:
        print("biggiest " , y)
max_of_two(_number1, _number2)
