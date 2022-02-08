from typing import Dict

from fastapi import APIRouter

router = APIRouter()


@router.get("/show/{id}/{user_id}", tags=["medical test"])
async def get_medical_test(id: str, user_id: str) -> Dict:
    return {"data": {}}
