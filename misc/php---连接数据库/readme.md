# php---连接数据库

```php
<?php

function blightDB()
{
        static $conn;
        if (!isset($conn))
        {
            $dbhost = 'localhost:3306';  // mysql服务器主机地址
			$dbuser = 'root';            // mysql用户名
			$dbpass = 'helloworld';          // mysql用户名密码
			$conn = mysqli_connect($dbhost, $dbuser, $dbpass);
			if(! $conn )
			{
			    die('Could not connect: ' . mysqli_error());
			}
			echo '数据库连接成功！<br/>';
        }
        return $conn;
}
 
 
function blightVuln($password)
{
        
        $conn = blightDB();
        $id = 1;
        $query = "SELECT 1 FROM (SELECT password FROM blight WHERE id=$id) b WHERE password='$password'";
        mysqli_select_db( $conn, 'test');
        $retval = mysqli_query($conn, $query);
        return $retval;
}



// 开始执行的东西
blightDB();

$password = "pass";
if(isset($_POST["password"])){
	$password = $_POST["password"];
	$result = blightVuln($password);
	if($result){
		echo "you got it.";
	}else{
		echo "Losing it!";
	}
}


?>



<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>blind sql injection</title>
</head>
<body>
    <a href="index.php?do=blightDB">初始化环境</a>
    
    <form action="index.php" method = "post">
    	<input type="text" name="password">
    	<input type="submit">
    </form>
</body>
</html>
```


2017/9/2  
