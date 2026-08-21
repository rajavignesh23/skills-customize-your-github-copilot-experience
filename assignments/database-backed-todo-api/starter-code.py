from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import sqlite3

app = FastAPI()


class TaskBase(BaseModel):
    title: str
    completed: bool = False


class Task(TaskBase):
    id: int


def get_db_connection():
    conn = sqlite3.connect("tasks.db")
    conn.row_factory = sqlite3.Row
    return conn


@app.on_event("startup")
def startup():
    conn = get_db_connection()
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            completed BOOLEAN NOT NULL DEFAULT 0
        )
        """
    )
    conn.commit()
    conn.close()


# TODO: Add GET /tasks
# TODO: Add POST /tasks
# TODO: Add PUT /tasks/{task_id}
# TODO: Add DELETE /tasks/{task_id}
