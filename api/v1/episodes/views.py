from fastapi import Depends, HTTPException, APIRouter, status
from .models import Episode
from .schemas import Add_Episode, Update_Episode
from .utils import find_value, color_dict, subject_dict, month_dict
from initiate import Session, get_db


router = APIRouter(
    prefix="/api/v1/episodes"
)


@router.get("/")
def all_episodes(db: Session = Depends(get_db)):
    """ Define GET request made to /episodes endpoint """
    eps = db.query(Episode).all()
    return eps


@router.get("/{ep_id}")
def one_episode(ep_id: int, db: Session = Depends(get_db)):
    """ Define GET request made to endpoint including ep_id """
    ep = db.query(Episode).filter_by(id=ep_id).first()
    if not ep:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Episode not found")
    return ep


@router.post("/{ep_id}")
def add_episode(ep_id: int, ep: Add_Episode, db: Session = Depends(get_db)):
    """ Define POST request made to endpoint including ep_id """
    new_ep = Episode(id=ep_id, title=ep.title, date=ep.date)
    if new_ep:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Episode ID already exists")
    db.add(new_ep)
    db.commit()
    return new_ep


@router.put("/{ep_id}")
def update_episode(ep_id: int, ep: Update_Episode,
                   db: Session = Depends(get_db)):
    """ Define PUT request made to endpoint including ep_id """
    episode = db.query(Episode).filter_by(id=ep_id).first()
    if not episode:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Episode not found")
    if ep.title:
        episode.title = ep.title
    if ep.date:
        episode.date = ep.date
    db.commit()
    return episode


@router.get("/color/{color_id}")
def all_episodes_by_color(color_id: int,
                          db: Session = Depends(get_db)) -> str:
    """ Define GET request made to /episodes/colors/:id endpoint """
    column_name = find_value(color_dict, color_id)
    if not column_name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Color not found")
    # Search for eps within column name based on color_id
    eps = db.query(Episode).filter_by(**{column_name: True}).all()
    return eps


@router.get("/subject/{subject_id}")
def all_episodes_by_subject(subject_id: int,
                            db: Session = Depends(get_db)) -> str:
    """ Define GET request made to /episodes/subject/:id endpoint """
    column_name = find_value(subject_dict, subject_id)
    if not column_name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Subject not found")
    # Search for eps within column name based on subject_id
    eps = db.query(Episode).filter_by(**{column_name: True}).all()
    return eps


@router.get("/month/{month_id}")
def all_episodes_by_month(month_id: int,
                          db: Session = Depends(get_db)) -> str:
    """ Define GET request made to /episodes/month/:id endpoint """
    column_name = find_value(month_dict, month_id)
    if not column_name:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Month not found")
    # Search for eps where date column includes month based on month_id
    eps = db.query(Episode).filter(Episode.date.like(f"%{column_name}%")).all()
    return eps
