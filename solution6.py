def generate_fibonacci_terms(n):
    """Return a list of the first n Fibonacci numbers."""
    sequence = []
    a, b = 0, 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b
    return sequence


def is_fibonacci(num):
    """Return True if num appears in the Fibonacci sequence, False otherwise."""
    if num < 0:
        return False
    a, b = 0, 1
    while a <= num:
        if a == num:
            return True
        a, b = b, a + b
    return False


def main():
    # ---------------- PART A ----------------
    n = int(input("How many terms? "))
    if n <= 0:
        print("Error: N must be a positive integer.")
    else:
        terms = generate_fibonacci_terms(n)
        print("Fibonacci sequence:", " ".join(str(t) for t in terms))

    # ---------------- PART B ----------------
    num = int(input("Enter a number to check: "))
    if is_fibonacci(num):
        print(f"{num} is a Fibonacci number.")
    else:
        print(f"{num} is NOT a Fibonacci number.")


if __name__ == "__main__":
    main()