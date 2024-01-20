package main

import (
	"encoding/json"
	"fmt"
)

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
