from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from database import Base, engine

class PersonModel(Base):
    __tablename__ = 'person'
    person_id = Column(Integer, primary_key=True)
    username = Column('username', String)
    fullname = Column('fullname', String)
    Articles = relationship("ArticleModel")
    
class ArticleModel(Base):
    __tablename__ = 'article'
    article_id = Column(Integer, primary_key=True)
    title = Column('title', String)
    article_text = Column('article_text', String)
    person_id = Column(ForeignKey("person.person_id"))
    
Base.prepare(engine)