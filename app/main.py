from fastapi import FastAPI
from app.api.v1 import router as api_router

app = FastAPI(title="AIssistant")

app.include_router(api_router, prefix="/api/v1")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
