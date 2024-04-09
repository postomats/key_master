from fastapi import APIRouter, HTTPException, Depends

from ..utilities.dors import *
from ..utilities import controller


router = APIRouter()

@router.get('/door/{id}/open')
def open_all_dors(id: int, session = Depends(controller.connection)):    
    return unlock(session, id)


@router.get('/door/{id}/status')
def open_all_dors(id: int, session = Depends(controller.connection)):
    return send_single_door_status(session, id)


@router.get('/door/all/open')
def open_all_dors(session = Depends(controller.connection)):
    return open_all_locks(session, 0), open_all_locks(session, 1)