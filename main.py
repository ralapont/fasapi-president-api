from fastapi import FastAPI
from app.v1.router.president_router import router as president_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:5173",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(president_router)

@app.get('/')
def home():
    return {"message": "Hello World"}
