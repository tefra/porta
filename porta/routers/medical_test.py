import asyncio
from typing import Dict
from typing import List

import httpx
from clients.MedexClient import MedexClient
from clients.NumanClient import NumanClient
from fastapi import APIRouter

router = APIRouter()


@router.get("/{id}/{user_id}", tags=["medical test"])
async def get_medical_test(id: str, user_id: str) -> List[Dict]:

    async with httpx.AsyncClient() as client:
        medex_client = MedexClient(client)
        numan_client = NumanClient(client)
        tasks = [
            medex_client.get(f"medical_tests/{id}/", user_id=user_id),
            numan_client.get("clinicos/prescription_requests", user_id=user_id),
        ]

        result = await asyncio.gather(*tasks)

    return result
