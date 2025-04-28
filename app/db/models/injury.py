from sqlalchemy import Boolean, Column, Integer, String

from app.db.database import Base


class Injury(Base):
    __tablename__ = "injuries"
    id = Column(Integer, primary_key=True, index=True)
    body_part_name = Column(String(50), nullable=False)
    illness_name = Column(String(50), nullable=True)
    has_been_cured = Column(Boolean, nullable=False, default=False)

    def __str__(self):
        return f"{self.body_part_name} - {self.illness_name}"
