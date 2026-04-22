# Question 5: Digital Clock

**Problem Statement:** 
Using JavaScript create a digital clock.


```html
<!DOCTYPE html>
<html>
<head>
    <title>Digital Clock</title>
    <style>
        .clock {
            font-family: 'Courier New', Courier, monospace;
            font-size: 48px;
            color: #333;
            text-align: center;
            margin-top: 20%;
        }
    </style>
</head>
<body>
    <div class="clock" id="digitalClock"></div>

    <script>
        function updateClock() {
            const now = new Date();
            let hours = now.getHours();
            let minutes = now.getMinutes();
            let seconds = now.getSeconds();
            
            // Format time to strictly 2 digits
            hours = hours < 10 ? '0' + hours : hours;
            minutes = minutes < 10 ? '0' + minutes : minutes;
            seconds = seconds < 10 ? '0' + seconds : seconds;
            
            const timeString = hours + ':' + minutes + ':' + seconds;
            document.getElementById('digitalClock').textContent = timeString;
        }

        // Update the clock every second
        setInterval(updateClock, 1000);
        
        // Initialize the clock immediately
        updateClock();
    </script>
</body>
</html>
```


