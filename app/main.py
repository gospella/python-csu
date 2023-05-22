from fastapi import FastAPI, Request, Form, HTTPException, Depends
from fastapi.responses import RedirectResponse, FileResponse
from fastapi.templating import Jinja2Templates
from starlette import status

from db.crud import get_last_results
from db.crud import save_result

from dostoevsky.tokenization import RegexTokenizer
from dostoevsky.models import FastTextSocialNetworkModel

app = FastAPI()

templates = Jinja2Templates(directory="src/templates")

tokenizer = RegexTokenizer()
model = FastTextSocialNetworkModel(tokenizer=tokenizer)


@app.get("/")
async def return_index():
    return FileResponse("src/templates/analyze.html")


@app.post('/api/analyze')
def analyze(comment: str):
    results = model.predict([comment], k=2)
    save_result(comment, list(results[0].keys())[0])
    return RedirectResponse(
        '/',
        status_code=status.HTTP_302_FOUND)


@app.get("/api/results")
def get_results(limit: int):
    return get_last_results(limit)
