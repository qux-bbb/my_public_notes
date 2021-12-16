# C#---读写所有字节

```c#
using System;
using System.IO;
using System.Text;

namespace CSharpConsoleApp1
{
    class Program
    {
        static void Main(string[] args)
        {
            string thePath = "test_file";
            byte[] wBytes = { 71, 72, 73 };

            File.WriteAllBytes(thePath, wBytes);
            byte[] rBytes = File.ReadAllBytes(thePath);
            
            Console.WriteLine(Encoding.ASCII.GetString(rBytes));
            Console.ReadKey();
        }
    }
}
```


2021/12/17  
