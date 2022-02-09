import asyncio
from typing import Dict
from typing import List

import httpx
from fastapi import APIRouter

from porta.clients.MedexClient import MedexClient
from porta.clients.NumanClient import NumanClient

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
