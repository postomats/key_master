from app.routes import cells

from fastapi import FastAPI


app = FastAPI()
app.include_router(cells.router, prefix='/doors', tags=['Ключник'])