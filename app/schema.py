from graphene_django import DjangoObjectType
import graphene
from .models import UserModel, MarkerModel


class User(DjangoObjectType):
    class Meta:
        model = UserModel


class Marker(DjangoObjectType):
    class Meta:
        model = MarkerModel


class Query(graphene.ObjectType):
    users = graphene.List(User)
    user = graphene.Field(User,id=graphene.Int(),
                                name=graphene.String(),
                                lastName = graphene.String()
                                )
    markers = graphene.List(Marker)
    marker = graphene.Field(Marker, id=graphene.Int(),
                                    longitude=graphene.Float(),
                                    latitude=graphene.Float(),
                                    icon=graphene.String(),
                                    song=graphene.String()
                                    )

    def resolve_users(self, info):
        return UserModel.objects.all()

    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return UserModel.objects.get(id=id)
        return None

    def resolve_markers(self, info):
        return MarkerModel.objects.all()

    def resolve_marker(self, info, **kwargs):
        id = kwargs.get('id')
        if id is not None:
            return MarkerModel.objects.get(id=id)
        return None

schema = graphene.Schema(query=Query)
