# Question 4: HTML Form with All Input Types

**1:** 
Design a comprehensive HTML form that utilizes various input types (text, password, email, number, date, radio, checkbox, etc.).


```html
<!DOCTYPE html>
<html>
<head>
    <title>All Input Types</title>
</head>
<body>

    <h2>Student Registration Form</h2>
    
    <form>
        <label>Full Name:</label>
        <input type="text" placeholder="John Doe"><br><br>

        <label>Email:</label>
        <input type="email" placeholder="john@example.com"><br><br>

        <label>Password:</label>
        <input type="password"><br><br>

        <label>Age:</label>
        <input type="number" min="18" max="100"><br><br>

        <label>Date of Birth:</label>
        <input type="date"><br><br>

        <label>Gender:</label>
        <input type="radio" name="gender" value="Male"> Male
        <input type="radio" name="gender" value="Female"> Female<br><br>

        <label>Skills:</label>
        <input type="checkbox"> HTML
        <input type="checkbox"> Python
        <input type="checkbox"> SQL<br><br>

        <label>Upload Resume:</label>
        <input type="file"><br><br>

        <label>Favorite Color:</label>
        <input type="color"><br><br>

        <label>Experience Level:</label>
        <input type="range" min="1" max="10"><br><br>
    </form>
</body>
</html>
```



