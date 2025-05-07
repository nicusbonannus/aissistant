from sqlalchemy.orm import Session

from app.services.exercise_logger import ExerciseLogger


class TestLogExercise:
    def test_log_exercise__happy_path(self, db_session: Session):
        # given
        exercise_logger = ExerciseLogger(db_session)
        assert exercise_logger.get_exercise_logs() == []

        # when
        exercise_logger.log_exercise(muscles_worked="biceps,triceps", duration=30)

        # then
        logs = exercise_logger.get_exercise_logs()
        assert len(logs) == 1
        assert logs[0].body_parts == "biceps,triceps"
        assert logs[0].total_time == 30
