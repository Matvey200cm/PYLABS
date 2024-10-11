def is_prime(number):
    if number < 2:  
        return False
    for i in range(2, int(number**0.5) + 1):  
        if number % i == 0:
            return False  
    return True  


number = int(input("Введите ваше число: "))
if is_prime(number):
    print("Число простое.")
else:
    print("Число не является простым.")
