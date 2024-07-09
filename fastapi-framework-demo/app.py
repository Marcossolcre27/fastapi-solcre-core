from dotenv import load_dotenv
from .src.config.db import engine, Base
from .src.models.test import User
# FAST API
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")



@app.on_event("startup")
def configure():
    Base.metadata.create_all(bind=engine)


load_dotenv()