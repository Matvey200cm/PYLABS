choise = input("all or line\n")
def read_file(file_name, read_mode):
    try:
        with open(file_name, 'r') as file:
            if read_mode == 'all':
                content = file.read()
                print(content)
            elif read_mode == 'line':
                for line in file:
                    print(line.strip())
            else:
                print("Неверный режим чтения. Используйте 'all' или 'line'.")
    except FileNotFoundError:
        print(f"Ошибка: файл {file_name} не найден. Пожалуйста, проверьте путь к файлу.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


read_file('example.txt', choise)  
