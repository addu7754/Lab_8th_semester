# Question 2: Reshaping Elements of Array

**Problem Statement:** 
Reshape a one-dimensional array into a matrix of different sizes.


```python
import numpy as np

def main():
    # Create a 1D array of 12 elements
    arr_1d = np.arange(1, 13)
    print(f"Original 1D Array:\n{arr_1d}\n")
    
    # Reshape to a 3x4 matrix
    matrix_3x4 = arr_1d.reshape(3, 4)
    print(f"Reshaped to 3x4 Matrix:\n{matrix_3x4}\n")
    
    # Reshape to a 2x6 matrix
    matrix_2x6 = arr_1d.reshape(2, 6)
    print(f"Reshaped to 2x6 Matrix:\n{matrix_2x6}\n")

if __name__ == "__main__":
    main()
```

**Output:**

```sh
Original 1D Array:
[ 1  2  3  4  5  6  7  8  9 10 11 12]

Reshaped to 3x4 Matrix:
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]]

Reshaped to 2x6 Matrix:
[[ 1  2  3  4  5  6]
 [ 7  8  9 10 11 12]]
```



\section{Problems based on HTML and JavaScript}

