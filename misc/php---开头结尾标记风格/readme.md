# php---开头结尾标记风格

官方资料(PHP Opening and Closing Tags)  
1.  
```php
<?php echo 'if you want to serve PHP code in XHTML or XML documents,
    use these tags'; ?>
```

2. You can use the short echo tag . It's always enabled in PHP 5.4.0 and later  
```php
<?= 'print this string' ?>
```

3.  
```php
<? echo 'this code is within short tags, but will only work '.
    'if short_open_tag is enabled'; ?>
```

4. This syntax is removed in PHP 7.0.0.  
```php
<script language="php">
    echo 'some editors (like FrontPage) don\'t
          like processing instructions within these tags';
</script>
``` 

5. Both of these syntaxes are removed in PHP 7.0.0.  
```php
<% echo 'You may optionally use ASP-style tags'; %>
<%= $variable; %>
```

原链接: https://www.php.net/manual/en/language.basic-syntax.phpmode.php  


2017/9/2  
