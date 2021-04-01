from fastapi import APIRouter, Depends, status
from . import schemas, database
from sqlalchemy.orm import Session
from .repository import score

get_db = database.get_db

router = APIRouter()


@router.post("/goal", status_code=status.HTTP_200_OK, response_model=schemas.Score)
def post_goal(
    request: schemas.Goal,
    db: Session = Depends(get_db),
):
    return score.post_goal(request, db)


@router.get("/score", status_code=status.HTTP_200_OK, response_model=schemas.Score)
def get_score(db: Session = Depends(get_db)):
    return score.get_score(db)