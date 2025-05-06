from pydantic import BaseModel, Field


class GenerateRoutineParams(BaseModel):
    description: str = Field(
        max_length=200,
        examples=["biceps"],
        description="Description of the muscles to train, the type of training (e.g., strength, cardio)",
    )
    available_time: int = Field(
        default=60,
        ge=0,
        le=180,
        description="Time available for the workout in minutes.",
    )
    try_new_exes: bool = Field(
        default=False,
        description="Whether to try new exercises or stick to the usual ones.",
    )
