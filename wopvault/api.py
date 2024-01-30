from fastapi import FastAPI, HTTPException

from wopvault.models import Drawing
from wopvault import __version__
from wopvault.common import get_vault_from_config
from wopvault import ex


vault = get_vault_from_config()


app = FastAPI(
    title='Words of Power Vault',
    version=__version__,
)


@app.get("/")
async def read_root():
    return {"Hello": "World"}


@app.post("/submit/drawing/{abc}/{symbol}/")
async def submit_drawing(abc: str, symbol: str, drawing: Drawing,
                         tag: str | None = None):
    try:
        vault.save_drawing(abc, symbol, drawing, tag=tag)
    except ex.AlphabetNotFound as e:
        raise HTTPException(e.statuscode, detail=f"Invalid alphabet: {abc}")
    except ex.SymbolNotFound as e:
        raise HTTPException(e.statuscode, detail=f"Invalid symbol: {symbol}")
    except ex.TagNotFound as e:
        raise HTTPException(e.statuscode, detail=f"Invalid tag: {tag}")
    except ex.PayloadTooSmall as e:
        raise HTTPException(e.statuscode,
            detail=f"Drawing too small: {e.args[0]} points (min: {e.args[1]})")
    except ex.PayloadTooLarge as e:
        raise HTTPException(e.statuscode,
            detail=f"Drawing too big: {e.args[0]} points (max: {e.args[1]})")

    return {"status": "ok", "abc": abc, "symbol": symbol}


@app.get("/status/")
async def status():
    return {"status": "ready"}
