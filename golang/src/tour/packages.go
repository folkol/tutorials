package main

import (
    "fmt"
    "math/rand"
    "math"
)

func main() {
    fmt.Println("My favourite number is", rand.Intn(10))
    fmt.Printf("Now you have %g problems.\n", math.Sqrt(7))
    fmt.Println(math.Pi)
}

