from fastapi import APIRouter, status
from fastapi.params import Depends
from sqlalchemy.orm import Session
from starlette.responses import StreamingResponse

from app.api.v1.deps.excercises_params import GenerateRoutineParams
from app.db.database import get_db
from app.services.trainer import Trainer

router = APIRouter()


@router.post("/generate_routine", status_code=status.HTTP_200_OK)
async def generate_routine(
    request: GenerateRoutineParams, db: Session = Depends(get_db)
):
    trainer = Trainer(db)
    return StreamingResponse(
        trainer.generate_routine(
            description=request.description,
            try_new_exes=request.try_new_exes,
            available_time=request.available_time,
        ),
        media_type="text/event-stream",
    )
