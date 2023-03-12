# 代码雨效果

代码雨效果，抄自某个网站  

```html
<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
    <title>Hello World!</title>
    <style>
        * {
            margin: 0;
            padding: 0;
        }

        body {
            background: black;
        }

        canvas {
            display: block;
        }
    </style>
</head>

<body>
    <canvas id="ad"></canvas>
    <script>
        var ad = document.getElementById("ad");
        var ctx = ad.getContext("2d");
        ad.height = window.innerHeight;
        ad.width = window.innerWidth;
        var chinese = "Hello World!";
        chinese = chinese.split("");
        var font_size = 15;
        var columns = ad.width / font_size;
        var drops = [];
        for (var x = 0; x < columns; x++) drops[x] = 1;

        function draw() {
            ctx.fillStyle = "rgba(0, 0, 0, 0.05)";
            ctx.fillRect(0, 0, ad.width, ad.height);
            ctx.fillStyle = "#0F0";
            ctx.font = font_size + "px arial";
            for (var i = 0; i < drops.length; i++) {
                var text = chinese[Math.floor(Math.random() * chinese.length)];
                ctx.fillText(text, i * font_size, drops[i] * font_size);
                if (drops[i] * font_size > ad.height && Math.random() > 0.975) drops[i] = 0;
                drops[i]++;
            }
        }
        setInterval(draw, 50);
    </script>
</body>

</html>
```


2018/1/28  
