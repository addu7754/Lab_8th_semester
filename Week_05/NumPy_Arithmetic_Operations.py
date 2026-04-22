import numpy as np

def numpy_arithmetic():
    # Create two sample arrays
    arr1 = np.array([10, 20, 30, 40, 50])
    arr2 = np.array([2, 4, 5, 8, 10])

    print("Array 1:", arr1)
    print("Array 2:", arr2)

    # 1. Addition
    print("\n1. Addition (arr1 + arr2):", arr1 + arr2)

    # 2. Subtraction
    print("2. Subtraction (arr1 - arr2):", arr1 - arr2)

    # 3. Multiplication
    print("3. Multiplication (arr1 * arr2):", arr1 * arr2)

    # 4. Division
    print("4. Division (arr1 / arr2):", arr1 / arr2)

    # 5. Exponentiation (Power)
    print("5. Power (arr1 ^ 2):", np.power(arr1, 2))

if __name__ == "__main__":
    numpy_arithmetic()
