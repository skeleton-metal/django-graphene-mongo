from Modules.Users.models import Group
from graphene_django import DjangoObjectType


class GroupType(DjangoObjectType):
    class Meta:
        model = Group
