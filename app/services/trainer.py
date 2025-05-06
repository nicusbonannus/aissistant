from typing import AsyncGenerator

from sqlalchemy.orm import Session

from app.db.models.injury import Injury
from app.services.llm_handler import LLMHandler


class Trainer:
    def __init__(self, db: Session):
        self._db = db

    async def generate_routine(
        self, description: str, try_new_exes: bool, available_time: int
    ) -> AsyncGenerator[str, None]:
        injuries = self._db.query(Injury).all()
        injuries_summary = " - ".join(
            f"{injury.body_part_name}:{injury.illness_name}" for injury in injuries
        )

        llm_handler = LLMHandler(temperature=0.8 if try_new_exes else 0.0)

        async for chunk in llm_handler.astream_response(
            description, injuries_summary, available_time
        ):
            yield chunk
