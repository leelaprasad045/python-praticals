def input_matrix(rows, cols, name):
    print(f"Enter elements of Matrix {name} ({rows}x{cols}):")
    matrix = []

    for i in range(rows):
        row = list(map(int, input(f"Row {i + 1}: ").split()))
        if len(row) != cols:
            print(f"Invalid row length. Please enter exactly {cols} values.")
            return None
        matrix.append(row)

    return matrix


def add_matrices(matrix_a, matrix_b):
    return [
        [matrix_a[i][j] + matrix_b[i][j] for j in range(len(matrix_a[0]))]
        for i in range(len(matrix_a))
    ]


def multiply_matrices(matrix_a, matrix_b):
    result = []

    for i in range(len(matrix_a)):
        row = []
        for j in range(len(matrix_b[0])):
            product = sum(
                matrix_a[i][k] * matrix_b[k][j]
                for k in range(len(matrix_b))
            )
            row.append(product)
        result.append(row)

    return result


def main():
    try:
        r1 = int(input("Enter number of rows for Matrix A: "))
        c1 = int(input("Enter number of columns for Matrix A: "))
        r2 = int(input("Enter number of rows for Matrix B: "))
        c2 = int(input("Enter number of columns for Matrix B: "))

        if r1 <= 0 or c1 <= 0 or r2 <= 0 or c2 <= 0:
            print("Rows and columns must be positive integers.")
            return

        matrix_a = input_matrix(r1, c1, "A")
        if matrix_a is None:
            return

        matrix_b = input_matrix(r2, c2, "B")
        if matrix_b is None:
            return

        if r1 == r2 and c1 == c2:
            print("\nMatrix Addition (A + B):")
            for row in add_matrices(matrix_a, matrix_b):
                print(row)
        else:
            print("\nMatrix addition is not possible (incompatible dimensions).")

        if c1 == r2:
            print("\nMatrix Multiplication (A x B):")
            for row in multiply_matrices(matrix_a, matrix_b):
                print(row)
        else:
            print(
                "\nMatrix multiplication is not possible "
                "(the columns of A must equal the rows of B)."
            )
    except ValueError:
        print("Invalid input. Please enter only integers.")


if __name__ == "__main__":
    main()