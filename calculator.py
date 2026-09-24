class Calculator:
    def calculate(self, num1, operator, num2):
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is undefined.")
            return num1 / num2
        else:
            raise ValueError("Invalid operator.")


def main():
    calculator = Calculator()

    print("--- Basic Calculator ---")

    while True:
        try:
            num1 = float(input("Enter first number: "))
            operator = input("Enter operator (+, -, *, /): ").strip()

            if operator not in {"+", "-", "*", "/"}:
                print("Error: Invalid operator.")
                continue

            num2 = float(input("Enter second number: "))

            result = calculator.calculate(num1, operator, num2)
            print(f"Result: {num1} {operator} {num2} = {result}")

        except ValueError:
            print("Error: Please enter valid numbers.")
        except ZeroDivisionError as error:
            print(f"Error: {error}")

        again = input("Calculate again? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
