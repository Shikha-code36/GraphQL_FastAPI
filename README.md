# CRUD Operation GraphQL FastAPI with MongoDB

This is a sample project that demonstrates a CRUD operation GraphQL API using FastAPI, MongoDB, and Strawberry.

## Installation

1. Clone the repository:
```
git clone https://github.com/Shikha-code36/GraphQL_FastAPI.git

cd GraphQL_FastAPI
```

2. Create and activate a virtual environment:
```
python3 -m venv venv
source venv/bin/activate # On Linux/MacOS
venv\Scripts\activate.bat # On Windows
```
3. Install dependencies using pip:
```
pip install -r requirements.txt
```

## Usage

1. Make sure your MongoDB server is running on `localhost` at the default port `27017`. You can use your MongoDB server instead of localhost.


2. Start the FastAPI server:
```
uvicorn main:app --reload
```

3. The GraphQL API will be available at `http://localhost:8000/graphql`. You can access this URL in your browser or use tools like Insomnia or GraphQL Playground to interact with the API.

## Test

To run the test cases, use the following command:

```
python -m pytest
```


## Examples

### Create User
To create a new user, send a GraphQL mutation request:

```graphql
mutation {
  createUser(name: "Shikha Pandey") {
    id
    name
  }
}
```
### Update User
To update a user, send a GraphQL mutation request:
```
mutation {
  updateUser(id: 1, name: "Kritika Pandey") {
    id
    name
  }
}
```
### Delete User
To delete a user, send a GraphQL mutation request:
```
mutation {
  deleteUser(id: 1) {
    id
    name
  }
}
```
### Get All Users
To get a list of all users, send a GraphQL query request:
```
query {
  users {
    id
    name
  }
}
```
### Get User by ID
To get a specific user by ID, send a GraphQL query request:
```
query {
  user(id: 1) {
    id
    name
  }
}
```

#### [Note:] Please adjust the URLs, ports, and API endpoints according to your setup.

## License

This project is licensed under the [MIT License](LICENSE).

## Disclaimer

This project is a basic implementation of a graphql and python FastApi for educational purposes. It may not be suitable for production use. Use it at your own risk.

## Contributing

Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.



