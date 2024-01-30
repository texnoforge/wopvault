from fastapi import FastAPI


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/submit/drawing/{abc}/{symbol}")
async def submit_drawing(abc: str, symbol: str):
    return {"abc": abc, "symbol": symbol}
