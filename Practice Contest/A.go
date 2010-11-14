// Problem: Old Magician
// Language: Go
// Author: KirarinSnow
// Usage: 8g thisfile.go && 8l thisfile.8 && ./8.out <input.in >output.out


package main

import (
    "os"
    "fmt"
    "scanner"
    "strconv"
)

func main() {
    var s scanner.Scanner
    s.Init(os.Stdin)
    s.Scan()
    total, _ := strconv.Atoi(s.TokenText())
    for i := 1; i <= total; i++ {
        s.Scan()
        _ = s.TokenText()
        s.Scan()
        b, _ := strconv.Atoi(s.TokenText())
        var out string
        if b % 2 == 0 {
            out = "WHITE"
        } else {
            out = "BLACK"
        }
        fmt.Printf("Case #%d: %s\n", i, out)
    }
}
