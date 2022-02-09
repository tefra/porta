import logging
from typing import Dict

from fastapi import FastAPI
from starlette.exceptions import HTTPException
from starlette.requests import Request
from starlette.responses import JSONResponse

from porta.routers import medical_test

logger = logging.getLogger(__name__)

app = FastAPI()
app.include_router(medical_test.router, prefix="/medical_test")


@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException) -> JSONResponse:
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "errors": [
                {
                    "code": exc.status_code,
                    "detail": exc.detail,
                }
            ]
        },
    )


@app.exception_handler(Exception)
async def exception_handler(request: Request, exc: Exception) -> JSONResponse:
    logger.error(exc)
    return JSONResponse(
        status_code=500,
        content={
            "errors": [
                {
                    "code": 500,
                    "detail": "Something's broken, something's broken, it's your fault",
                }
            ]
        },
    )


@app.get("/")
async def index() -> Dict:
    return {"data": {"message": "I am porta"}}
