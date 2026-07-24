from fastapi import FastAPI, HTTPException


app = FastAPI()

text_post = {
    1: {"title": "video content", "content": "Playing video"},
    2: {"title": "music content", "content": "Listening to music"},
    3: {"title": "study content", "content": "Doing homework"},
    4: {"title": "game content", "content": "Playing football"},
    5: {"title": "food content", "content": "Eating lunch"},
    6: {"title": "travel content", "content": "Going to Chennai"},
    7: {"title": "work content", "content": "Coding project"},
    8: {"title": "shopping content", "content": "Buying groceries"},
    9: {"title": "exercise content", "content": "Morning workout"},
   10: {"title": "movie content", "content": "Watching a film"}
}

@app.get('/posts')
def get_all_post(limit:int):
    if limit:
        return list(text_post.values())[:limit]
    return text_post

@app.get('/posts/{id}')
def get_post_id(id:int):
    if id not in text_post:
        raise HTTPException(status_code=404, detail="Post Not Found!")
    return text_post.get(id)

