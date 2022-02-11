from fastapi import HTTPException, APIRouter, status
from .models import Episode
from .schemas import Add_Episode, Update_Episode
from initiate import session

router = APIRouter(
    prefix="/api/v1/episodes"
)


@router.get("/")
def all_episodes():
    """ Define GET request made to /episodes endpoint """
    eps = session.query(Episode).all()
    return eps

# # How to handle query parameters
# @app.get("/api/v1/episodes")
# def search_episodes(subject: Optional[int] = None, color: Optional[int] = None, date: Optional[int] = None):
#     ep = s.query(Episode).filter_by(subject=subject, color=color, date=date).first()
#     if not ep:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
#     return ep

@router.get("/{ep_id}")
def one_episode(ep_id: int):
    """ Define GET request made to endpoint including ep_id """
    ep = session.query(Episode).filter_by(id=ep_id).first()
    if not ep:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    return ep

@router.post("/{ep_id}")
def add_episode(ep_id: int, ep: Add_Episode):
    """ Define POST request made to endpoint including ep_id """
    new_ep = Episode(id=ep_id, title=ep.title, date=ep.date)
    session.add(new_ep)
    session.commit()
    return new_ep

@router.put("/{ep_id}")
def update_episode(ep_id: int, ep: Update_Episode):
    """ Define PUT request made to endpoint including ep_id """
    episode = session.query(Episode).filter_by(id=ep_id).first()
    if not episode:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Not found")
    if ep.title:
        episode.title = ep.title
    if ep.date:
        episode.date = ep.date
    session.commit()
    return episode
