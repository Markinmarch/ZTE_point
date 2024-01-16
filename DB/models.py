import sqlalchemy as sql
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = sql.Column(
        sql.Integer,
        primary_key = True,
    )
    name = sql.Column(
        sql.String(length = 40),
        nullable = False
    )
    phone = sql.Column(
        sql.Integer,
        nullable = False,
        unique = True
    )
    email = sql.Column(
        sql.String,
        mullable = False,
        unique = True
    )
    password = sql.Column(
        sql.String,
        nullable = False
    )

    def __str__(self):
        return '%s, %s, %s' % (self.id, self.name)
    
class Order(Base):
    __tablename__ = 'order'

    id = sql.Column(
        sql.Integer,
        primary_key = True
    )
    item = sql.Column(
        sql.String,
        nullable = True,
        unique = True
    )
    index = sql.Column(
        sql.Integer,
        nullable = True,
        unique = True
    )
    id_user = sql.Column(
        sql.Integer,
        sql.ForeignKey('user.id'),
        nullable = False
    )

    user = relationship(User, backref = 'order')

    def __str__(self):
        return '%s: %s, %s' % (self.id, self.id_user, self.item)
    
def create_table(engine):
    Base.metadata.create_all(engine)