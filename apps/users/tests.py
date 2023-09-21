#Калькулятор от Исмара на фукнциях

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "На ноль делить нельзя!"
    return x / y


def calculator(num1, operator, num2):
    if operator == "+":
        return add(num1, num2)
    elif operator == "-":
        return subtract(num1, num2)
    elif operator == "*":
        return multiply(num1, num2)
    elif operator == "/":
        return divide(num1, num2)
    else:
        return "Неподдерживаемая операция"


while True:
    try:
        num1 = float(input("Введите первое число: "))
        operator = input("Введите оператор (+, -, *, /): ")
        num2 = float(input("Введите второе число: "))
        result = calculator(num1, operator, num2)
        print(f"Результат: {result}")
    except ValueError:
        print("Ошибка: Введите корректные числа")
    except KeyboardInterrupt:
        print("\nКалькулятор завершен.")
        break
