# IE---Msgbox弹出

```html

<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="X-UA-Compatible" content="ie=10">
    <title>Document</title>
</head>
<body>
    <script language="vbscript">
        Msgbox "Hello World"
    </script>
</body>
</html>

```

重要的有两点  

`<meta http-equiv="X-UA-Compatible" content="ie=10">`  
必须有这一行，并且content中ie的取值必须为数字，范围为[0, 11)  

`<script language="vbscript">`  
只能写成这种形式  


2019/7/2  
