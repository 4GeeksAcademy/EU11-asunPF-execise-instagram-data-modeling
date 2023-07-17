import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er
from sqlalchemy import Column, Enum

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(100), nullable=False)
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    user_email = Column(String(100), nullable=False, unique=True)

class Follower(Base):
    __tablename__ = 'followers'
    id = Column(Integer, primary_key=True) 
    user_from_id= Column(Integer, ForeignKey('users.id'))
    user_from = relationship(User)
    user_to_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship(User)

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(Integer, ForeignKey('users.id'))
    author = relationship(User)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Post)

class Media(Base):
    __tablename__ = 'medias'
    id = Column(Integer, primary_key=True)
    type = Column(Enum('1', '2', '3'))
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship(Post)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
