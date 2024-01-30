from fastapi import FastAPI

from wopvault.models import Drawing


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/submit/drawing/{abc}/{symbol}/")
async def submit_drawing(abc: str, symbol: str, drawing: Drawing):
    print(drawing)
    return {"abc": abc, "symbol": symbol, "drawing": drawing}


@app.get("/status/")
async def status():
    return {"status": "ready"}
