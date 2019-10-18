from Modules.Users.models import Permission
from graphene_django import DjangoObjectType


class PermissionType(DjangoObjectType):
    class Meta:
        model = Permission
