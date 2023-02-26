from fastapi import FastAPI, Form
import requests as r
import json
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

link = "https://data.rcsb.org/rest/v1/core/entry/"

@app.post("/req")
async def login(data: str = Form(...)):
    resp = json.loads(r.get(link + data).text)
    
    return resp
