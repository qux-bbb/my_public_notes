# 一些语言的helloworld

keywords: hello world example  

记一些语言的helloworld，直接拿来用  

## C
```cpp
#include <stdio.h>

int main(){
    printf("Hello World!\n");
    return 0;
}
```


## python3
```python
# coding:utf8

def main():
    print('Hello World!')

if __name__ == '__main__':
    main()
```


## rust
```rust
fn main() {
    println!("Hello, world!");
}
```


## c#
```c#
using System;

namespace CSharpConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Hello World!");
            Console.ReadKey();
        }
    }
}
```