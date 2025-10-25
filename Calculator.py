import math
print ("Добро пожаловать в калькулятор! / Welcome to the calculator!")
language = str(input("Выберите язык / Select language \n" \
"Введите Рус / Eng \n" \
"Enter Рус / Eng \n"))

def calc():
    if language == "Рус":
        print("""На данный момент программа может работать только с целыми числами (результат будет округлен до 2 чисел до запятой), которые вам сейчас предстоит ввести""")
        try:
            print ("Введите первое число: ")
            ch1 = int(input().strip())
            print ("Введите второе число: ") 
            ch2 = int(input().strip())
            print("""В данной версии программа может производить сложение, вычитание, умножение, деление, возведение в степень, вычисление корня""")
            print("""Сейчас, когда вы ввели числа, вам предстоит выбрать какое действие будет необходимо выполнить, если вам нужна помощь, введите ? для получения справки""")
        except Exception:
            print ("Введите верное число")
            return True
        act = input().strip()
        if act == "+":
            result1 = ch1 + ch2
            print ("Результат: ", round(result1, 2))
        elif act == "-":
            result2 = ch1 - ch2
            print ("Результат: ", round(result2, 2))
        elif act == "*":
            result3 = ch1 * ch2
            print ("Результат: ", round(result3, 2))
        elif act == "/":
            try:
                result4 = ch1 / ch2
                print ("Результат: ", round(result4, 2))
            except ZeroDivisionError:
                print("Нельзя делить на ноль")
        elif act == "**":
            result5 = ch1 ** ch2
            print ("Результат: ", round(result5, 2))
        elif act == "//":
            try:
                result6 = math.sqrt(ch1)
                result7 = math.sqrt(ch2)
                print ("Результат: ", round(result6, 2),"и", round(result7, 2))
            except ValueError:
                print("Невозможно вывести корень отрицательного числа")
        elif act == "q":
            print ("Завершение программы")
            return False
        elif act == "?":
            print ("""Введите: + для сложения, - для вычитания, * для умножения, / для деления, ** для возведения в степень, // для вычисления квадратного корня обоих чисел, q для выхода""")
        else:
            print("Введено неверное действие, попробуйте еще раз")
            return 
    elif language == "Eng":
        print("""At the moment, the program can only work with integers (the result will be rounded to 2 numbers before the decimal point), which you will now have to enter""")
        try:
            print ("Enter the first number:")
            ch1 = int(input().strip())
            print ("Enter the second number:") 
            ch2 = int(input().strip())
            print("""In this version, the program can perform addition, subtraction, multiplication, division, raising to a power, and root calculations""")
            print("""Now that you have entered the numbers, you will have to choose what action you want to perform. If you need help, enter ? for help.""")
        except Exception:
            print ("Enter the correct number")
            return True
        act = input().strip()
        if act == "+":
            result1 = ch1 + ch2
            print ("Result: ", round(result1, 2))
        elif act == "-":
            result2 = ch1 - ch2
            print ("Result: ", round(result2, 2))
        elif act == "*":
            result3 = ch1 * ch2
            print ("Result: ", round(result3, 2))
        elif act == "/":
            try:
                result4 = ch1 / ch2
                print ("Result: ", round(result4, 2))
            except ZeroDivisionError:
                print("You can't divide by zero")
        elif act == "**":
            result5 = ch1 ** ch2
            print ("Result: ", round(result5, 2))
        elif act == "//":
            try:
                result6 = math.sqrt(ch1)
                result7 = math.sqrt(ch2)
                print ("Result: ", round(result6, 2),"и", round(result7, 2))
            except ValueError:
                print("It is impossible to derive the root of a negative number.")
        elif act == "q":
            print ("Completing the program")
            return False
        elif act == "?":
            print ("""Enter: + for addition, - for subtraction, * for multiplication, / for division, ** for exponentiation, // for calculating the square root of both numbers, q to exit""")
        else:
            print("Invalid action entered, please try again")
            return 
    else:
        print("Неверный язык / Wrong language") 
    return   

running = True
while running:
    running = calc()

print ("Программа завершена. Для начала работы снова введите restart / The program has completed. To start again, enter restart.")
req = input().strip()
if req == "restart":
    language = str(input("Выберите язык / Select language \n" \
"Введите Рус / Eng \n" \
"Enter Рус / Eng"))
    calc()
else: 
    print("Неверная команда / Invalid command")