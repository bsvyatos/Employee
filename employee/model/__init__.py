import sqlalchemy as sa
from sqlalchemy import orm

from employee.model.meta import Session, Base


def init_model(engine):
    """Call me before using any of the tables or classes in the model"""
    Session.configure(bind=engine)

t_persons = sa.Table("users", Base.metadata,
    sa.Column("id", sa.types.Integer, autoincrement=True, primary_key=True),
    sa.Column("sname", sa.types.String(100)),
    sa.Column("name", sa.types.String(100), primary_key=True),
    sa.Column("email", sa.types.String(100)),
    sa.Column("password", sa.types.String(100)),
    sa.Column("birthday", sa.types.String(50)),
    sa.Column("wage", sa.types.Integer),
    sa.Column("depart_id", sa.types.Integer, sa.ForeignKey('depart.id')),
    )
t_departments = sa.Table("depart", Base.metadata,
    sa.Column("id", sa.types.Integer, autoincrement=True, primary_key=True),
    sa.Column("depart", sa.types.String(20)),
    )

class Person(object):
    pass

class Department(object):
    pass

orm.mapper(Person, t_persons)
orm.mapper(Department, t_departments)
