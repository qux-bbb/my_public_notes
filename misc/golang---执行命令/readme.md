# golang---执行命令

```go
package main

import (
	"fmt"
	"os/exec"
)

func execute() {

	// here we perform the dir command.
	// we can store the output of this in our out variable
	// and catch any errors in err
	out, err := exec.Command("dir").Output()

	// if there is an error with our execution
	// handle it here
	if err != nil {
		fmt.Printf("%s", err)
	}
	// as the out variable defined above is of type []byte we need to convert
	// this to a string or else we will see garbage printed out in our console
	// this is how we convert it to a string
	fmt.Println("Command Successfully Executed")
	output := string(out[:])
	fmt.Println(output)

}

func main() {
	execute()
}
```

原链接: https://tutorialedge.net/golang/executing-system-commands-with-golang/  


2022/6/5  
