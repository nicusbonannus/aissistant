from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette import status

from app.api.v1.deps.injuries import InjuryCreationData, InjuryResponse
from app.db.database import get_db
from app.services.doctor import Doctor

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
def list_injuries(db: Session = Depends(get_db)):
    injuries = Doctor(db).list_injuries()
    return {"data": injuries}


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=InjuryResponse)
def create_injury(injury_data: InjuryCreationData, db: Session = Depends(get_db)):
    try:
        doctor = Doctor(db)
        injury = doctor.register_injury(injury_data)
        db.commit()
        return injury
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))


@router.get("/{injury_id}", status_code=status.HTTP_200_OK)
def get_injury(injury_id: int, db: Session = Depends(get_db)):
    injury = Doctor(db).get_injury(injury_id)
    if not injury:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Injury not found"
        )
    return {"data": injury}


@router.delete("/{injury_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_injury(injury_id: int, db: Session = Depends(get_db)):
    Doctor(db).remove_injury(injury_id)
    db.commit()
