My notes for Go.

Based on a local copy of "a tour of Go" at https://go.dev/tour/list.

# What Go is

A compiled language that aims to get both efficiency and readability.
Statically typed. offers a dynamic type inference as well.
described as C-like and Python-like in syntax.
It has very quick compilation time compared to other compiled languages.

Advanced: Efficient multi-threading as well.

Runtime: An intermediate, below interpreted languages but above compiled languages.

# Comparison to C and Python

Automatically runs the function main, like C.

strongly typed, unlike C. Expliciy conversion is required.

"fmt" module - similar in function to stdio in C.

boilerplate - first line must be "package NAME", with NAME being the starting function of your program.

All functions / variables from imported modules are in capital letters. Non-capital letters are inacessible externally.

statically-typed in the style of TypeScript, but without colons to reduce verbosity.

Permits sequences like in Python to declare multiple items at once, swap, unpack, etc.

# Hello, World

Hello World Program:

```
package main

import "fmt"

func main() {
	fmt.Println("Hello, 世界")
    //Alternative: fmt.Printf("Hello, world!")
}

/* Alternative

*/
```

Import multiple packages with the following syntax:

```
import (
"fmt"
"math"
)
```

# Functions, variables, types

Go is a statically-typed language:

```
func add(x int, y int) int {
	return x + y
}
```

Syntactic sugar is offered for shared types:

```
func add(x, y int) int {
	return x + y
}
```

Go uses types: bool, string, int, uint, byte (alias for uint8), rune (alias for int32), float, complex.

Numerical types can have their sizes specified as well: int8, int16, etc.

Format strings are used in Go, just like C. Documentation [here](https://pkg.go.dev/fmt).

Basics:

%v: Default formatting.

%T: prints the type of the variable.

Variables can be
