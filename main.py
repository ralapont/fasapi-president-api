from fastapi import FastAPI
from app.v1.router.president_router import router as president_router

app = FastAPI()
app.include_router(president_router)

@app.get('/')
def home():
    return {"message": "Hello World"}
