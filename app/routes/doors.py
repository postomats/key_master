from fastapi import APIRouter, HTTPException

from ..utilities.dors import COMMANDS, send_command


router = APIRouter()

@router.get('/door/{id}/open')
def open_all_dors(id: int):
    if id == 3:
        raise HTTPException(403, 'services door')
    
    send_command(COMMANDS.UNLOCK, data_field=[id])
    return True


@router.get('/door/{id}/status')
def open_all_dors(id: int):
    send_command(COMMANDS.READ_SINGLE_DOOR_STATUS, data_field=[id])
    return True


@router.get('/door/all/open')
def open_all_dors():
    send_command(COMMANDS.OPEN_ALL_LOCKS)
    return True