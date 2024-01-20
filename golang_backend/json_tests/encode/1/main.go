package main

import (
	"encoding/json"
	"fmt"
)

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

