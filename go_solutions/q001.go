package main

import "fmt"

func compute() int {
	n := 1000
	var sum int

	for i := 0; i < n; i++ {
		if i%3 == 0 || i%5 == 0 {
			sum += i
		}
	}

	return sum
}

func main() {
	fmt.Println(compute())
}
