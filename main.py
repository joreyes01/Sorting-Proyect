from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class MsgModel(BaseModel):
    msg : str

@app.get("/")
async def root():
    return {"message": "Welcome to the Sorting Proyect"}


@app.get("/randomSort")
async def root():
    return {"message": "Este sera el path para el ordenamiento con input random"}
