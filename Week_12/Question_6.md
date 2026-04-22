# Question 6: XSL Transformation of XML to HTML Document

**Problem Statement:** 
Create an XSL style sheet to display the data in the xml using HTML table.


```xml
<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
<xsl:template match="/">
  <html>
  <head>
    <title>Employee Database Catalog</title>
    <style>
      body { font-family: 'Segoe UI', Arial, sans-serif; background-color: #f8f9fa; text-align: center; margin: 40px; }
      table { width: 70%; margin: 20px auto; border-collapse: collapse; box-shadow: 0 0 10px rgba(0,0,0,0.1); background-color: white;}
      th, td { border: 1px solid #ced4da; padding: 12px; text-align: center; }
      th { background-color: #007bff; color: white; text-transform: uppercase; }
      tr:hover { background-color: #f1f1f1; cursor: default; }
      h2 { color: #343a40; text-transform: uppercase; font-weight: 700; margin-bottom: 20px; }
    </style>
  </head>
  <body>
    <h2>Employee Database Catalog</h2>
    <table>
      <tr>
        <th>Employee ID</th>
        <th>Name</th>
        <th>Department</th>
        <th>Job Title</th>
      </tr>
      <xsl:for-each select="company/employee">
      <tr>
        <td><xsl:value-of select="id"/></td>
        <td><xsl:value-of select="name"/></td>
        <td><xsl:value-of select="department"/></td>
        <td><xsl:value-of select="title"/></td>
      </tr>
      </xsl:for-each>
    </table>
  </body>
  </html>
</xsl:template>
</xsl:stylesheet>
```



```xml
<?xml version="1.0" encoding="UTF-8"?>
<?xml-stylesheet type="text/xsl" href="week12_prob4.xsl"?>
<company>
    <employee>
        <id>SA7001</id>
        <name>Robert Anderson</name>
        <department>Information Technology</department>
        <title>System Administrator</title>
    </employee>
    <employee>
        <id>SA7002</id>
        <name>Elena Rossi</name>
        <department>Data Analytics</department>
        <title>Machine Learning Engineer</title>
    </employee>
    <employee>
        <id>SA7003</id>
        <name>Marcus Cho</name>
        <department>Web Engineering</department>
        <title>Senior Frontend Developer</title>
    </employee>
</company>
```


\end{document}