import uvicorn


def run_server():
    uvicorn.run("wopvault.api:app")


if __name__ == "__main__":
    run_server()
