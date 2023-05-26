# php---session

```php
<?php
    session_start();
    if(!isset($_SESSION['a']){
        $_SESSION['a'] = 1;
    }else{
        $_SESSION['a'] = $_SESSION['a'] + 1;
    }
?>
```


2018/1/15  
