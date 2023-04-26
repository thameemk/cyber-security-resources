# SQL Injection

1. Retrieving Hidden Data
   
    https://thameem.dev/blogs?category=Python

    ```sql
    SELECT * FROM blogs WHERE category = 'python' AND is_active = True
    ```

    https://thameem.dev/blogs?category=Python'--

    The double-dash sequence is a comment indicator
    
    ```sql
    SELECT * FROM blogs WHERE category = 'python'--' AND is_active = 1
    ```