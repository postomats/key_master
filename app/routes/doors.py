from fastapi import APIRouter, HTTPException, Depends

from utilities.dors import *
from utilities import controller


router = APIRouter()

@router.get('/door/{id}/open')
def open_all_dors(id: int, session = Depends(controller.connection)):    
    return unlock(session, id)


@router.get('/door/{id}/status')
def open_all_dors(id: int, session = Depends(controller.connection)):
    res = send_single_door_status(session, id)
    return res[-1] == 0


@router.get('/door_all/open')
def open_all_dors(id:int = 2, session = Depends(controller.connection)):
    open_all_locks(session, id)
    return True