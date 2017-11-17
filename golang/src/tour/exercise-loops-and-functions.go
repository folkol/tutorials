package main

import (
    "fmt"
    "math"
)

func Sqrt(x float64) float64 {
    z := 1.0
    oldz := 1 - z
    for math.Abs(z - oldz) > 0.0000001 {
        fmt.Println(z)
        // Newton-Raphson
        oldz = z
        z -= (z*z - x) / (2*z)
    }
    fmt.Println()
    return z
}

func main() {
    fmt.Println(Sqrt(2))
    fmt.Println(math.Sqrt(2))
}

