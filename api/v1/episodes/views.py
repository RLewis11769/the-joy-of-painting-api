from fastapi import Depends, HTTPException, APIRouter, status
from .models import Episode
from .schemas import Add_Episode, Update_Episode
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
                            detail="Not found")
    return ep


@router.post("/{ep_id}")
def add_episode(ep_id: int, ep: Add_Episode, db: Session = Depends(get_db)):
    """ Define POST request made to endpoint including ep_id """
    new_ep = Episode(id=ep_id, title=ep.title, date=ep.date)
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
                            detail="Not found")
    if ep.title:
        episode.title = ep.title
    if ep.date:
        episode.date = ep.date
    db.commit()
    return episode
