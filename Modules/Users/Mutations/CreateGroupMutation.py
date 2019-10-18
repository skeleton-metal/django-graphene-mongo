import graphene
from Modules.Users.Types.GroupType import GroupType
from Modules.Users.Models.User import Group
from graphql_jwt.decorators import login_required, permission_required


class CreateGroup(graphene.Mutation):
    group = graphene.Field(GroupType)

    class Arguments:
        id = graphene.Int()
        name = graphene.String()

    @login_required
    def mutate(self, info, name):
        group = Group.objects.create(
            name=name)
        return CreateGroup(group=group)
