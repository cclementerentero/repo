from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def read_root():
    return {"message": "Welcome to my API!"}
# @copilot: create a Pydantic model for the request body with a field called "text"
