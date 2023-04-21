# SQL Injection

1. Retrieving Hidden Data
   
    https://sample.com/blogs?category=Python

    ```sql
    SELECT * FROM blogs WHERE category = 'python' AND is_active = True
    ```

    https://sample.com/blogs?category=Python'--

    The double-dash sequence is a comment indicator
    
    ```sql
    SELECT * FROM blogs WHERE category = 'python'--' AND is_active = 1
    ```