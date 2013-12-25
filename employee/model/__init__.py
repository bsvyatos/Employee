import sqlalchemy as sa
from sqlalchemy import orm

from employee.model.meta import Session, Base


def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)

t_persons = sa.Table("users", Base.metadata,
    sa.Column("id", sa.types.Integer, autoincrement=True, primary_key=True),
    sa.Column("sname", sa.types.String(100), primary_key=True),
    sa.Column("name", sa.types.String(100)),
    sa.Column("email", sa.types.String(100)),
    sa.Column("password", sa.types.String(100)),
    sa.Column("birthday", sa.types.String(50)),
    sa.Column("wage", sa.types.Integer),
    sa.Column("depart", sa.types.String(10)),
    )

class Person(object):
    pass

orm.mapper(Person, t_persons)
