import logging

from fastapi import APIRouter


router = APIRouter()


@router.get('/healthcheck', responses={200: {'content': {'application/json': {'example': 'OK'}}}})
async def _():
    return 'OK'


@router.get('/')
async def _():
    return 'Test'
