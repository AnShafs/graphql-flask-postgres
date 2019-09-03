import graphene
from graphene_sqlalchemy import SQLAlchemyObjectType
from database import db_session
from models import PersonModel
import utils

class PersonAttribute:
    username = graphene.String(description='username')
    fullname = graphene.String(description='first and last name')

class Person(SQLAlchemyObjectType):

    class Meta:
        model = PersonModel
        interfaces = (graphene.relay.Node, )

class CreatePersonInput(graphene.InputObjectType, PersonAttribute):
    pass

class CreatePerson(graphene.Mutation):
    person = graphene.Field(lambda: Person, description='person created by mutation')

    class Arguments:
        input = CreatePersonInput(required=True)

    def mutate(self, info, input):
        data = utils.input_to_dictionary(input)

        person = PersonModel(**data)
        db_session.add(person)
        db_session.commit()

        return CreatePerson(person=person)
