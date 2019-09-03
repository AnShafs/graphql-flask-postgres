import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from database import db_session
from models import ArticleModel
import utils

class ArticleAttribute:
    title = graphene.String(description='article title')
    article_text = graphene.String(description='link to the article')
    person_id = graphene.ID(description='Global Id of the author')

class Article(SQLAlchemyObjectType):
  
    class Meta:
        model = ArticleModel
        interfaces = (graphene.relay.Node, )
