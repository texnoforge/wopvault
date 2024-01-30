from fastapi import FastAPI
import uvicorn


app = FastAPI()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.get("/submit/drawing/{abc}/{symbol}")
async def submit_drawing(abc: str, symbol: str):
    return {"abc": abc, "symbol": symbol}


def run_app():
    uvicorn.run("wopvault.server:app")


if __name__ == "__main__":
    run_app()
