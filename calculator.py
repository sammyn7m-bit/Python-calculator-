def main():
    print("--- Basic Calculator ---")
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))
        
        if op == "+":
            print(f"Result: {num1} + {num2} = {num1 + num2}")
        elif op == "-":
            print(f"Result: {num1} - {num2} = {num1 - num2}")
        elif op == "*":
            print(f"Result: {num1} * {num2} = {num1 * num2}")
        elif op == "/":
            if num2 == 0:
                print("Error: Math rule exception. Division by zero is undefined.")
            else:
                print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Invalid operator input.")
    except ValueError:
        print("Error: Input strings must be numbers.")

if __name__ == "__main__":
    main()

