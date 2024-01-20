Notes for Go regarding relevant concepts for doing a Go backend.
- [JSON and RESTful APIs](#json-and-restful-apis)
- [Built-in support and Frameworks](#built-in-support-and-frameworks)
- [JSON encoding / decoding with encoding/json](#json-encoding--decoding-with-encodingjson)
  - [Decoding (Fixed)](#decoding-fixed)
  - [Decoding (Dynamic)](#decoding-dynamic)
  - [Encoding](#encoding)
  - [Alternatives](#alternatives)
- [SQL Database Communication (in PostgreSQL)](#sql-database-communication-in-postgresql)

# JSON and RESTful APIs

An application interface (API) is a way for components of our website to communicate with one another, in this case the frontend fetching data from the backend, without having to know the implementations of one another. In most APIs today, APIs return their data in JavaScript Object Notation (JSON). An Object in JavaScript is a collection of key-value pairs, and is the equivalent of a dict in Python. Within JSON, all key values are strings, but values can be any type, including arrays and objects.

```JavaScript
{
    "status": 200,
    "person": {
        "name": "Josh",
        "age": 21
    },
    "friends": [
        "Shew",
        "Xu",
        "Tan"
    ],
    "employed": false,
    "car": null
}
```

A RESTful (Representional State Architecture) API follows several rules and specifications of its output that allow for widespread use of some API.

# Built-in support and Frameworks

Go offers rich innate support for backend matters like JSON processing and database communications. Frameworks like `go-chi` and `gin` are of course available to make backend development even easier.

# JSON encoding / decoding with encoding/json

The built-in package, `encoding/json`, contains functions to translate Go data into JSON, and vice-versa.

## Decoding (Fixed)

Decoding converts JSON data into data useable in Golang, typically in structs.

The first thing you should do is to ensure that your data is actually in JSON format. Use the `Valid` function to ensure this. Note that this function can only accept a byte array, so ensure that it is converted first.
```Go
/*boilerplate here*/

func main() {
    wrong_data := `
        {
            "nums": 33,
            types: null
        }
    `
    
    if !json.Valid([]byte(wrong_data)) {
        fmt.Printf("invalid.")
        os.Exit(1)
    } else {
        //process json here
    }
}
```

**NOTE**: recall that Go separates private/public functionality using capitalization. Other packages can only access capitalized fields within your code, and vice versa.


Within `encoding/json`, the `Unmarshall` function is available that decodes a string representing JSON into useable data in Go.
The `Unmarshall` function has the following signature:

```Go
func Unmarshal(data []byte, v any) error
```

The function writes JSON data read from a byte array into our struct using a pointer. It emits an error when parsing issues occur, which need to be explicitly checked for. [example use below:](json_tests/decode/1/main.go)

```Go
type person struct {
	Name    string
	Age     int
	Friends []string
}

func main() {
	data := `
	{
		"name" : "Josh",
		"age" : 21,
		"friends": [
			"Shew",
			"Xu",
			"Tan"
		]
	}
	`
	var p person
	err := json.Unmarshal([]byte(data), &p)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Println(p.Friends)
}
```
The function writes to fields that directly match the capitalized string in JSON. This can be a problem if the JSON input is as follows, but we want it to correspond regardless:
```JavaScript
{
    "first_name" : "Josh",
    "age" : 21,
    "insta_followers": [
        "Shew",
        "Xu",
        "Tan"
    ]
}
```

We can overwrite this behaviour using struct field tags in Go. Field tags are a kind of metainfo in Go associated in each field that gives more information about them. The example code below will help to adjust the decoding within the `Unmarshal` function.

```Go
type person struct {
	Name    string `json:"first_name"`
	Age     int
	Friends []string `json:"insta_followers"`
}
```

**NOTE**: ensure that your metatag contains no spaces for proper parsing.

## Decoding (Dynamic)

You can instead opt for a "dynamic struct" setup in Go using an empty interface.
```Go
var v interface{}
```

With an empty interface, `Unmarshal` will populate the output with key value pairs in a map with the following signature:
```Go
map[string]interface{}
```
This allows Go to decode JSON with varying keys and value types.

## Encoding

APIs typically return data to the caller, like a frontend, using an API in JSON format. The process of encoding Go data into JSON is done using the `Marshal` function, with the following signature:

```Go
//any is an alias for interface{}
func Marshal(v any) ([]byte, error) 
```

`Marshal` expects some filled struct as an input, and it will output the JSON equivalent plus an error message.

The output will use the name of the field as the key, and the data as the values. You may override this default behaviour by using a metatag to customize the output JSON as needed.

```Go
package main

import (
	"encoding/json"
	"fmt"
)

type person struct {
	Name    string
	Age     int
	Friends []string `json:"people"`
}

func main() {
	p := person{"Josh", 21, []string{"Shew", "Xu", "Tan"}}
	json, err := json.Marshal(p)
	if err != nil {
		fmt.Println(err)
	}
	fmt.Printf("%s", json)
}
```

Other customizations include:
- You can choose to hide your struct from being encoded into JSON using "-".
- You can choose to hide your struct if it is empty using `omitempty`, but it must be on the 2nd field of the metatag.
  ```Go
    type person struct {
	Name    string      `json:",omitempty"`
	Age     int         `json:"-"`
	Friends []string    `json:"people,omitempty"`
    }
  ``` 

For more complex JSONs that you wish to visualize, you may use the `MarshalIndent` function, which performs the role of `Marshal` but also applies a new line to different fields, along with a specified prefix and indent.
```Go
func MarshalIndent(v any, prefix, indent string) ([]byte, error)
```
## Alternatives

You may use `encoding/gob` if all decoding and encoding will be run in Go programs. It sacrifices some language-agnostic behaviour for speed and efficiency.


# SQL Database Communication (in PostgreSQL)

Go offers innate database communication using the `database/sql` module. It does so by offering SQL queries that run on any database, once set up.

You can (and should) communicate with your database language of choice through `database/sql` as an interface, with the 3rd party drivers doing the implementation.

The tutorial offered in the book uses the PostgreSQL driver as it offers a pure Go driver implementation at https://www.github.com/lib/pq but other drivers are also available (see fill list at https://go.dev/wiki/SQLDrivers)