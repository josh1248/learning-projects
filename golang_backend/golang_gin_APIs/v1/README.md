Adapted from a Go-gin API tutorial at https://www.youtube.com/watch?v=bj77B59nkTQ.

Rudimentary non-db API with Create, Read, Update capabilities.

Example curl queries to test:

```
curl localhost:8080/books --request "GET"
curl localhost:8080/new --include --header "Content-Type: application/json" -d #payload.json --request "POST"
curl localhost:8080/checkout/2 --request "PATCH"
```