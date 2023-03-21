import uuid
import httpx
import uvicorn
from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()


class Task(BaseModel):
    id: uuid.UUID
    status: str
    result: List[int]


class TaskCreateRequest(BaseModel):
    data: List[dict]


tasks = {}


@app.post("/api/v1/tasks/", status_code=201)
async def create_task(request_body: TaskCreateRequest):
    urls = [data['url'] for data in request_body.data]
    task_id = uuid.uuid4()
    tasks[task_id] = Task(id=task_id, status="running", result=[])
    async with httpx.AsyncClient() as client:
        for url in urls:
            try:
                response = await client.get(url)
                tasks[task_id].result.append(response.status_code)
            except:
                tasks[task_id].result.append(-1)
    tasks[task_id].status = "ready"
    return {"task_id": task_id}


@app.get("/api/v1/tasks/{task_id}")
async def get_task(task_id: uuid.UUID):
    if task_id not in tasks:
        return {"detail": "Task not found"}
    return tasks[task_id]


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8888)
