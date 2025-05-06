from sqlalchemy import Column, DateTime, Integer, String, func

from app.db.database import Base


class ExerciseLog(Base):
    __tablename__ = "exercises_logs"
    id = Column(Integer, primary_key=True, index=True)
    body_parts = Column(String(250), nullable=False)
    total_time = Column(Integer, nullable=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(
        DateTime(timezone=True), server_default=func.now(), onupdate=func.now()
    )

    def __str__(self):
        return f"{self.id} - {self.created_at}"
