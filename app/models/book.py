from app.extensions import db
import uuid


class Book(db.Model):
    __tablename__ = "Books"
    id = db.Column(db.String(), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = db.Column(db.String())
    length = db.Column(db.Integer())

    def __init__(self, title: str, length: int) -> None:
        self.id = str(uuid.uuid4())
        self.title = title
        self.length = length
