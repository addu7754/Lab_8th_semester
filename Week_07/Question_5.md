# Question 5: Image Rollover (Mouse Hover)

**Problem Statement:** 
Create a Web page using two image files, which switch between one another as the mouse pointer moves over the image. Use the On Mouse over and On Mouse out event handler.


```html
<!DOCTYPE html>
<html>
<head>
    <title>Image Switcher</title>
</head>
<body>
    <h2>Hover over the image to switch it</h2>
    
    <!-- We use 'onmouseover' to change the image URL and 'onmouseout' to revert it -->
    <img src="image1.jpg" id="switcherImg"
         onmouseover="this.src='image2.jpg';"
         onmouseout="this.src='image1.jpg';" 
         alt="Interactive Image">
         
</body>
</html>
```


