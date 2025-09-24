from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def main():
    return {"message":"Hello World!"}

@app.get("/payment")
async def root(authority,status):
    return {"Authority":Authority,"Status":status}
