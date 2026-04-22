# Question 5: Unequal Frames with Validated Forms

**Problem Statement:** 
Create a website that divides the Web page into two unequal frames. In Frame One, there are two links to two different forms. The forms are validated on submitting and the result is shown at the bottom of the same page. Use CSS for formatting.


```html
<!DOCTYPE html>
<html>
<head>
    <title>Two Unequal Frames</title>
</head>
<!-- Divides the window into left (30%) and right (70%) unequal frames -->
<frameset cols="30%, 70%">
    <frame src="frame1.html" name="menuFrame">
    <frame src="form1.html" name="contentFrame">
</frameset>
</html>
```



```html
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial; background-color: #f4f4f9; padding: 20px; }
        a { 
            display: block; margin-bottom: 15px; padding: 10px; 
            background-color: #007bff; color: white; 
            text-decoration: none; text-align: center; border-radius: 5px; 
        }
        a:hover { background-color: #0056b3; }
    </style>
</head>
<body>
    <h2>Menu</h2>
    <!-- Targets the right-side frame -->
    <a href="form1.html" target="contentFrame">Registration Form</a>
    <a href="form2.html" target="contentFrame">Feedback Form</a>
</body>
</html>
```



```html
<!DOCTYPE html>
<html>
<head>
    <style>
        body { font-family: Arial, sans-serif; padding: 20px; text-align: center;}
        .form-box { 
            border: 1px solid #ccc; padding: 20px; 
            border-radius: 8px; width: 60%; margin: 0 auto; 
            background: #fff; box-shadow: 2px 2px 8px rgba(0,0,0,0.1); 
        }
        input { display: block; margin: 10px auto; width: 90%; padding: 8px; border: 1px solid #ccc; border-radius: 4px; }
        button { padding: 10px 15px; background: #28a745; color: white; border: none; border-radius: 4px; cursor: pointer; }
        button:hover { background: #218838; }
        #result { margin-top: 20px; color: blue; font-weight: bold; font-size: 1.2em; }
    </style>
    <script>
        function validateRegistration(e) {
            e.preventDefault(); // Stop page reload
            let name = document.getElementById("name").value;
            let email = document.getElementById("email").value;
            let resultDiv = document.getElementById("result");
            
            if(name.trim() === "" || email.trim() === "") {
                resultDiv.style.color = "red";
                resultDiv.innerText = "Error: Name and Email fields cannot be empty!";
            } else {
                resultDiv.style.color = "green";
                resultDiv.innerText = "Registration Configured for: " + name + " (" + email + ")";
            }
        }
    </script>
</head>
<body>
    <div class="form-box">
        <h3>Registration Form</h3>
        <form onsubmit="validateRegistration(event)">
            <input type="text" id="name" placeholder="Enter Full Name">
            <input type="email" id="email" placeholder="Enter Email Address">
            <button type="submit">Submit Registration</button>
        </form>
    </div>
    <!-- Result prints here on the same page -->
    <div id="result"></div>
</body>
</html>
```


