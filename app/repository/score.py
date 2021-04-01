from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi.encoders import jsonable_encoder


def get_score(db: Session):
    score = db.query(models.Score).first()
    if not score:
        new_score = create_score()
        db.add(new_score)
        db.commit()
        db.refresh(new_score)
        return new_score
    return score


def post_goal(request: schemas.Goal, db: Session):
    score = db.query(models.Score).first()
    if not score:
        new_score = create_score()
        db.add(new_score)
        db.commit()
        db.refresh(new_score)
    score = db.query(models.Score).first()
    query = jsonable_encoder(request)
    if query["team"] == "home":
        score.home += 1
    else:
        score.away += 1
    db.commit()
    return score


def create_score():
    new_score = models.Score(home=0, away=0)
    return new_score
