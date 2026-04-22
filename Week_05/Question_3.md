# Question 3: Interactive Form with JavaScript

**Problem Statement:** 
Design a page with a text box called 'name' (default value "Victoria") and two buttons:
    -  **Enter:** Opens a new window with the message "Welcome [Name]".
    -  **Reset:** Changes the text box value to 100.


```html
<!DOCTYPE html>
<html>
<head>
    <title>Interactive Form</title>
    <script>
        function showWelcome() {
            // Get the value from the input box
            var name = document.getElementById("nameInput").value;
            
            // Open a new window and write the message
            var newWindow = window.open("", "_blank", "width=400,height=200");
            newWindow.document.write("<h1>Welcome " + name + "</h1>");
        }

        function resetValue() {
            // Requirement: Set value to "100" on click
            document.getElementById("nameInput").value = "100";
        }
    </script>
</head>
<body>

    <h2>User Interaction</h2>
    
    <label>Name:</label>
    <input type="text" id="nameInput" value="Victoria">
    <br><br>

    <button onclick="showWelcome()">Enter</button>
    <button onclick="resetValue()">Reset</button>

</body>
</html>
```


