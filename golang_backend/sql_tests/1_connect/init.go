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

	create_command := `
		CREATE TABLE users
		(
				username VARCHAR(20) PRIMARY KEY,
				password TEXT,
				is_admin BOOLEAN,
				likes INT
		);
	`

	//1st argument returns number of rows affected and last insert row, but we are not using it for now.
	_, err = db.Exec(create_command)
	if err != nil {
		log.Fatal(err)
	} else {
		log.Println("Table created.")
	}
}
