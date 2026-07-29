def read_matrix(rows, cols, label=""):
    """Read a matrix of given size from the user, one row at a time."""
    matrix = []
    for i in range(rows):
        while True:
            row_input = input(f"Enter row {i + 1}{label}: ").split()
            row = [int(x) for x in row_input]
            if len(row) != cols:
                print(f"Error: expected {cols} values, got {len(row)}. Try again.")
                continue
            matrix.append(row)
            break
    return matrix


def print_matrix(matrix):
    """Print a matrix in a neat, aligned grid."""
    for row in matrix:
        print("  ".join(f"{val:4}" for val in row))


def transpose(matrix, rows, cols):
    """Return the transpose of a matrix (rows become columns)."""
    result = [[0] * rows for _ in range(cols)]
    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]
    return result


def add_matrices(a, b, rows, cols):
    """Return the element-wise sum of two same-sized matrices."""
    result = [[0] * cols for _ in range(rows)]
    for i in range(rows):
        for j in range(cols):
            result[i][j] = a[i][j] + b[i][j]
    return result


def multiply_matrices(a, b, m, n, p):
    """Return the product of an MxN matrix and an NxP matrix (result MxP)."""
    result = [[0] * p for _ in range(m)]
    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += a[i][k] * b[k][j]
            result[i][j] = total
    return result


def main():
    # ---------------- PART A: Transpose ----------------
    print("=== PART A: Transpose a Matrix ===")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    print_matrix(matrix)

    print("\nTransposed Matrix:")
    print_matrix(transpose(matrix, rows, cols))

    # ---------------- PART B: Addition ----------------
    print("\n=== PART B: Add Two Matrices ===")
    add_rows = int(input("Enter number of rows for both matrices: "))
    add_cols = int(input("Enter number of columns for both matrices: "))

    print("Matrix A:")
    matrix_a = read_matrix(add_rows, add_cols)
    print("Matrix B:")
    matrix_b = read_matrix(add_rows, add_cols)

    print("\nSum:")
    print_matrix(add_matrices(matrix_a, matrix_b, add_rows, add_cols))

    # ---------------- PART C: Multiplication ----------------
    print("\n=== PART C: Multiply Two Matrices ===")
    m = int(input("Enter rows of Matrix A: "))
    n = int(input("Enter columns of Matrix A (= rows of Matrix B): "))
    p = int(input("Enter columns of Matrix B: "))

    print("Matrix A:")
    mat_a = read_matrix(m, n)
    print("Matrix B:")
    mat_b = read_matrix(n, p)

    print("\nProduct (A x B):")
    print_matrix(multiply_matrices(mat_a, mat_b, m, n, p))


if __name__ == "__main__":
    main()