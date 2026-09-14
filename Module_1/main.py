from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "this is my first Backend Route OR end Point","status": "healthy"}

 