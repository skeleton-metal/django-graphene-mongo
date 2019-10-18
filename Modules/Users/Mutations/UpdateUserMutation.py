import graphene
from Modules.Users.Models.User import User, Group
from Modules.Users.Types.UserType import UserType
from graphql_jwt.decorators import login_required, permission_required
from graphene_django.forms.mutation import DjangoModelFormMutation
from Modules.Users.Forms.UserForm import UpdateUserForm


class UpdateUserMutation(DjangoModelFormMutation):
    user = graphene.Field(UserType)

    class Meta:
        form_class = UpdateUserForm



