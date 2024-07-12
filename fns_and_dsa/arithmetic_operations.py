def perform_operation(num1, num2, operation):

    match operation:
        case "add": return num1 + num2
        case "subtract": return num1 - num2
        case "multiply": return num1 * num2
        case "devide": 
            if (num1 == 0) or (num2 == 0):
                return "Invalid division"
            else:
                return num1 / num2
            
def main():
    print("Arithmetic Operations")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add, subtract, multiply, divide): ").strip().lower()

    result = perform_operation(num1, num2, operation)
    print(f"Result: {result}")

if __name__ == "__main__":
    main()
