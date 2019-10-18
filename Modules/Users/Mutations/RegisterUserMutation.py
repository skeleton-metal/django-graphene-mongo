import graphene
from Modules.Users.Types.UserType import UserType
from Modules.Users.Models.User import User, Group
from graphql import GraphQLError
from graphql_jwt.decorators import login_required, permission_required
from graphene_django.forms.mutation import DjangoModelFormMutation
from Modules.Users.Forms.UserForm import UserForm


class RegisterUserMutation(DjangoModelFormMutation):
    user = graphene.Field(UserType)

    class Meta:
        form_class = UserForm

