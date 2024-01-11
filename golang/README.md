My notes for Go.

Based on https://go.dev/tour/list, cross referenced with https://www.youtube.com/watch?v=un6ZyFkqFKo.

- [What Go is](#what-go-is)
- [Comparison to C and Python](#comparison-to-c-and-python)
- [Design Choices](#design-choices)
- [Hello, World!](#hello-world)
- [Functions](#functions)
- [Types](#types)
- [Variable declarations](#variable-declarations)
- [Loops and control flow](#loops-and-control-flow)
- [structs](#structs)
- [Pointers](#pointers)
- [Slices](#slices)
- [Higher Order Functions and Closures](#higher-order-functions-and-closures)
- [Advanced: Defer / Panic / Recover](#advanced-defer--panic--recover)
- [Advanced: Concurrency, Goroutines, chan](#advanced-concurrency-goroutines-chan)
  
(generated with Markdown All In One in VSCode)

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

"fmt" module - similar in function to stdio in C.- [What Go is](#what-go-is)



boilerplate - first line must be "package NAME", with NAME being the starting function of your program.

All functions / variables from imported modules are in capital letters. Non-capital letters are inacessible externally.

statically-typed in the style of TypeScript, but without colons to reduce verbosity.

Permits sequences like in Python to declare multiple items at once, swap, unpack, etc.

# Design Choices

No ternary operators (bool ? cons : alt) allowed as a design choice.

Unused operators will be flagged as a compile time error. Silence this by using the \_ variable name, a special variable name that cannot be used whatsoever.

Functions are "first class citizens". Higher order functions are supported.

Function closures are used, referencing variables in the block or function it is declared in.

```Go
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

```Go
package main

import "fmt"

func main() {
	fmt.Println("Hello, 世界") //this is print l n, for print line, not print IN.
    //Alternative: fmt.Printf("Hello, world!")
}
```

Import multiple packages with the following syntax. In fact, you can use this syntax for repeated uses of *any* keyword, like var.

```Go
import (
"fmt"
"math"
)
```

# Functions

Go is a statically-typed language, with TypeScript-like syntax without colons.

```Go
func add(x int, y int) int {
	return x + y
}
```

Syntactic sugar is offered for shared types:

```Go
func add(x, y int) int {
	return x + y
}
```

Functions can return multiple items:

```Go
func swap(x, y string) (string, string) {
	return y, x
}
```

Functions can have named output variables, which can then be used in the function. It is useful as a documentation construct.

Not recommended: a "naked" return statement will return the output variables by default, but is discouraged as it is less readable.

```Go
func add(x, y int) (z int) {
    z = x + y
    //will return z automatically.
    return
}
```

Anonymous functions (called 'function literals') are supported, but return statements must be stated even for one-liners. I think JS lambda functions are still the most elegant.

```Go
fmt.Println(func(x int) int {return 3 * x}(10))
quad := func(y int) int {
	return 4 * y
}
fmt.Println(quad(20))
```

Higher order functions are supported in Go.
```Go
func apply_twice(fn func(float64) float64) func(float64) float64 {
	return func(num float64) float64 {
		return fn(fn(num))
	}
}

func double(x float64) float64 {return 2 * x}

func main() {
	fmt.Println(apply_twice(double)(7)) //returns 28
}
```


Functions reference variables starting from the environment they are created in. This is called a closure like in JS: https://developer.mozilla.org/en-US/docs/Web/JavaScript/Closures. Recall the Environment model in CS1101S. 

```Go
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

Notice that in the code above, any time the `adder` function is called, a new block instance is created, which the returned function can access. Hence, the variable `sum` in the 2 adders exist in their separate instances.

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

```Go
var i, j int
var a, b = 12, "xyz"
var balance float64 = 5 //explicit type stated here as balance could be fractional in the future.
```

:= is syntactic sugar for var declarations with explicit values and given types, BUT := can only work within functions.

```Go
func main() {
	var i, j int = 1, 2
	k := 3 //equivalently, var k = 3
	c, python, java := true, false, "no!"

	fmt.Println(i, j, k, c, python, java)
}
```

You may use brackets, similar to multiple import statements, as an alternative to sequence statements:

```Go
var i int, j string, k bool = 2, "hi", true
var (
    a int = 4
    b string = "hello"
    c bool = false
)
```

Just like JS, you can use const to declare fixed names. However, all const variables must be computable before runtime.

```Go
const i = 20
```

Explicit type conversion is required for Go (hence, strongly typed).

int to string conversion is ASCII-based. For example, string(65) gives "A". For atoi / itoa behaviour like in C, see the strconv package for Go.

# Loops and control flow

`if-else` functionality is similarly supported in C, but additionally offers an initializer statement as syntactic sugar. Similar to the initializer in `for` loops, it can help to reduce namespace pollution outside of the loop it is used in.
```
func pow(x, n, lim float64) float64 {
	if v := math.Pow(x, n); v < lim {
		return v
	}
	return lim
}
```

The **only** looping construct in Go is the `for` loop, with an initializer, expression, and increment. It combines all looping functionalities in both C and Python.

All fields are optional, which allows Go to represent many kinds of loops differently.

- Typical C `for` loop: fill in all fields.
- `while` loop: leave only the expression, no semicolons required.
- For an infinite loop: leave all fields blank.
- C `do-while` loop: no equivalents, can be emulated using the construct `for next := true; next; next=<condition>`
- Python `for` loop over sequence data types are offered as well.

```Go
//1: Typical 'for' loop
sum := 0
for i := 0; i < 10; i++ {
	sum += i
}

//2: 'while' loop
sum := 1
for sum < 1000 {
	sum += sum
}
fmt.Println(sum)

//3: infinite loop
for {
	//do something
}

//4: do-while loop
i := 0
for next := true; true; next = i < 10 {
	i += i
}

//5: Range over a sequence, like a slice or map. returns the index of the element and the element itself, akin to enumerate() in Python. If not used, use the _ variable name to silence compile time errors.

var pow = []int{1, 2, 4, 8, 16, 32, 64, 128}

func main() {
	for i, v := range pow {
		fmt.Printf("2\*\*%d = %d\n", i, v)
	}

	for _, value := range pow {
		fmt.Printf("%d\n", value)
	}

	//uses the index only.
	for i := range pow {
		pow[i] = 1 << uint(i) // == 2**i
	}
}
```

control flow statements like `break` and `continue` are supported in Go. `break` even supports goto-like constructs.

# structs

structs in Go are analagous to structs in C, and can contain multiple fields which are accessed with the "." operator.

similar to typedef in C, use "type" to provide an alias for structs (or even primitive data types). In Go, the alias comes before the struct, unlike in C where the struct is specified first.

structs can be created with positional or named inputs ('struct literals'). Positional creation must specify all fields. Omitted fields in named creation will be given their default zero values.

```Go
type Vertex struct {
	X, Y int
}

var (
	v1 = Vertex{1, 2}  // has type Vertex
	v2 = Vertex{X: 1}  // Y:0 is implicit
	v3 = Vertex{}      // X:0 and Y:0
	p  = &Vertex{1, 2} // has type *Vertex
)
```

# Pointers

Go has pointers like C. The `&` operator obtains the address of a value, and `*` is used as a dereference operator to obtain the value from a location. The zero value of pointers is `nil`.

Pointers are their own data types. Just like in C, the `*` operator is overloaded to represent the data type: `*int` is a type that is pointer to a value of type `int`.

Locations of custom structs, e.g. a Vertex, will simply be `&{1, 2}` (without change to the String() interface - more on that later.)

However, no pointer arithmetic is allowed in Go.

```Go
i, j := 42, 2701

p := &i         // point to i
fmt.Println(*p) // read i through the pointer
*p = 21         // set i through the pointer
fmt.Println(i)  // see the new value of i

p = &j         // point to j
*p = *p / 37   // divide j through the pointer
fmt.Println(j) // see the new value of j
```

The `.` operator in Go is overloaded. If it is applied on a struct value, it accesses the field directly. If it is applied on a pointer to a struct, it will dereference before accessing the field.

```Go
type Vertex struct {
	X int
	Y int
}

func main() {
	v := Vertex{1, 2}
	p := &v
	p.X = 1e9 // (*p).X, or p->X in C, not needed.
	fmt.Println(v)
}
```

# Slices

# Higher Order Functions and Closures

# Advanced: Defer / Panic / Recover

Go offers the defer statement, which saves statements into a stack that is executed only when the function ends. Example:

```Go
func main() {
fmt.Println("counting")

    for i := 0; i < 10; i++ {
    	defer fmt.Println(i)
    }

    fmt.Println("done")
}
```
it is used as an alternative for error handling when used with the `panic` and `recover` constructs.

# Advanced: Concurrency, Goroutines, chan
