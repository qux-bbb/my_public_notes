# golang---flag模块示例

```go
package main

import (
	"flag"
	"fmt"
)

func main() {

	wordPtr := flag.String("word", "foo", "a string")

	numbPtr := flag.Int("numb", 42, "an int")
	forkPtr := flag.Bool("fork", false, "a bool")

	var svar string
	flag.StringVar(&svar, "svar", "bar", "a string var")

	flag.Parse()

	fmt.Println("word:", *wordPtr)
	fmt.Println("numb:", *numbPtr)
	fmt.Println("fork:", *forkPtr)
	fmt.Println("svar:", svar)
	fmt.Println("tail:", flag.Args())
}
```

执行: `go run test.go --help`  
输出：  
```r
  -fork
        a bool
  -numb int
        an int (default 42)
  -svar string
        a string var (default "bar")
  -word string
        a string (default "foo")
```


原链接: https://gobyexample.com/command-line-flags  


2022/12/20  
