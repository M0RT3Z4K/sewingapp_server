from fastapi import FastAPI

app = FastAPI()


@app.get("/payment")
async def root(authority,status):
    return {"Authority":Authority,"Status":status}
