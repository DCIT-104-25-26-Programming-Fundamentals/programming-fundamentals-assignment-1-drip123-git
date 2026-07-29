def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    """Return a / b rounded to 2 decimal places, or None if b is zero."""
    if b == 0:
        return None
    return round(a / b, 2)


def modulus(a, b):
    """Return a % b, or None if b is zero."""
    if b == 0:
        return None
    return a % b


def power(a, b):
    return a ** b


def show_menu():
    """Display the calculator menu."""
    print("============================")
    print("     SIMPLE CALCULATOR")
    print("============================")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exponentiation")
    print("7. Quit")


def get_numbers():
    """Prompt for and return two numbers as a tuple."""
    a = float(input("Enter first number : "))
    b = float(input("Enter second number: "))
    return a, b


def main():
    operations = {
        "1": ("+", add),
        "2": ("-", subtract),
        "3": ("*", multiply),
        "4": ("/", divide),
        "5": ("%", modulus),
        "6": ("**", power),
    }

    while True:
        show_menu()
        choice = input("Select an operation (1-7): ")

        if choice == "7":
            print("Goodbye!")
            break

        if choice not in operations:
            print("Error: Please enter a number between 1 and 7.")
            print()
            continue

        symbol, operation = operations[choice]
        a, b = get_numbers()

        if choice in ("4", "5") and b == 0:
            print("Error: Cannot divide by zero.")
        else:
            result = operation(a, b)
            print(f"Result: {a:g} {symbol} {b:g} = {result}")

        print()  # blank line for readability between cycles


if __name__ == "__main__":
    main()