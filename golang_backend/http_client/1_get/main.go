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
