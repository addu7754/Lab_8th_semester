# Question 6: Stylized Form Design

**Problem Statement:** 
Design a form as shown below.


```html
<!DOCTYPE html>
<html>
<head>
    <title>Details Form</title>
    <style>
        body { font-family: "Times New Roman", Times, serif; }
        .form-container { width: 500px; margin: 50px auto; }
        
        h2 {
            text-align: center;
            color: #1a428a; /* Deep blue matching the image */
            text-decoration: underline;
        }
        
        table { width: 100%; border-collapse: separate; border-spacing: 0 15px; }
        
        td.label {
            color: #2b5f9e; /* Muted blue for labels */
            width: 30%;
            vertical-align: top;
            padding-top: 5px;
        }
        
        input[type="text"], textarea {
            width: 100%;
            border: 2px inset #ddd; /* Match the 'inset' style from the image */
        }
    </style>
</head>
<body>
    <div class="form-container">
        <h2>Details</h2>
        <form>
            <table>
                <tr>
                    <td class="label">Your Name:</td>
                    <td><input type="text" name="name"></td>
                </tr>
                <tr>
                    <td class="label">Your Address:</td>
                    <td><input type="text" name="address"></td>
                </tr>
                <tr>
                    <td class="label">Your Gender:</td>
                    <td>
                        <span style="color: #2b5f9e;">Male</span> 
                        <input type="radio" name="gender" value="male"> 
                        <span style="color: #2b5f9e;">Female</span> 
                        <input type="radio" name="gender" value="female" checked>
                    </td>
                </tr>
                <tr>
                    <td class="label">Your Country:</td>
                    <td>
                        <select name="country">
                            <option value="India">India</option>
                        </select>
                    </td>
                </tr>
                <tr>
                    <td class="label">Your Opinion:</td>
                    <td><textarea name="opinion" rows="5"></textarea></td>
                </tr>
            </table>
        </form>
    </div>
</body>
</html>
```


