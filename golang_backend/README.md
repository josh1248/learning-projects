Notes for Go regarding relevant concepts for doing a Go backend.
- [JSON and RESTful APIs](#json-and-restful-apis)
- [Built-in support and Frameworks](#built-in-support-and-frameworks)
- [JSON encoding / decoding with encoding/json](#json-encoding--decoding-with-encodingjson)
	- [Decoding (Fixed)](#decoding-fixed)
	- [Decoding (Dynamic)](#decoding-dynamic)
	- [Encoding](#encoding)
	- [Alternatives](#alternatives)
- [SQL Database Communication (in PostgreSQL)](#sql-database-communication-in-postgresql)
	- [Setup](#setup)
	- [Establishing a connection](#establishing-a-connection)
	- [Creating (Inserting) Data](#creating-inserting-data)
- [HTTP Client and Servers with net/http](#http-client-and-servers-with-nethttp)
	- [Read data with GET requests](#read-data-with-get-requests)
	- [Send data with POST](#send-data-with-post)

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

SQL tutorial [here.](https://github.com/josh1248/learning-projects/blob/main/sql/README.md)

Go offers innate database communication using the `database/sql` module. It does so by offering SQL queries that run on any database, once set up.

You can (and should) communicate with your database language of choice through `database/sql` as an interface, with the 3rd party drivers doing the implementation.

The tutorial offered in the book uses the PostgreSQL driver as it offers a pure Go driver implementation at https://www.github.com/lib/pq but other drivers are also available (see fill list at https://go.dev/wiki/SQLDrivers)

The relevant import statements are:

```Go
import (
    "database/sql"
    _ "github.com/lib/pq"
)
```

**NOTE**: _ is an applied alias that silences the Go compiler's complaint that a package is imported but never used. This is because our imported package for Postgres is meant to invoke its side effects in `init()` even though we wont call any of its functions.


I used the Postgres app (Universal version 16) and pgAdmin 4 for this task. Within the Postgres app, I used the default `127.0.0.1` localhost on port `5432`. I have also decided to stick with the default `postgres` superuser to create a database with a password of choice (I set a dummy password here for demonstration.)

The built-in `database/sql` package allows us to directly liaise with our database via the 3rd party driver. We can perform the crucial Create, Read, Update, and Delete (CRUD) functionalities with our database in persistent memory.

## Setup

We will create the following folder and files:
```
sql_tests
 ┣ 1_connect
 ┃ ┗ init.go
 ┣ 2_create
 ┃ ┗ create.go
 ┣ 3_read
 ┃ ┗ read.go
 ┣ 4_update
 ┃ ┗ update.go
 ┗ 5_delete
 ┃ ┗ delete.go
```
Within each separate file, we will run `go mod init <filename>` then `go mod tidy` to initialize their `go.mod` and `go.sum` files, which help to download the dependencies when building our executable.

Note that this set-up is not designed with a project in mind and is simply a learning directory. A multi-directory Go project that is on GitHub should use the go Modules functionality (which works best on version control sites like GitHub).

## Establishing a connection

We shall work on this in the `1_connect` folder.

First, the `Open` function allows us to establish a connection with our credentials. Our credentials must be that of a superuser with permission to create a new database. In this case, I will use the `postgres` superuser I have set up.

```Go
package main

import (
	"database/sql"
	"log"

	_ "github.com/lib/pq"
)

func main() {
	credentials := `
		user=postgres
		password=xddd
		host=127.0.0.1
		port=5432
		dbname=postgres
		sslmode=disable
	`
	db, err := sql.Open("postgres", credentials)
	defer db.Close()
	if err != nil {
		log.Fatal(err)
	} else {
		log.Println("Driver opened.")
	}

	if check := db.Ping(); check != nil {
		log.Fatal(check)
	} else {
		log.Println("Connection to database established.")
	}

	//...
}
```

The `db` variable represents our database connection, which the `Open` function sets up. The `Ping` function is an additional test that verifies that the database connection is present.

Enter this folder and run `go mod init init.go` and `go mod tidy`. You can then compile with `go build init.go` or run directly with `go run init.go`.

You should receive success logs at this point. Otherwise, ensure that your credentials like your password, local host, and port are set correctly (check your postgres app).

After checking that you can connect with the database, add a command to create a table within the database, then use the `Exec` method to run that SQL query.

```Go
...
	//1st argument returns number of rows affected and last insert row, but we are not using it for now.
	_, err = db.Exec(create_command)
	if err != nil {
		log.Fatal(err)
	} else {
		log.Println("Table created.")
	}

```

this completes the `init.go` file. Re-run `init.go` with the new code, and you should receive a 3rd log this time that declares that your table was created. **Crucially**, if you then run `init.go` once again, you will receive the error that your table has been created:
```
pq: relation "users" already exists
```

## Creating (Inserting) Data




# HTTP Client and Servers with net/http
`net/http` provides innate support for sending requests like GET or POST to a HTTP server to obtain data.

## Read data with GET requests


Here is example code to obtain data from a HTTP server. We obtain it as a string that represents some JSON. Advanced HTTP clients like Firefox convert them into readable items. This is available in the test repository [here](http_client/1_get/main.go)

```Go
package main

import (
	"io"
	"log"
	"net/http"
)

func getData(target string) string {
	//1: GET request
	r, err := http.Get(target)
	if err != nil {
		log.Fatal(err)
	}
	defer r.Body.Close()

	//2: receive data
	data, err := io.ReadAll(r.Body)
	if err != nil {
		log.Fatal(err)
	}

	//3: return data
	return string(data)
}

func main() {
	data := getData("https://www.google.com")
	//In HTTP clients like Firefox or Chrome, this is formatted into an interactive webpage.
	log.Println(data)
}
```

Now, lets make a rudimentary HTTP server-client pair that passes around a fake JSON string.

```
2_basic_server
 ┣ client
 ┃ ┗ client.go
 ┗ server
 ┃ ┗ server.go
```
*This file structure representation was generated using the file-tree-generator extension in VSCode, which you can find at https://marketplace.visualstudio.com/items?itemName=Shinotatwu-DS.file-tree-generator*

For our server, we define the following string that represents JSON to be returned:
```Go
package main

import (
	"log"
	"net/http"
)

type server struct{}

func (srv server) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	msg := `{"message": "hello world!", "knowledge" : 42}`
	w.Write([]byte(msg))
}

func main() {
	log.Fatal(http.ListenAndServe(":8080", server{}))
}
```

Since our string is a valid JSON format, we can use `Unmarshal` to decode it as though it was JSON. Since we know in advance what JSON we are getting, let's adjust our client to process and decode the expected output from the server:
```Go
package main

import (
	"encoding/json"
	"io"
	"log"
	"net/http"
)

type messageData struct {
	Message string `json:"message"`
	Number  int    `json:"knowledge"`
}

func getData(target string) messageData {
	//1: GET request
	r, err := http.Get(target)
	if err != nil {
		log.Fatal(err)
	}
	defer r.Body.Close()

	//2: receive data
	data, err := io.ReadAll(r.Body)
	if err != nil {
		log.Fatal(err)
	}

	//3: process data
	message := messageData{}
	err = json.Unmarshal(data, &message)
	if err != nil {
		log.Fatal(err)
	}

	//4: return data
	return message
}

func main() {
	data := getData("http://localhost:8080")
	//In HTTP clients like Firefox or Chrome, this is formatted into an interactive webpage.
	log.Println(data)
}
```

To check that this works, go to each separate `server` and `client` directory and run `go run server.go` and `go run client.go` respectively. You will need to open up 2 clients to make this work. Volia!

## Send data with POST
