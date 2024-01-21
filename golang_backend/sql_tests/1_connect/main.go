package main

import (
	"database/sql"
	"fmt"

	_ "github.com/lib/pq"
)

func main() {
	db, err := sql.Open("postgres", "user=testuser password=he11oworld! host=127.0.0.1 port=5432 dbname=postgres sslmode=disable")
	defer db.Close()
	if err != nil {
		panic(err)
	}
	fmt.Println("The connection to the DB was successfully initialized!")
	create_test := `
		CREATE TABLE example_table (
			name VARCHAR(50),
			age INT,
			alive BOOLEAN
		)
	`
	_, err = db.Exec(create_test)
	if err != nil {
		panic(err)
	}

	fmt.Println("Table created successfully")
}
