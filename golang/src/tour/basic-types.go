// Go basic types: 
// bool, string, (u)int(8, 16, 32, 64), uintptr 
// byte (alias for uint8)
// rune (alias for int32, represents unicode code point)
// float32, float64
// complex64, complex128
package main

import (
	"fmt"
	"math/cmplx"
)

var (
	ToBe   bool       = false
	MaxInt uint64     = 1<<64 - 1
	z      complex128 = cmplx.Sqrt(-5 + 12i)
)

func main() {
    fmt.Printf("Type: %T Value: %v\n", ToBe, ToBe)
    fmt.Printf("Type: %T Value: %v\n", MaxInt, MaxInt)
    fmt.Printf("Type: %T Value: %v\n", z, z)
}

