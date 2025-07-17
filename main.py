from fastapi import FastAPI, Response, status, HTTPException
from datetime import datetime
from fastapi.params import Body
from pydantic import BaseModel
from typing import Optional
from random import randrange

now = datetime.now()

app  = FastAPI()


my_post = [{"title": "Learn Coding", "content": "Api Development With Python", "id":1},{ "Title": "AI Development", "Content": "Programming AI Models With Python", "id": 4}]

class Post(BaseModel):
    title : str
    content: str
    published: bool = True
    rating: Optional[int] = None
    # publish_date: datetime.now()
    # publish_date: datetime.now()




#Get Post By id Logic To Get
def find_post_by_id(id):
    for p in my_post:
        if p['id'] == id:
            return p



#Logic To Delete Post From List
def find_index_post(id: int):
    for i, p in enumerate(my_post):
        if p['id'] == id:
            return i
    
        
#test endpoint
@app.get("/")
async def root():
    return {"message": "Welcome to my Api"}

#List all posts
@app.get('/posts')
def get_posts():
    return {"Data": my_post}


#Create new posts
@app.post('/posts', status_code=status.HTTP_201_CREATED)
def create_post(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0, 100000)
    my_post.append(post_dict)
    print(post.published)
    return {"data": post_dict}


#get last updated Input
@app.get('/posts/latest')
def get_latest_post():
    lat = my_post[len(my_post)-1]
    return {"Data": lat}


#Get Post By id Implementation
@app.get('/posts/{id}')
def get_posts(id: int, response: Response):
    post = find_post_by_id(int(id))
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                             detail=f"Post with id: {id} was Not Found!")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {"Message": f"Post with id: {id} was Not Found!"}
    else:
        return {"Message": f"This is the Post your Interested in:{post}"}
    


#Implementation For Deleting Posts.
@app.delete('/posts/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)
    my_post.pop(index)
    return{"Message": "Post {id} Was Succeccfully Delete."}
