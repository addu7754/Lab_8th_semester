# Question 6: Combobox Populated Dynamic Calendars

**Problem Statement:** 
Create an HTML page with 2 combo box populated with month \& year, to display the calendar for the selected month \& year from combo box using JavaScript.


```html
<!DOCTYPE html>
<html>
<head>
    <title>Dynamic Combobox Calendar</title>
    <style>
        body { font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; text-align: center; background: #fdfdfd; padding: 20px;}
        .form-container { background: #fff; padding: 20px; border-radius: 8px; font-size: 16px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); width: 350px; margin: auto; border: 1px solid #e1e1e1;}
        .form-container select { padding: 8px; margin: 10px; font-size: 16px; border-radius: 4px; border: 1px solid #ccc;}
        .form-container button { padding: 10px 20px; font-size: 16px; color: white; background-color: #007bff; border: none; border-radius: 4px; cursor: pointer; transition: 0.3s;}
        .form-container button:hover { background-color: #0056b3; }
        #calendarArea { margin-top: 30px; display: flex; justify-content: center; }
        table { width: 100%; border-collapse: collapse; background: white; border: 1px solid #ddd; }
        th, td { padding: 12px; text-align: center; border: 1px solid #eee; }
        th { background: #007bff; color: white; font-weight: 500; }
        td { color: #333; }
        td:not(.empty):hover { background: #f1f8ff; cursor: default; }
        .empty { background: #f9f9f9; border: none;}
        .cal-header { font-size: 20px; font-weight: bold; margin-bottom: 15px; color: #444; }
    </style>
</head>
<body>

    <div class="form-container">
        <h2>Select Calendar Date</h2>
        <!-- 1. Two Comboboxes for Month and Year -->
        <label for="monthSelect">Month:</label>
        <select id="monthSelect">
            <option value="0">January</option>
            <option value="1">February</option>
            <option value="2">March</option>
            <option value="3">April</option>
            <option value="4">May</option>
            <option value="5">June</option>
            <option value="6">July</option>
            <option value="7">August</option>
            <option value="8">September</option>
            <option value="9">October</option>
            <option value="10">November</option>
            <option value="11">December</option>
        </select>
        <br>
        <label for="yearSelect">Year:</label>
        <select id="yearSelect"></select>
        <br>
        <button onclick="displayCalendar()">Show Calendar</button>
    </div>

    <!-- Container for dynamic calendar rendering -->
    <div id="calendarArea"></div>

    <script>
        // 2. Populate the 'Year' Combobox on page load dynamically
        window.onload = function() {
            let yearSelect = document.getElementById('yearSelect');
            let currentYear = new Date().getFullYear();
            // Populate years from currentYear-5 to currentYear+5
            for (let i = currentYear - 5; i <= currentYear + 5; i++) {
                let option = document.createElement("option");
                option.value = i;
                option.text = i;
                if (i === currentYear) option.selected = true; // Default to current year
                yearSelect.add(option);
            }
            // Set current month as default selected value
            document.getElementById('monthSelect').value = new Date().getMonth();
        };

        // 3. Logic to display the calendar using selected Combobox values
        function displayCalendar() {
            let m = parseInt(document.getElementById('monthSelect').value);
            let y = parseInt(document.getElementById('yearSelect').value);
            const months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"];
            const daysOfWeek = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"];

            let calendarHTML = `<div style="width: 350px;">`;
            calendarHTML += `<div class="cal-header">${months[m]} ${y}</div><table><tr>`;

            // Table headers for days of the week
            for (let d = 0; d < 7; d++) {
                calendarHTML += `<th>${daysOfWeek[d]}</th>`;
            }
            calendarHTML += `</tr><tr>`;

            let firstDay = new Date(y, m, 1).getDay();
            let daysInMonth = new Date(y, m + 1, 0).getDate();
            let dayCount = 1;

            // Empty cells before the 1st day of the month
            for (let i = 0; i < firstDay; i++) {
                calendarHTML += `<td class="empty"></td>`;
            }

            // Fill standard days
            for (let i = firstDay; i < 7; i++) {
                calendarHTML += `<td>${dayCount}</td>`;
                dayCount++;
            }
            calendarHTML += `</tr>`;

            // Fill remaining weeks in the month
            while (dayCount <= daysInMonth) {
                calendarHTML += `<tr>`;
                for (let i = 0; i < 7; i++) {
                    if (dayCount <= daysInMonth) {
                        calendarHTML += `<td>${dayCount}</td>`;
                        dayCount++;
                    } else {
                        calendarHTML += `<td class="empty"></td>`;
                    }
                }
                calendarHTML += `</tr>`;
            }
            
            calendarHTML += `</table></div>`;
            document.getElementById("calendarArea").innerHTML = calendarHTML;
        }
    </script>
</body>
</html>
```

**Output:**

```sh
Interactive Web Page / Rendered in Browser
```


