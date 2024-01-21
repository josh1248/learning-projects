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

	statement, err := db.Prepare("DROP TABLE users")
	if err != nil {
		log.Fatal(err)
	}

	result, err := statement.Exec()
	if err != nil {
		log.Fatal(err)
	} else {
		log.Println(result)
		log.Println("table dropped.")
	}

}
