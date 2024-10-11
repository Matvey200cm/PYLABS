number = int(input("Введите число: "))


if number > 0:
    
    for i in range(1, number + 1):
        print(i)
else:
  
    for i in range(1, number - 1, -1):
        print(i)
