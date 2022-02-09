import os
import uuid
from datetime import datetime
from datetime import timedelta
from datetime import timezone
from typing import Dict
from typing import Optional

import jwt
from httpx import AsyncClient

HMAC_SECRET = "development_secret"
BASE_URL = os.environ.get("NUMAN_API_URL", "http://localhost:3000/v1")


class NumanClient:
    __slots__ = "async_client"

    def __init__(self, async_client: AsyncClient):
        self.async_client = async_client

    async def get(self, path: str, user_id: str, params: Optional[Dict] = None) -> Dict:
        headers = self.prepare_headers(user_id)
        url = f"{BASE_URL}/{path}"
        response = await self.async_client.get(url, params=params, headers=headers)
        return response.json()

    def prepare_headers(self, user_id: str) -> Dict:
        return {
            "authorization": f"Bearer {self.create_jwt_token(user_id)}",
            "Content-Type": "application/vnd.api+json",
        }

    @classmethod
    def create_jwt_token(cls, user_id: str) -> str:
        random_uuid = uuid.uuid1()
        now = datetime.utcnow().replace(tzinfo=timezone.utc)
        payload = {
            "jti": str(random_uuid),
            "sub": str(user_id),
            "scp": "user",
            "iat": int(now.timestamp()),
            "exp": int((now + timedelta(days=1)).timestamp()),
        }

        # sign token with application secret
        return jwt.encode(payload, HMAC_SECRET, algorithm="HS256")
