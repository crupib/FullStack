from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Fastapi Success!"}

@app.post("/")
async def post_root():
    return {"message": "Post request success"}  



# uvicorn chapter_3_first_endpoint:app --reload 
