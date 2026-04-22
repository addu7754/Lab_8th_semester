str = input("Enter a String\n")
vowels = ['a','e','i','o','u','A','E','I','O','U']
count = 0
for alphabet in str:
    if alphabet in vowels:
        count+=1
print(f"The number of vowels is {count}")
