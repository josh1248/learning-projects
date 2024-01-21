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

	//db Query is for data-returning queries like SELECT.
	rows, err := db.Query("SELECT * FROM users")
	defer rows.Close()
	if err != nil {
		log.Fatal(err)
	}

	var username string
	var password string
	var admin bool
	var l int

	for rows.Next() {
		err := rows.Scan(&username, &password, &admin, &l)
		if err != nil {
			log.Fatal(err)
		}
		log.Println(username, password, admin, l)
	}

	err = rows.Err()
	if err != nil {
		log.Fatal(err)
	}
}
