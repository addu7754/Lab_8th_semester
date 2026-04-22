# Question 1: Write a python program to generate the first n fibonacci numbers using a loop. 



```python
def fib(n: int):
    a, b = 0, 1
    
    for _ in range(n):
        print(a)
        # 'a' becomes 'b', and 'b' becomes the sum
        a, b = b, a + b

if __name__ == "__main__":
    n = int(input("Enter how many fibonacci numbers you want to print: "))
    fib(n)
```

\vspace{0.5cm}
**Output:**

```sh
Enter how many fibonacci numbers you want to print: 10
0
1
1
2
3
5
8
13
21
34
```


