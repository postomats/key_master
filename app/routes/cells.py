from fastapi import APIRouter, HTTPException, Depends

from utilities.cells_control import *
from utilities import controller


router = APIRouter()

@router.get('/{id}/open')
def open_cell(id: int, session = Depends(controller.connection)):
    if id < 0:
        raise HTTPException(404, 'Cell not found')
    unlock(session, id)
    return True


@router.get('/{id}/status')
def is_open(id: int, session = Depends(controller.connection)):
    if id < 0:
        raise HTTPException(404, 'Cell not found')
    res = send_single_door_status(session, id)
    return res[-1] == 0


@router.get('/open_all')
def open_all_cells(id:int = 2, session = Depends(controller.connection)):
    open_all_locks(session, id)
    return True