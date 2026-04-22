import numpy as np

def main():
    # Generate a random array of 10 elements between 1 and 100
    rand_array = np.random.randint(1, 100, 10)
    print(f"Random Array: {rand_array}")
    
    # Find max and min
    max_val = np.max(rand_array)
    min_val = np.min(rand_array)
    
    print(f"Maximum Value: {max_val}")
    print(f"Minimum Value: {min_val}")

if __name__ == "__main__":
    main()
