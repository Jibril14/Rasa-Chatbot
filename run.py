import fastapi
import uvicorn
from app import web_app
from fastapi.staticfiles import StaticFiles
from db import models
from db.database import engine

app = fastapi.FastAPI()
app.include_router(web_app.router)

app.mount("/static", StaticFiles(directory="app/static"), name="static")


models.Base.metadata.create_all(engine)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)