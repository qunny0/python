package main

import (
	"fmt"
	"runtime"
)

func main() {
	fmt.Println("Hello, world 命令", runtime.Version())
}