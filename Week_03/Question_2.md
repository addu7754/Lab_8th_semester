# Question 2: Write a python program to count the number of vowels in a given string.



```python
str = input("Enter a String\n")
vowels = ['a','e','i','o','u','A','E','I','O','U']
count = 0
for alphabet in str:
    if alphabet in vowels:
        count+=1
print(f"The number of vowels is {count}")
```

\vspace{0.5cm}
**Output:**

```sh
Enter a String
Adnan
The number of vowels is 2
```


