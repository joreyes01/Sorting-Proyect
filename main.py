from fastapi import FastAPI
from pydantic import BaseModel
from mainSorting import apiMessagge

app = FastAPI()
message = apiMessagge

class MsgModel(BaseModel):
    msg : str

@app.get("/")
async def root():

    message2 = 'Prueba message2'
    return { "message" : message}


@app.get("/randomSort")
async def root():
    return {"message": "Este sera el path para el ordenamiento con input random 2"}
