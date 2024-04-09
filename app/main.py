from routes import doors

from fastapi import FastAPI


app = FastAPI()
app.include_router(doors.router, prefix='/doors')