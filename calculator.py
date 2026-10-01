"""Basic Calculator with execution time tracking."""

import time


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b


OPERATIONS = {
    "1": ("Addition", "+", add),
    "2": ("Subtraction", "-", subtract),
    "3": ("Multiplication", "*", multiply),
    "4": ("Division", "/", divide),
}


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def show_menu():
    print("\n===== Basic Calculator =====")
    for key, (name, symbol, _) in OPERATIONS.items():
        print(f"{key}. {name} ({symbol})")
    print("5. Exit")


def main():
    while True:
        show_menu()
        choice = input("Choose an operation (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in OPERATIONS:
            print("Invalid choice. Please select 1-5.")
            continue

        name, symbol, func = OPERATIONS[choice]
        a = get_number("Enter first number: ")
        b = get_number("Enter second number: ")

        start = time.perf_counter()
        try:
            result = func(a, b)
        except ZeroDivisionError as e:
            print(f"Error: {e}")
            continue
        end = time.perf_counter()

        print(f"\n{name}: {a} {symbol} {b} = {result}")
        print(f"Execution time: {(end - start) * 1000:.6f} ms")


if __name__ == "__main__":
    program_start = time.perf_counter()
    main()
    total = time.perf_counter() - program_start
    print(f"Total program run time: {total:.2f} seconds")
