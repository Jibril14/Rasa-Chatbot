import fastapi
import uvicorn
from app import web_app
from fastapi.staticfiles import StaticFiles
from db import models
from db.database import engine
from fastapi.middleware.cors import CORSMiddleware

app = fastapi.FastAPI()
app.include_router(web_app.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")


models.Base.metadata.create_all(engine)

origins = [
    "http://127.0.0.1:8000/message"
    "http://127.0.0.1:8000",
    "http://127.0.0.1:8000/message",
    "http://localhost:8000",
    "http://localhost:8000/message"
    
]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)