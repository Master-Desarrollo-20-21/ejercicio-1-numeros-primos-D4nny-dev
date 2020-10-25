package main

import (
	"fmt"
)

func sieveOfEratosthenes(num int) []int {

	filter := make([]bool, num+1)

	for i := 0; i < num+1; i++ {
		filter[i] = false
	}

	for i := 2; i*i <= num; i++ {
		if filter[i] == false {
			for j := i * 2; j <= num; j += i {
				filter[j] = true
			}
		}
	}

	primes := []int{}
	for i := 2; i < num; i++ {
		if filter[i] == false {
			primes = append(primes, i)
		}
	}
	return primes
}

func add(values []int) int {

	total := 0
	for _, v := range values {
		total += v
	}
	return total
}

func addFirstFiftyPrimes() int {
	i := 0
	for {
		if len(sieveOfEratosthenes(i)) < 50 {
			i++
		} else {
			return add(sieveOfEratosthenes(i))
		}
	}
}

func main() {

	// Find all prime numbers up to given limit.
	fmt.Println(sieveOfEratosthenes(7))

	// Add the prime number up to given limit [0-50]
	fmt.Println(add(sieveOfEratosthenes(50)))

	// Add the first Fifty prime numbers
	fmt.Println(addFirstFiftyPrimes())

}
