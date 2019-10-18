from Modules.Users.Types.PermissionType import PermissionType
from Modules.Users.Models.User import Permission
import graphene


class PermissionQuery(graphene.ObjectType):
    permission = graphene.List(PermissionType)

    def resolve_permission(self, info):
        return Permission.objects.all()
