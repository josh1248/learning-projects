My notes for Go.

Based on https://go.dev/tour/list, cross referenced with https://www.youtube.com/watch?v=un6ZyFkqFKo.

# What Go is

A compiled language that aims to get both efficiency and readability.
Statically typed. offers type inference as well.
described as C-like and Python-like in syntax.
It has very quick compilation time compared to other compiled languages.

Advanced: Efficient multi-threading as well.

Runtime: An intermediate, below interpreted languages but above compiled languages as it uses Go runtime to ensure memory safety, garbage collection etc.

# Comparison to C and Python

Automatically runs the function main, like C.

strongly typed, unlike C. Explicit conversion is required.

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

# Functions

Go is a statically-typed language, with TypeScript-like syntax without colons.

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

Functions can return multiple items:

```
func swap(x, y string) (string, string) {
	return y, x
}
```

Functions can have named output variables, which can then be used in the function.

Go uses types: bool, string, int, uint, byte (alias for uint8), rune (alias for int32), float, complex.

Numerical types can have their sizes specified as well: int8, int16, etc.

Format strings are used in Go, just like C. Documentation [here](https://pkg.go.dev/fmt).

Basics:

%v: Default formatting.

%T: prints the type of the variable.

Variables are declared with var, followed by their type.

With an explicit value in declaration, the type can be inferred.

Without an explicit value, the types must be stated. A default "zero value" depending on type is offered until later modified, e.g. 0 for int and "" for string.

```
var i, j int
var a, b = 12, "xyz"
fmt.Printf("%T %T %T %T", i, j, a, b)
```
