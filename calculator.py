import math
import sys

def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def modulo(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot modulo by zero.")
    return a % b

def power(a, b):
    return a ** b

def square_root(a):
    if a < 0:
        raise ValueError("Square root of negative number not allowed.")
    return math.sqrt(a)

def evaluate_expression(expr):
    allowed = {'__builtins__': None}
    return eval(expr, allowed)

def get_number(prompt):
    while True:
        n = input(prompt).strip()
        try:
            return float(n)
        except ValueError:
            print("Invalid number. Try again.")

def main():
    history = []

    menu = """
=== CLI CALCULATOR ===
1) Add
2) Subtract
3) Multiply
4) Divide
5) Modulo
6) Power (a^b)
7) Square Root
8) Expression Evaluator
9) View History
10) Clear History
0) Exit
"""

    while True:
        print(menu)
        choice = input("Choose an option: ").strip()

        if choice == "0":
            print("Goodbye!")
            sys.exit()

        # History options
        if choice == "9":
            if history:
                print("\n--- Calculation History ---")
                for h in history:
                    print(h)
            else:
                print("History is empty.")
            continue

        if choice == "10":
            history.clear()
            print("History cleared.")
            continue

        # Operations
        try:
            if choice in ["1","2","3","4","5","6"]:
                a = get_number("Enter first number: ")
                b = get_number("Enter second number: ")

                ops = {
                    "1": ("+", add),
                    "2": ("-", subtract),
                    "3": ("*", multiply),
                    "4": ("/", divide),
                    "5": ("%", modulo),
                    "6": ("^", power),
                }

                op_symbol, func = ops[choice]
                result = func(a, b)
                output = f"{a} {op_symbol} {b} = {result}"
                print("Result:", result)

            elif choice == "7":
                a = get_number("Enter number: ")
                result = square_root(a)
                output = f"√{a} = {result}"
                print("Result:", result)

            elif choice == "8":
                expr = input("Enter expression (example: 5+7*2/3): ")
                result = evaluate_expression(expr)
                output = f"{expr} = {result}"
                print("Result:", result)

            else:
                print("Invalid choice. Try again.")
                continue

            history.append(output)

        except Exception as e:
            print("Error:", e)

        print("-" * 30)

if __name__ == "__main__":
    main()
