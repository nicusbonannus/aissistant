from sqlalchemy import desc
from sqlalchemy.orm import Session

from app.db.models.injury import Injury


class Doctor:
    def __init__(self, db: Session):
        self._db = db

    def list_injuries(self):
        injuries = self._db.query(Injury).order_by(desc(Injury.id)).all()
        return injuries

    def register_injury(self, injury_data) -> Injury:
        injury = Injury(**injury_data.dict())
        self._db.add(injury)
        return injury

    def get_injury(self, injury_id):
        return self._db.query(Injury).filter(Injury.id == injury_id).first()

    def remove_injury(self, injury_id):
        injury = self.get_injury(injury_id)
        self._db.delete(injury)
