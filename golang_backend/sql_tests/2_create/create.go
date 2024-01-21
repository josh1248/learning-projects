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

	//Prepare helps to establish a SQL statement in advance.
	//Compared to Sprintf, It is superior in terms of execution speed and security (it lowers the risk of SQL injection.),
	//as well as supporting quick concurrent use in golang.

	//insert is of type *sql.Stmt, for your interest.
	statement, err := db.Prepare("INSERT INTO users VALUES ($1, $2, $3, $4)")
	if err != nil {
		log.Fatal(err)
	}

	//Exec is an overloaded function that can perform different tasks in a *sql.Stmt and *sql.DB.
	//first value returns number of rows affected and last insert row, similar to that in sql.DB's Exec.
	_, err = statement.Exec("Timmy Jimmy Limmy Ki", "letmein", false, 15)
	if err != nil {
		log.Fatal(err)
	} else {
		log.Println("inserted username")
	}

}
