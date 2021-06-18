# C---结构体

结构体简单使用  

Books是结构体  
book是结构体变量，访问成员使用 `.`  
book_p是指向结构体变量的指针，访问成员使用 `->`  

```cpp
#include <stdio.h>

struct Books
{
    char  title[50];
    char  author[50];
    char  subject[100];
    int   book_id;
};


int main()
{
    Books book = { "C 语言", "RUNOOB", "编程语言", 123456 };

    printf("直接访问方式：\n");
    printf("title : %s\nauthor: %s\nsubject: %s\nbook_id: %d\n", book.title, book.author, book.subject, book.book_id);

    printf("\n使用指针访问方式：\n");
    Books* book_p = &book;
    printf("title : %s\nauthor: %s\nsubject: %s\nbook_id: %d\n", book_p->title, book_p->author, book_p->subject, book_p->book_id);

    return 0;
}
```


参考链接: https://www.runoob.com/cprogramming/c-structures.html  


2021/6/18  
