from fastapi import APIRouter, status
from fastapi.params import Depends
from pydantic import BaseModel, Field
from sqlalchemy.orm import Session
from starlette.responses import StreamingResponse

from app.db.database import get_db
from app.services.trainer import Trainer

router = APIRouter()


class GenerateRoutineParams(BaseModel):
    description: str = Field(
        max_length=200,
        examples=["biceps"],
        description="Description of the muscles to train, the type of training (e.g., strength, cardio)",
    )
    try_new_exes: bool = Field(
        default=False,
        description="Whether to try new exercises or stick to the usual ones.",
    )


@router.post("/generate_routine", status_code=status.HTTP_200_OK)
async def generate_routine(
    request: GenerateRoutineParams, db: Session = Depends(get_db)
):
    trainer = Trainer(db)
    return StreamingResponse(
        trainer.generate_routine(
            description=request.description, try_new_exes=request.try_new_exes
        ),
        media_type="text/event-stream",
    )
