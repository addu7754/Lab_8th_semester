import numpy as np

def indexing_slicing():
    # Create a 2D array (Matrix) for better demonstration
    arr = np.array([
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ])
    
    print("Original Array:\n", arr)

    # --- Indexing ---
    # Accessing specific elements
    element = arr[1, 2] # Row 1, Column 2 (Value: 7)
    print(f"\nElement at [1, 2]: {element}")

    # --- Slicing ---
    # Slicing rows: Row 0 and 1
    print("\nSlice (First 2 Rows):\n", arr[0:2, :])

    # Slicing columns: Column 1 and 2 for all rows
    print("\nSlice (Middle Columns):\n", arr[:, 1:3])

if __name__ == "__main__":
    indexing_slicing()
