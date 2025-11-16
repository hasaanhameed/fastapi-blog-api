from fastapi import FastAPI
from Blog import models
from Blog.database import engine
from Blog.routers import blog, user, authentication

app = FastAPI()

models.Base.metadata.create_all(engine) # For creating tables

app.include_router(blog.router)
app.include_router(user.router)
app.include_router(authentication.router)

    