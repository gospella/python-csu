from fastapi import FastAPI, Request, Form, HTTPException, Depends
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from src.models import *
from db.crud import check_user_auth
from db.session import get_db

app = FastAPI()

templates = Jinja2Templates(directory="src/templates")


@app.get("/")
async def return_index():
    return RedirectResponse("/login")


@app.get("/login")
async def return_index():
    return FileResponse("src/templates/login.html")


@app.post("/form/")
async def login(
    request: Request,
    username: str = Form(),
    password: str = Form(),
    db: Session = Depends(get_db),
):
    user = check_user_auth(db, username, password)
    if not user:
        raise HTTPException(status_code=403, detail="Incorrect login or password")

    return templates.TemplateResponse(
        "main.html", {"request": request, "name": user.name}
    )
