from graphene_sqlalchemy import SQLAlchemyConnectionField
import graphene
import schema_person
import schema_article

class Mutation(graphene.ObjectType):
    createPerson = schema_person.CreatePerson.Field()

class Query(graphene.ObjectType):
    
    node = graphene.relay.Node.Field()
    person = graphene.Field(schema_person.Person, uuid = graphene.Int())
    people = SQLAlchemyConnectionField(schema_person.Person)
    article = graphene.Field(schema_article.Article)
    articleList = SQLAlchemyConnectionField(schema_article.Article)
    
    def resolve_person(root, info, uuid):
        query = schema_person.Person.get_query(info)
        return query.get(uuid)

schema = graphene.Schema(query=Query, mutation=Mutation)
