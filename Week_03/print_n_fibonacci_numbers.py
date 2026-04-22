def fib(n: int):
    a, b = 0, 1
    
    for _ in range(n):
        print(a)
        # 'a' becomes 'b', and 'b' becomes the sum
        a, b = b, a + b

if __name__ == "__main__":
    n = int(input("Enter how many fibonacci numbers you want to print: "))
    fib(n)
