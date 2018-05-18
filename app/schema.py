from graphene_django import DjangoObjectType
import graphene
from graphene import relay, ObjectType, InputObjectType
from graphql_relay.node.node import from_global_id
from .models import MarkerModel



class Marker(DjangoObjectType):
    class Meta:
        model = MarkerModel

class MarkerInput(InputObjectType):
    id=graphene.Int()
    longitude=graphene.Float()
    latitude=graphene.Float()
    icon=graphene.String(required = False)
    song=graphene.String()

class CreateMarker(graphene.Mutation):
    marker = graphene.Field(Marker)
    class Arguments:
        marker = graphene.Argument(MarkerInput)
    def mutate(self, info, marker):
        new_marker = MarkerModel.objects.create(**marker)
        return CreateMarker(new_marker)

class DeleteMarker(graphene.Mutation):
    status = graphene.Boolean()

    class Arguments:
        id = graphene.Int()

    def mutate(self, info, id):
        MarkerModel.objects.filter(id=id).delete()
        return DeleteMarker(True)


class Mutation(ObjectType):
    create_marker = CreateMarker.Field()
    delete_marker = DeleteMarker.Field()


class Query(graphene.ObjectType):
    markers = graphene.List(Marker)
    marker = graphene.Field(Marker, input = MarkerInput())

    def resolve_markers(self, info):
        return MarkerModel.objects.all()

    def resolve_marker(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return MarkerModel.objects.get(id=id)
        return None

schema = graphene.Schema(
    query=Query,
    mutation=Mutation,
    )
