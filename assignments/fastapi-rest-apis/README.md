# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a small REST API using FastAPI to practice routing, JSON responses, request validation, and API design fundamentals.

## 📝 Tasks

### 🛠️ Set Up the FastAPI App

#### Description
Create a new FastAPI application and add a root endpoint that returns a simple message when the server starts.

#### Requirements
Completed program should:

- Import `FastAPI` and create an application instance.
- Define a `GET` route at `/` that returns a JSON message such as `{"message": "Welcome to the API"}`.
- Start the app using `uvicorn` so it can be accessed in a browser or with a client.
- Confirm the endpoint returns the expected JSON response.

### 🛠️ Build a Resource API

#### Description
Create an API for managing a simple collection of items, such as books, products, or tasks.

#### Requirements
Completed program should:

- Define a `Pydantic` model for an item with at least a name and a description.
- Add a `GET /items` endpoint that returns the current list of items.
- Add a `POST /items` endpoint that accepts a new item and returns it with a success response.
- Validate incoming data so invalid requests are rejected cleanly.
- Use JSON responses with clear, easy-to-read data.

### 🛠️ Add a Detail Endpoint

#### Description
Extend the API so it can return a single item by its ID and update the item list in a more realistic REST style.

#### Requirements
Completed program should:

- Add a `GET /items/{item_id}` route that returns one item.
- Add a `PUT` or `PATCH` route to update an existing item.
- Return a helpful error response if the requested item does not exist.
- Keep the API simple, organized, and easy for another developer to follow.

### 🛠️ Practice API Testing

#### Description
Test the API behavior to make sure the endpoints work as expected.

#### Requirements
Completed program should:

- Use FastAPI’s built-in test client or another simple test method to call the API endpoints.
- Verify that `GET`, `POST`, and update requests return the expected status codes.
- Check that invalid payloads are rejected during validation.
- Write a short summary explaining how the app behaves and what each endpoint does.
