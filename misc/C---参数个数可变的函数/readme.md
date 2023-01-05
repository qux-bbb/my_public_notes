# C---参数个数可变的函数

```cpp
#include <stdio.h>
#include <stdarg.h>

double average(int num,...) {

   va_list valist;
   double sum = 0.0;
   int i;

   /* initialize valist for num number of arguments */
   va_start(valist, num);

   /* access all the arguments assigned to valist */
   for (i = 0; i < num; i++) {
      sum += va_arg(valist, int);
   }
	
   /* clean memory reserved for valist */
   va_end(valist);

   return sum/num;
}

int main() {
   printf("Average of 2, 3, 4, 5 = %f\n", average(4, 2,3,4,5));
   printf("Average of 5, 10, 15 = %f\n", average(3, 5,10,15));
}
```

输出：  
```r
Average of 2, 3, 4, 5 = 3.500000
Average of 5, 10, 15 = 10.000000
```

原链接: https://www.tutorialspoint.com/cprogramming/c_variable_arguments.htm  


2023/1/5  
