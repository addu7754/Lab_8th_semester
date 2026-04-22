# Question 3: Multi-page Form Data Transfer (ABC.COM)

**Problem Statement:** 
Design a series of three HTML Pages for ABC.COM, each called from the previous one. Accept Name on the first page. When the user clicks on the enter button, second page should open. The second page should not display the name but a 'Welcome screen with some information about ABC.COM. When the user will click on the 'next' button it should display the name accepted in page 1 on page 3. (Hint: you may use hidden fields)


```html
<!DOCTYPE html>
<html>
<head><title>ABC.COM - Page 1</title></head>
<body>
    <h1>ABC.COM</h1>
    <!-- Form submits to page2.html via GET to pass data without a backend -->
    <form action="page2.html" method="get">
        <label>Enter Name:</label>
        <input type="text" name="username" required>
        <input type="submit" value="Enter">
    </form>
</body>
</html>
```



```html
<!DOCTYPE html>
<html>
<head><title>ABC.COM - Page 2</title></head>
<body>
    <h1>Welcome to ABC.COM!</h1>
    <p>ABC.COM is a leading company in web technologies and software engineering.</p>
    
    <form action="page3.html" method="get">
        <!-- Hidden field to carry forward the name -->
        <input type="hidden" name="username" id="hiddenName">
        <input type="submit" value="Next">
    </form>

    <script>
        // Extract the 'username' from the URL parameters
        const params = new URLSearchParams(window.location.search);
        document.getElementById('hiddenName').value = params.get('username') || '';
    </script>
</body>
</html>
```



```html
<!DOCTYPE html>
<html>
<head><title>ABC.COM - Page 3</title></head>
<body>
    <h1>ABC.COM - Dashboard</h1>
    <h2 id="greeting"></h2>

    <script>
        // Retrieve the name passed from Page 2's hidden field
        const params = new URLSearchParams(window.location.search);
        const name = params.get('username') || 'Guest';
        document.getElementById('greeting').innerText = "Hello, " + name + "!";
    </script>
</body>
</html>
```


