# SQL---左连接和右连接

左连接是以左边表中的数据为基准，若左边表有数据而右边表没数据，则显示左表中的数据，右表中的数据显示为空  
```sql
SELECT ... LEFT JOIN ... ON  
select * from book as a left join stu as b on a.sutid = b.stuid
```

右连接类比上面  
```sql
SELECT ... RIGHT JOIN ... ON
select * from book as a right join stu as b on a.sutid = b.stuid
```


2017/9/21  
