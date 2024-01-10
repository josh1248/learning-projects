My notes for Go.

Based on a local copy of "a tour of Go" at https://go.dev/tour/list.

# What Go is

A compiled language that aims to get both efficiency and readability.
Statically typed. offers a dynamic type inference as well.
described as C-like and Python-like in syntax.
It has very quick compilation time compared to other compiled languages.

Advanced: Efficient multi-threading as well.

Runtime: An intermediate, below interpreted languages but above compiled languages.

[t](#basic-syntax)

# Basic Syntax

Automatically runs the function main, like C.

"fmt" module - similar in function to stdio in C.

boilerplate - first line must be "package NAME", with NAME being the starting function of your program.

All functions / variables from imported modules are in capital letters. Non-capital letters are inacessible externally.

Hello World Program:

````
package main

import "fmt"

func main() {
	fmt.Println("Hello, 世界")
}
```'

Import multiple packages with the following syntax:
````

import (
"fmt"
"math"
)

```

```
