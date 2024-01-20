package main

import (
	"encoding/json"
	"fmt"
)

type person struct {
	Name    string `json:"first_name"`
	Age     int
	Friends []string `json:"insta_followers"`
}

func main() {
	data := `
	{
		"first_name" : "Josh",
		"age" : 21,
		"insta_followers": [
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
