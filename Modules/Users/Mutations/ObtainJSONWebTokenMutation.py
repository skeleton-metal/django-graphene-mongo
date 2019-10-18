import graphql_jwt

from Api import settings
from Modules.Users.Types.UserType import UserType
import graphene


class ObtainJSONWebToken(graphql_jwt.JSONWebTokenMutation):
    user = graphene.Field(UserType)

    @classmethod
    def resolve(cls, root, info, **kwargs):
        if info.context.user.avatar:
            info.context.user.avatar = settings.MEDIA_HOST + str(info.context.user.avatar)
        return cls(user=info.context.user)
