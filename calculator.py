import operator

# define the operators
class Calculator:
    OPS ={
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

# check the operator and the division by zero
    def calculate(self,num1, op, num2):
        if op not in self.OPS:
            raise ValueError("Invalid Operator")

        if op == "/" and num2 == 0:
            raise ZeroDivisionError("Division by zero is undefined")

        return self.OPS[op](num1, num2)


def main():
    print("--- Basic Calculator ---")
    calculator = Calculator()

# get user inputs
    while True:
     try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ").strip()
        num2 = float(input("Enter second number: "))

        result = calculator.calculate(num1, op, num2)
        print(f"Result: {num1} {op} {num2} = {result}")

     except ValueError as error:
        print(f"Error: {error}")
     except ZeroDivisionError as error:
        print(f"Error: {error}")


     again = input("Calculate again? (y/n): ").strip().lower()
     if again != "y":
            print("Exiting!")
            break

if __name__ == "__main__":
    main()
