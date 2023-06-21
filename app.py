from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from routes.jokes import router as jokes_router
import random

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
app.include_router(jokes_router)


# Joke generator
@app.get("/", response_class=HTMLResponse)
async def read_item():
    return FileResponse("static/index.html")
