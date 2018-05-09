from graphene_django import DjangoObjectType
import graphene
from .models import UserModel


class User(DjangoObjectType):
    class Meta:
        model = UserModel



class Query(graphene.ObjectType):
    users = graphene.List(User)
    user = graphene.Field(User,id=graphene.Int(),
                                name=graphene.String(),
                                lastName = graphene.String()
                                )

    def resolve_users(self, info):
        return UserModel.objects.all()
    def resolve_user(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return UserModel.objects.get(id=id)

        return None

schema = graphene.Schema(query=Query)
