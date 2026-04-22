# Question 4: JavaScript Confirm Greeting

**Problem Statement:** 
Write the segment of Script that would ask the user if he wants a greeting message and if he does, display a Gif file called Welcome.gif and display "Welcome to Department of Computer Science!" in the document window following the Gif.


```html
<!DOCTYPE html>
<html>
<head><title>Greeting Page</title></head>
<body>
    <script>
        // Ask the user using confirm()
        if (confirm("Do you want a greeting message?")) {
            // If true, write the GIF and text to the document
            document.write('<img src="Welcome.gif" alt="Welcome Image"><br><br>');
            document.write('<h2>Welcome to Department of Computer Science!</h2>');
        } else {
            document.write('<h2>Goodbye!</h2>');
        }
    </script>
</body>
</html>
```


