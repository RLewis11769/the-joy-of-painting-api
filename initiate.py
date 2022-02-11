from engine.db import SessionLocal
# from api.v1.episodes import views
# from sqlalchemy import Session

# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
session = SessionLocal()
