from fastapi import FastAPI
app = FastAPI(
    title="project hai ga ",
    description="This is a FastAPI project created by Ayush Gupta",
    version="1.0.0",
)


@app.get("/")
async def root():
    return{"message": "welcome to MAC Section A1","status": "healthy"}