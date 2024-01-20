Notes for Go regarding relevant concepts for doing a Go backend.
- [JSON and RESTful APIs](#json-and-restful-apis)
- [Built-in support and Frameworks](#built-in-support-and-frameworks)
- [JSON encoding / decoding with encoding/json](#json-encoding--decoding-with-encodingjson)
  - [Decoding](#decoding)
  - [Encoding](#encoding)
- [d](#d)

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

## Decoding

Within `encoding/json`, the `Unmarshall` function is available 

## Encoding

# d