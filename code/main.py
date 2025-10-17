from fastapi import FastAPI

app=FastAPI()
@app.get('/')

def hello():
    return {'home':'hello world'}

@app.get("/about")
def about():
    return {'message' : "this is the first fastapi code"}

@app.get('/info')
def info():
    return "this is the new adding in the web page"