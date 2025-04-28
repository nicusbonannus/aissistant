from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import router as api_router
from app.core.config import settings

tags_metadata = [
    {
        "name": "test",
        "description": "Proofs of concept.",
    },
    {
        "name": "exercises",
        "description": "Generate exercises routines for a given set of muscles.",
    },
]

app = FastAPI(title=settings.APP_NAME, debug=settings.DEBUG, openapi_tags=tags_metadata)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
