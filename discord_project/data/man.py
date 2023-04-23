from datetime import datetime
import sqlalchemy
from .db_session import SqlAlchemyBase


class Man(SqlAlchemyBase):
    __tablename__ = 'people'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=False)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    phone_number = sqlalchemy.Column(sqlalchemy.String, nullable=False, unique=True, index=True)
    birthday = sqlalchemy.Column(sqlalchemy.Date, nullable=False)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    created_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.now)

    def __repr__(self):
        return f'id {self.id}, {self.name}, {self.email}, {self.phone_number} {self.birthday} {self.address}'
