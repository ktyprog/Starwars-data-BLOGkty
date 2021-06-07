import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(40), nullable=False)
    last_name = Column(String(80), nullable=False)
    email = Column (String(120), nullable=False)
    

    # is_logged= Column(Boolean, default=False, nullable=False)
class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    creator_id = Column(Integer, ForeignKey('user.id'))
    post = relationship(User)
    image = Column(String(400), nullable=False)
    text = Column(String(400))

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    creator_id = Column(Integer, ForeignKey('user.id'))
    user=relationship(User)
    post_id = Column(Integer, ForeignKey('post.id'))

    
class Likes(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    creator_id = Column(Integer, ForeignKey('user.id'))
    comment_id =  Column(Integer, ForeignKey('comment.id'))

class Media(Base):
	__tablename__ = 'media'
	id = Column(Integer, primary_key=True)
	url = Column(String(250))
	post_id = Column(Integer, ForeignKey('post.id'))
	post= relationship(Post)
    

def to_dict(self):
    return {}

render_er(Base, 'diagram.png')

	







