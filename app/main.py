from routes import cells

from fastapi import FastAPI


app = FastAPI()
app.include_router(cells.router, prefix='/cells', tags=['Ключник'])


@app.get('/info')
def information():
    return {
        'size': 24,
        'servises': [3],
        'lockers': 2
    }