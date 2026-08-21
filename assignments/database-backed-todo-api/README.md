# 📘 Assignment: Database-Backed To-Do API

## 🎯 Objective

Build a small to-do application backend using FastAPI and SQLite so you can practice CRUD operations, data persistence, and API design.

## 📝 Tasks

### 🛠️ Create the API Skeleton

#### Description
Set up a FastAPI app that serves a simple to-do list with routes for creating, listing, updating, and deleting tasks.

#### Requirements
Completed program should:

- Import `FastAPI` and create an app instance.
- Define a `Task` model with fields such as `id`, `title`, and `completed`.
- Use SQLite or an in-memory database to store tasks persistently across requests.
- Add a simple `GET /tasks` route that returns the stored tasks as JSON.

### 🛠️ Add Task Creation

#### Description
Allow users to add new to-do items to the task list through an API endpoint.

#### Requirements
Completed program should:

- Add a `POST /tasks` endpoint that accepts a task title and optional completion status.
- Validate that the submitted task information is in the expected format.
- Save the new task to the database and return the created task in the response.
- Include a success response status code for a valid request.

### 🛠️ Update and Delete Tasks

#### Description
Expand the API so it can edit existing tasks and remove tasks from the list.

#### Requirements
Completed program should:

- Add a `PUT /tasks/{task_id}` route to update a task's title or completion value.
- Add a `DELETE /tasks/{task_id}` route to remove a task by ID.
- Return a helpful error response when a task ID does not exist.
- Keep the API behavior consistent and easy to test.

### 🛠️ Test Your API

#### Description
Verify that the application behaves correctly by testing the main endpoints.

#### Requirements
Completed program should:

- Test creating a task, retrieving the task list, updating a task, and deleting a task.
- Confirm that invalid requests return an appropriate status code or validation error.
- Write a brief explanation of how each endpoint works and what data it stores.
- Keep the final project organized and readable for other developers.
