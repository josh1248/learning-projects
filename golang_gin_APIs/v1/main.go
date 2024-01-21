package main

import (
	"errors"
	"fmt"
	"net/http"

	"github.com/gin-gonic/gin"
)

type book struct {
	ID       string `json:"id"`
	Title    string `json:"title"`
	Author   string `json:"author"`
	Quantity int    `json:"qty"`
}

var books []book = []book{
	{ID: "1", Title: "aardvark", Author: "Anne", Quantity: 5},
	{ID: "2", Title: "bees bees bees", Author: "Benny", Quantity: 14},
	{ID: "3", Title: "croissant", Author: "Colin", Quantity: 0},
}

func getBooks(c *gin.Context) {
	c.IndentedJSON(http.StatusOK, books)
}

func bookByID(c *gin.Context) {
	id := c.Param("id")
	book, err := getBookByID(id)

	if err != nil {
		c.IndentedJSON(http.StatusNotFound, gin.H{"message": "Book not found."})
		return
	}

	c.IndentedJSON(http.StatusOK, book)
}

func getBookByID(id string) (*book, error) {
	for i, book := range books {
		if book.ID == id {
			return &books[i], nil
		}
	}

	return nil, errors.New("book not found")
}

func createBook(c *gin.Context) {
	var new_book book
	if err := c.BindJSON(&new_book); err != nil {
		return
	}

	books = append(books, new_book)
	c.IndentedJSON(http.StatusCreated, new_book)
}

/*
query parameters method, but this is not RESTful?
func checkoutBook(c *gin.Context) {
	id, ok := c.GetQuery("id")

	if !ok {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"message": "No ID query"})
		return
	}

	book, err := getBookByID(id)
	if err != nil {
		c.IndentedJSON(http.StatusNotFound, gin.H{"message": "Book not found."})
		return
	}

	if book.Quantity == 0 {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"message": "out of stock."})
		return
	}

	book.Quantity -= 1
	c.IndentedJSON(http.StatusOK, book)
}*/

func checkoutBook(c *gin.Context) {
	id := c.Param("id")

	book, err := getBookByID(id)
	if err != nil {
		c.IndentedJSON(http.StatusNotFound, gin.H{"message": "Book not found."})
		return
	}

	if book.Quantity == 0 {
		c.IndentedJSON(http.StatusBadRequest, gin.H{"message": "out of stock."})
		return
	}

	book.Quantity -= 1
	c.IndentedJSON(http.StatusOK, book)
}

func returnBook(c *gin.Context) {
	id := c.Param("id")

	book, err := getBookByID(id)
	if err != nil {
		c.IndentedJSON(http.StatusNotFound, gin.H{"message": "Book not found."})
		return
	}

	book.Quantity += 1
	c.IndentedJSON(http.StatusOK, book)
}

func main() {
	router := gin.Default()
	router.GET("/books", getBooks)
	router.GET("/books/:id", bookByID)
	router.POST("/new", createBook)
	router.PATCH("/checkout/:id", checkoutBook)
	router.PATCH("/return/:id", returnBook)
	router.Run("localhost:8080")
	fmt.Println("Hello world!")
}
