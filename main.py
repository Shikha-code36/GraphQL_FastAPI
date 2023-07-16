from fastapi import FastAPI
from typing import List
from pymongo import MongoClient
import strawberry
from strawberry.asgi import GraphQL

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["CRUD"]
collection = db["users"]


# Define the User model
@strawberry.type
class User:
    id: int
    name: str


# Define the root resolver
@strawberry.type
class Query:
    @strawberry.field
    def users(self) -> List[User]:
        users = []
        for user_data in collection.find():
            user = User(id=user_data["id"], name=user_data["name"])
            users.append(user)
        return users

    @strawberry.field
    def user(self, id: int) -> User:
        user_data = collection.find_one({"id": id})
        if user_data:
            return User(id=user_data["id"], name=user_data["name"])
        else:
            return None


@strawberry.type
class Mutation:
    @strawberry.mutation
    def create_user(self, name: str) -> User:
        user = {"id": get_next_id(), "name": name}
        collection.insert_one(user)
        return User(id=user["id"], name=user["name"])

    @strawberry.mutation
    def update_user(self, id: int, name: str) -> User:
        collection.update_one({"id": id}, {"$set": {"name": name}})
        updated_user = collection.find_one({"id": id})
        return User(id=updated_user["id"], name=updated_user["name"])

    @strawberry.mutation
    def delete_user(self, id: int) -> User:
        deleted_user = collection.find_one_and_delete({"id": id})
        return User(id=deleted_user["id"], name=deleted_user["name"])


def get_next_id():
    last_user = collection.find_one(sort=[("id", -1)])
    if last_user:
        return last_user["id"] + 1
    else:
        return 1


schema = strawberry.Schema(query=Query, mutation=Mutation)
app.mount("/graphql", GraphQL(schema, debug=True))
