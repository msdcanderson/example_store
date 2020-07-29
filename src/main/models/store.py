from datetime import datetime
from typing import List
from db import db
# from flask_authorize import PermissionsMixin
# from extensions import authorize


# class StoreModel(db.Model, PermissionsMixin):
class StoreModel(db.Model):
    __tablename__ = "stores"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(255))
    created_on = db.Column(db.DateTime, server_default=db.func.now())
    updated_on = db.Column(db.DateTime, onupdate=datetime.now())

    @classmethod
    def find_by_id(cls, _id: int) -> "StoreModel":
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_all(cls) -> List["StoreModel"]:
        # return list(filter(authorize.read, cls.query.all()))
        return cls.query.all()

    def save_to_db(self) -> None:
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self) -> None:
        db.session.delete(self)
        db.session.commit()
