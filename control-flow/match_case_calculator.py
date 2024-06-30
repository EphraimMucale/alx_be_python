num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
operation = str(input("Choose operation (+, -, *, /): "))

match operation:
    case "+":
        print(num1 + num2)
    case "-":
        print(num1 - num2)
    case "*":
        print(num1 * num2)
    case "/":
        if num2 == 0:
           print("You cannot devide by zero")
        else:
            print(num1 / num2)
