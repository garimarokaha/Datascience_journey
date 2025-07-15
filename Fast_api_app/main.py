from fastapi import FastAPI

app = FastAPI()  #app bhane object banayeko, yehi ibject bata route banaune ho

@app.get('/') #@ ley route banaune
def show():
    return {'message':'Hello Guys!!'}

@app.get('/about')
def about():
    return {'Display':'Broad AI is a education sector'}
