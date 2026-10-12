package main

import "fmt"

func message(name string) string {
	return fmt.Sprintf("Hello from %s.", name)
}

func main() {
	fmt.Println(message("Go"))
}
