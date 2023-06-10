# c和c++---动态数组创建

一般的数组创建的时候必须是常量，这就造成了一些问题  
比如说，我想在程序执行的时候输入二维数组的第一维为4，第二维为5，或者其他的，如果直接在程序中定义了数组的大小，有的时候数组太大浪费空间，有的时候空间又不够  
创建动态数组就可以了  


## C++
创建动态二维数组：  
```c++
int **a = new int *[m];
for (int i = 0; i < m; i++)
    a[i] = new int[n];
```
释放二维数组空间  
```c++
for(int i=0;i<m;i++)
    delete[] a[i];
delete [] a;
```
举个栗子：
```c++
#include<iostream>  
using namespace std;  
  
int main() {  
    cout << "请输入矩阵行列数字m n："<< endl;  
    int m, n;  
    cin >> m >> n;  
  
    int **a = new int *[m];  
    for (int i = 0; i < m; i++)  
        a[i] = new int[n];  
  
    cout << "请按行优先顺序输入数组元素：" << endl;  
    for (int i = 0; i < m; i++)  
        for (int j = 0; j < n; j++)  
            cin >> a[i][j];  
    cout << "输出：" << endl;  
    for (int i = 0; i < m; i++) {  
        cout << endl;  
        for (int j = 0; j < n; j++)  
            cout << a[i][j]<<" ";  
    }
    
    for(int i=0;i<m;i++)
        delete[] a[i];
    delete [] a;

    return 0;  
}  
```


## C
创建动态二维数组：  
```c
int **p = (int**)malloc(m*sizeof(int*));
for (i = 0; i < m; i++ )
    p[i] = (int*) malloc(n*sizeof(int));
```
释放二维数组空间  
```c
for(i = 0;i < m; i++)
    free(p[i]);
free(p);
```

举个栗子：
```c
#include <stdio.h>
#include <stdlib.h>

int main(){
    int i, j;
    int m, n;
    printf("请输入m n:\n");
    scanf("%d%d", &m, &n);

    int **p = (int**)malloc(m*sizeof(int*));
    for (i = 0; i < m; i++ )
        p[i] = (int*) malloc(n*sizeof(int));

    printf("请输入%d个整数:\n", m*n);
    for(i = 0; i < m; i++)
        for(j = 0; j < n; j++)
            scanf("%d", &p[i][j]);

    for(i = 0; i < m; i++){
        for(j = 0; j < n; j++)
            printf("%d ",p[i][j]);
        printf("\n");
    }

    for(i = 0;i < m; i++)
        free(p[i]);
    free(p);

    return 0;
}

```


---
2017/9/27  
