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

# Design Choices

No ternary operators (bool ? cons : alt) allowed as a design choice.

Unused operators will be flagged as a compile time error. Silence this by using the \_ variable name, a special variable name that cannot be used whatsoever.

Functions are "first class citizens". Higher order functions are supported.

Function closures are used, referencing variables in the block or function it is declared in.

```
package main

import "fmt"

func adder() func(int) int {
	sum := 0
	return func(x int) int {
		sum += x
		return sum
	}
}

func main() {
	pos, neg := adder(), adder()
	for i := 0; i < 10; i++ {
		fmt.Println(
			pos(i),
			neg(-2*i),
		)
	}
}
```

# Hello, World!

Hello World Program:

```
package main

import "fmt"

func main() {
	fmt.Println("Hello, 世界") //this is print l n, for print line, not print IN.
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

Functions can have named output variables, which can then be used in the function. It is useful as a documentation construct.

Not recommended: a "naked" return statement will return the output variables by default, but is discouraged as it is less readable.

```
func add(x, y int) (z int) {
    z = x + y
    //will return z automatically.
    return
}
```

Anonymous functions (called 'function literals') are supported, but return statements must be stated even for one-liners. I think JS lambda functions are still the most elegant.

```
fmt.Println(func(x int) int {return 3 * x}(10))
quad := func(y int) int {
	return 4 * y
}
fmt.Println(quad(20))
```

# Types

Go uses types: bool, string, int, uint, byte (alias for uint8), rune (alias for int32), float, complex.

Numerical types can have their sizes specified as well: int8, int16, etc.

Format strings are used in Go, just like C, for I/O purposes like in Printf. Documentation [here](https://pkg.go.dev/fmt).

Unless performance is key, use default storage types like int, float, etc. to reduce type conversions required.

Basics:

%v: Default formatting.

%T: prints the type of the variable.

# Variable declarations

Variables used so far have been declared as part of functions.

Other variables can be declared with var, followed by their type.

With an explicit value in declaration, the type can be inferred, and is hence optional.

Without an explicit value, the types must be stated. A default "zero value" depending on type is offered until later modified, e.g. 0 for int and "" for string.

```
var i, j int
var a, b = 12, "xyz"
var balance float64 = 5 //explicit type stated here as balance could be fractional in the future.
```

:= is syntactic sugar for var declarations with explicit values and given types, BUT := can only work within functions.

```
func main() {
	var i, j int = 1, 2
	k := 3 //equivalently, var k = 3
	c, python, java := true, false, "no!"

	fmt.Println(i, j, k, c, python, java)
}
```

You may use brackets, similar to multiple import statements, as an alternative to sequence statements:

```
var i int, j string, k bool = 2, "hi", true
var (
    a int = 4
    b string = "hello"
    c bool = false
)
```

Just like JS, you can use const to declare fixed names. However, all const variables must be computable before runtime.

```
const i = 20
```

Explicit type conversion is required for Go (hence, strongly typed).

int to string conversion is ASCII-based. For example, string(65) gives "A". For atoi / itoa behaviour like in C, see the strconv package for Go.

# Loops and control flow: for, ranges

The only looping construct in Go is the `for` loop, with an initializer, expression, and increment. It works exactly as it does in C.

All fields are optional, which allows Go to represent many kinds of loops differently.

- For a "while" loop: leave only the expression, no semicolons required.
- For an infinite loop: leave all

control flow statements like `break` and `continue` are supported in Go. `break` even supports

# Pointers and structs

structs in Go are analagous to structs in C, and can contain multiple fields which are accessed with the "." operator.

similar to typedef in C, use "type" to provide an alias for structs (or even primitive data types). In Go, specify the alias before the struct, unlike in C where the struct is specified first.

```

```

# Slices

# Higher Order Functions and Closures

# Advanced

Go offers the defer statement, which saves statements into a stack that is executed only when the function ends. Example:

```
func main() {
	fmt.Println("counting")

	for i := 0; i < 10; i++ {
		defer fmt.Println(i)
	}

	fmt.Println("done")
}
```
