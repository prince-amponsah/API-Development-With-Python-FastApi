from fastapi import FastAPI
from datetime import datetime
from . import models
from .database import engine
from .routers import users, post, auth
from .config import Settings



models.Base.metadata.create_all(bind=engine)



now = datetime.now()

app  = FastAPI()


app.include_router(post.router)
app.include_router(users.router)
app.include_router(auth.router)


