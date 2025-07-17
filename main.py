from fastapi import FastAPI


app  = FastAPI()

@app.get("/")
async def root():
    return {"message": "Welcome to my Api"}


@app.get('/posts')
def get_posts():
    return {"Data": "This is your posts"}