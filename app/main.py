from utils.dors import COMMANDS, send_command

from fastapi import FastAPI


app = FastAPI()

@app.patch('/dors/open_app')
def open_all_dors():
    send_command(COMMANDS.all_dors)
    return True