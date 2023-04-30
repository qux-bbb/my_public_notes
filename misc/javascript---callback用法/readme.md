# javascript---callback用法

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Test</title>
</head>
<body>
    <script>
        function first(callback) {
            let a = 'hello world';
            callback(a);
        }
        first(function(value){
            alert(value);
        });
    </script>
</body>
</html>
```


2018/4/10  
