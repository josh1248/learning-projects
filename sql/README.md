Brief tutorial on SQL. You can find an implementation of SQL in a language in the Go tutorial [here](https://github.com/josh1248/learning-projects/blob/main/golang_backend/README.md).

# What it is
Structured Query Langage (SQL) is a language specification that allows us to work with relational databases, like in SQLite or PostgreSQL. In a relational database, there can exist multiple tables, which are linked within the database relationally in first-order logic.

# Introduction
Here is a template SQL query to create an empty table with our desired column names and specifications:
```SQL
CREATE TABLE people (
    full_name   VARCHAR(80) PRIMARY KEY,
    age         SMALLINT,
    IC          CHAR(9)     UNIQUE,
    alive       BOOLEAN     FOREIGN KEY
)
```

observe that each column name created can take a specified data type. Each column can also have some specifiers, like the `NOT NULL` constraint that disallows an addition with an empty field at this column, and so on.

# Types
Each column can take on a specified type. Here are some availables types for use, although there are a lot more exotic types like XML or JSON!


|Data Types|Description|
|--|--|
|INT|integer value of 32 bytes. BIGINT for 64 bytes, and SMALLINT|
