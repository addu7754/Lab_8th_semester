# Question 3: Frame-based Layout (Rows and Columns)


**Problem Statement:** 
Write an HTML code to develop a web page having two frames that divide the web page into two equal rows. Then, divide the second row into two equal columns. Fill each frame with a different background color.

**Source Code Solution:**


```html
<!DOCTYPE html>
<html>
<head>
    <title>Frameset Layout</title>
</head>
<frameset rows="50%, 50%">
    
    <frame src="about:blank" style="background-color: #ffcccc;" name="topFrame">
    
    <frameset cols="50%, 50%">
        
        <frame src="about:blank" style="background-color: #ccffcc;" name="leftFrame">
        
        <frame src="about:blank" style="background-color: #ccccff;" name="rightFrame">
        
    </frameset>
    
</frameset>
</html>
```


