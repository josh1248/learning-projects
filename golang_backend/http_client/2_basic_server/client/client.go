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
