from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse, FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from routes.jokes import router as jokes_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")
app.include_router(jokes_router)

app = FastAPI()


@app.get('/')
def home():
    return "hello world"

