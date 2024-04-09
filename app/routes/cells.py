from fastapi import APIRouter, HTTPException, Depends

from app.utilities.cells_control import *
from utilities import controller


router = APIRouter()

@router.get('/cell/{id}/open')
def open_cell(id: int, session = Depends(controller.connection)): 
    unlock(session, id)
    return True


@router.get('/cell/{id}/status')
def is_open(id: int, session = Depends(controller.connection)):
    res = send_single_door_status(session, id)
    return res[-1] == 0


@router.get('/all_cells/open')
def open_all_cells(id:int = 2, session = Depends(controller.connection)):
    open_all_locks(session, id)
    return True