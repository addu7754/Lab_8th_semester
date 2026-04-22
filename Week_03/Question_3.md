# Question 3: HTML Table Construction


**Problem Statement:** 
Create the following table in HTML with Dummy Data:

\begin{center}
\begin{tabular}{|l|l|l|l|c|c|l|}
\hline
\multirow{2}{*}{**Name of the Train**} & \multirow{2}{*}{**Place**} & \multirow{2}{*}{**Destination**} & \multirow{2}{*}{**Train No.**} & \multicolumn{2}{c|}{**Time**} & \multirow{2}{*}{**Fair**}  
\cline{5-6}
 & & & & **Arrival** & **Departure** &  
\hline
Rajdhani Exp & New Delhi & Mumbai & 12951 & 16:25 & 08:35 & 2800  \hline
Shatabdi Exp & Lucknow & New Delhi & 12003 & 15:35 & 22:30 & 1200  \hline
Vande Bharat & Varanasi & New Delhi & 22435 & 15:00 & 23:00 & 1800  \hline
\end{tabular}
\end{center}

\vspace{3cm}
**Source Code:**


```html
<!DOCTYPE html>
<html>
<head>
    <title>Train Schedule</title>
    <style>
        table {
            border-collapse: collapse;
            width: 100%;
        }
        th, td {
            border: 1px solid black;
            padding: 8px;
            text-align: left;
        }
        th {
            background-color: #f2f2f2;
        }
    </style>
</head>
<body>

    <h2>Train Schedule</h2>

    <table>
        <thead>
            <tr>
                <th rowspan="2">Name of the Train</th>
                <th rowspan="2">Place</th>
                <th rowspan="2">Destination</th>
                <th rowspan="2">Train No.</th>
                <th colspan="2" ">Time</th>
                <th rowspan="2">Fair</th>
            </tr>
            <tr>
                <th>Arrival</th>
                <th>Departure</th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <td>Rajdhani Exp</td>
                <td>New Delhi</td>
                <td>Mumbai</td>
                <td>12951</td>
                <td>16:25</td>
                <td>08:35</td>
                <td>2800</td>
            </tr>
            <tr>
                <td>Shatabdi Exp</td>
                <td>Lucknow</td>
                <td>New Delhi</td>
                <td>12003</td>
                <td>15:35</td>
                <td>22:30</td>
                <td>1200</td>
            </tr>
            <tr>
                <td>Vande Bharat</td>
                <td>Varanasi</td>
                <td>New Delhi</td>
                <td>22435</td>
                <td>15:00</td>
                <td>23:00</td>
                <td>1800</td>
            </tr>
        </tbody>
    </table>

</body>
</html>
```


\newpage
