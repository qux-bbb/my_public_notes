# golang---生成随机buffer

keywords: 字节流  

```go
package main

import (
	"crypto/rand"
	"log"
)

func main() {
	// first step is to create a slice of bytes with the desired length
	buf := make([]byte, 10)
	// then we can call rand.Read.
	_, err := rand.Read(buf)
	if err != nil {
		log.Fatalf("error while generating random string: %s", err)
	}
	// print the bytes (numbers from 0 to 255) with %v format verb (raw value)
	log.Printf("random bytes: %v", buf)
	// print the bytes encoded in hexadecimal with %x format verb
	log.Printf("random hex: %x", buf)
}
```

输出：  
```r
2022/12/20 23:11:52 random bytes: [106 63 151 232 19 108 138 213 177 90]
2022/12/20 23:11:52 random hex: 6a3f97e8136c8ad5b15a
```

原链接: https://www.practical-go-lessons.com/post/how-to-generate-random-bytes-with-golang-ccc9755gflds70ubqc2g  


2022/12/20  
