# cash_register
A transaction logging and tracking application. A zero to hero application on building a transaction logging and management.

## Milestones
- Functional implementation of transaction log input and storage (Data structure)
- Functional implementation and CLI search of transactions based on time parameters
- Refactoring to OOP
- Connecting with MySql Database
- Designing a UI to collect and visualize the inputs (HTML / CSS/ Bootstrap)
- Asynchronous Calls (AJAX with JAvaScript) and Backend Development with Flask (Python)

## Milestone 1
The application at the satged will be developed in python using just functions to collect, validate, store and retrieve input details about the transactions. The choice of data structure is __*List of Dictionaries*__. The information structure is destribed below

```
[
    {
        "customer_name": "james",
        "product": [
            {
                "product_name": "spoon",
                "product_quantity": 20.0,
                "product_price": 12.0
            },
            {
                "product_name": "50",
                "product_quantity": 5.0,
                "product_price": 100.0
            }
            ...another product detail dictionary
        ],
        "time": "10/02/2020 10:57"
    },
    ...another transaction dictionary
]
```

## Milestone 2
The application should be able to collect command line arguments (minimum of 1 and maximum of 4) to search between a range of time and display all the transactions between that time. The command syntax is as follows

`python search.py <start_date> <start_time> <end_date> <end_time>`

The end_date argument is required and the program will search from the beginning up until the end date. The other arguments can be provided in a combination of two to four.

## Milestone 3
The current source code will be refactored to OOP form. Classes will be created to manage the user, the data and so on

## Milestone 4
The application will be connected to a MySql Database to store and manage the data collated. A class will also be created to manage operations like insert, search and retrieve.

## Milestone 5
The user Interface and design will be implement in HTML, CSS and Bootstrap. Pages and Forms will be created to collect and visualize the inputs.

## Milestone 6
The application will be refactored to make asynchronous calls rather than synchronous form submission and reload. JavaScript and AJAX will be implemented for this. Endpoints (API) will be set up in the backend to handle all the calls using __Flask__ module routes.

## Conclusion
This is a practice project to develop a sales register (software) to manage transactions.
