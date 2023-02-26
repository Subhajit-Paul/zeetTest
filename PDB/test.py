from fastapi import FastAPI
import sys, os
from duckduckgo_images_api import search
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.post("/req")
async def login(data: str):
    sys.stdout = open(os.devnull, 'w')
    results = search(data)
    return {"image": [i["image"] for i in results["results"]], "thumbnail": [i["thumbnail"] for i in results["results"]]}
