# Question 5: CSS Integration with XML Files

**Problem Statement:** 
Create external style sheet and using the style sheet in XML file.


```html
books {
    display: block;
    background-color: #f0f0f0;
    padding: 20px;
    font-family: Arial, sans-serif;
    text-align: center;
}

book {
    display: block;
    background-color: #ffffff;
    margin: 15px auto;
    padding: 15px;
    border: 2px solid #007bff;
    border-radius: 8px;
    width: 60%;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
}

title {
    display: block;
    font-size: 24px;
    font-weight: bold;
    color: #333;
    margin-bottom: 5px;
}

author {
    display: block;
    font-size: 18px;
    color: #666;
    font-style: italic;
    margin-bottom: 10px;
}

price {
    display: block;
    font-size: 16px;
    color: #28a745;
    font-weight: bold;
}
```



```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/css" href="week12_prob3.css"?>
<books>
    <book>
        <title>Web Engineering Design Principles</title>
        <author>Dr. Jane Carter</author>
        <price>$45.99</price>
    </book>
    <book>
        <title>Advanced Data Science Algorithms</title>
        <author>William B. Smith</author>
        <price>$52.50</price>
    </book>
    <book>
        <title>A Hybrid Cloud Architecture Guide</title>
        <author>Anna Richards</author>
        <price>$38.00</price>
    </book>
</books>
```


