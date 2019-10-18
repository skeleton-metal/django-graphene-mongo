from Api import settings
from Modules.Users.Types.UserType import UserType
from Modules.Users.Models.User import User
import graphene


class UsersQuery(graphene.ObjectType):
    users = graphene.List(UserType)

    def resolve_users(self, info):
        users = User.objects.all()
        users2 = []
        for user in users:
            if user.avatar:
                user.avatar = settings.MEDIA_HOST + str(user.avatar)
            users2.append(user)
        return users2
