from fastapi import APIRouter

router = APIRouter()

@router.get("/today")
def describe_today():
    return {"message": "Bonsoir Elliot"}

