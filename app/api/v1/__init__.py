from fastapi import APIRouter

from .endpoints import events, exercises, injuries, proofs_of_concept

router = APIRouter()
router.include_router(events.router, prefix="/events", tags=["events"])
router.include_router(proofs_of_concept.router, prefix="/poc", tags=["test"])
router.include_router(exercises.router, prefix="/exercises", tags=["exercises"])
router.include_router(injuries.router, prefix="/injuries", tags=["injuries"])
