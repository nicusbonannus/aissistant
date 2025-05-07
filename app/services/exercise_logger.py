from sqlalchemy.orm import Session

from app.db.models.exercise_logs import ExerciseLog


class ExerciseLogger:
    def __init__(self, db: Session):
        self._db = db

    def log_exercise(self, muscles_worked: str, duration: int) -> ExerciseLog:
        log = ExerciseLog(
            body_parts=muscles_worked,
            total_time=duration,
        )
        self._db.add(log)
        self._db.commit()
        self._db.refresh(log)
        return log

    def get_exercise_logs(self):
        return self._db.query(ExerciseLog).all()
