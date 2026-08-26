from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating: Optional[int] = None

@app.get("/")  #path operation
def root(): #function
    return {"message" : "Welcome to my api !!"}

@app.get("/posts")
def get_posts():
    return {"data" : "This is your posts"}


@app.post("/createposts")
def create_posts(post: Post):
    print(post)
    print(post.model_dump())
    return {"data": "post"}

#title str, content str, category, bool published