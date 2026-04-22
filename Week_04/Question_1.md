# Question 1: Dictionaries and lists in python

**Create a dictionary of student names and marks. Display students scoring above 75. **

```python
#Create a dictionary of student names and marks
student_details = {
    'Aman': 85,
    'joey': 60,
    'Chandler': 92,
    'monica': 75,
    'Gulzar': 88,
    'Ammar': 70
}

#Display students scoring above 75
print("Students scoring above 75:")
for name, marks in student_details.items():
    if marks > 75:
        print(f"{name}")
```

**Output:**

```sh
Students scoring above 75:
Aman
Chandler
Gulzar
```




**Write a program to sort a list in ascending and descending order.**

```txt
   #Sort a list  in ascending and descending order
   list = [10, 2, 15, 27, 35, 97]

   # Ascending order
   list.sort()
   print(list)

   # Descending order
   list.sort( reverse=True)

   print (list)    
```


