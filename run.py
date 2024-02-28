import fastapi
import uvicorn

from app import web_app
from fastapi.staticfiles import StaticFiles

app = fastapi.FastAPI()

app.include_router(web_app.router)

# This is a sub app, must be mounted here, so the root router can handle it. you will get error if mount inside web_app
app.mount("/static", StaticFiles(directory="app/static"), name="static")

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)