
import numpy as np


# Validate inputs for vector-vector operations
def validate_vectors(u, v):
    u = np.asarray(u)
    v = np.asarray(v)

    if u.ndim != 1 or v.ndim != 1:
        raise ValueError("Both inputs must be one-dimensional vectors.")

    if len(u) != len(v):
        raise ValueError("Vectors must have the same length.")

    return u, v


# Scalar-vector operations
def scalar_add(s, v):
    return s + v


def scalar_subtract(s, v):
    return s - v


def scalar_multiply(s, v):
    return s * v


def scalar_divide(s, v):
    if np.any(np.asarray(v) == 0):
        raise ZeroDivisionError(
            "Cannot divide by a value containing zero."
        )
    return s / v


# Vector-vector operations
def add_vectors(u, v):
    u, v = validate_vectors(u, v)
    return u + v


def subtract_vectors(u, v):
    u, v = validate_vectors(u, v)
    return u - v


def multiply_vectors(u, v):
    u, v = validate_vectors(u, v)
    return u * v


def divide_vectors(u, v):
    u, v = validate_vectors(u, v)

    if np.any(v == 0):
        raise ZeroDivisionError(
            "Cannot divide a vector by a vector containing zero."
        )

    return u / v


# Dot product with input validation
def calculate_dot_product(u, v):
    u, v = validate_vectors(u, v)
    return np.dot(u, v)


# Main program
def main():
    s = 5
    v = np.array([1, 2, 3])

    print("1. Scalar-vector operations")

    print(f"{s} + {v} = {scalar_add(s, v)}")
    print(f"{s} - {v} = {scalar_subtract(s, v)}")
    print(f"{s} * {v} = {scalar_multiply(s, v)}")
    print(f"{s} / {v} = {scalar_divide(s, v)}")

    print("\n2. Vector-vector operations")

    u = np.array([1, 2, 3])
    v = np.array([4, 5, 6])

    print(f"{u} + {v} = {add_vectors(u, v)}")
    print(f"{u} - {v} = {subtract_vectors(u, v)}")
    print(f"{u} * {v} = {multiply_vectors(u, v)}")
    print(f"{u} / {v} = {divide_vectors(u, v)}")

    print("\n3. Dot product")

    dot_product = calculate_dot_product(u, v)
    print(f"Dot product of {u} and {v} = {dot_product}")

    # Demonstrate function reuse
    u2 = np.array([2, 3])
    v2 = np.array([4, 5])

    print(
        f"Dot product of {u2} and {v2} = "
        f"{calculate_dot_product(u2, v2)}"
    )


if __name__ == "__main__":
    main()

    # Python identifies how a file is being used.
    # It uses the special variable __name__ to represent that information.
    # The condition checks the variable's value.
    # If the condition is true, the main() function is called.
