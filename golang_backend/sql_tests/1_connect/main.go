package main

import (
	"database/sql"
	"fmt"

	_ "github.com/lib/pq"
)

func main() {
	db, err := sql.Open("postgres", "user=postgres password=Start!123 host=127.0.0.1 port=5432 dbname=postgres sslmode=disable")
	defer db.Close()
	if err != nil {
		panic(err)
	} else {
		fmt.Println("The connection to the DB was successfully initialized!")
		connectivity := db.Ping()
		if connectivity != nil {
			panic(err)
		} else {
			fmt.Println("Good to go!")
		}
	}
}
