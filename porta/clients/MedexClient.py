from typing import Dict
from typing import Optional

from httpx import AsyncClient

API_SECRET = "my_nonsecret_development_medex_key"
BASE_URL = "http://localhost:8000/api"


class MedexClient:
    __slots__ = "async_client"

    def __init__(self, async_client: AsyncClient):
        self.async_client = async_client

    async def get(self, path: str, user_id: str, params: Optional[Dict] = None) -> Dict:
        headers = self.prepare_headers(user_id)
        url = f"{BASE_URL}/{path}"
        response = await self.async_client.get(url, params=params, headers=headers)
        return response.json()

    @classmethod
    def prepare_headers(cls, user_id: str) -> Dict:
        return {
            "X-USER-ID": user_id,
            "authorization": f"Bearer {API_SECRET}",
            "Content-Type": "application/vnd.api+json",
        }
