import graphene
from Modules.Users.Types.ChangePasswordType import ChangePasswordType
from Modules.Users.Models.User import User
from graphql_jwt.decorators import login_required, permission_required


class ChangePassword(graphene.Mutation):
    status = graphene.Field(ChangePasswordType)

    class Arguments:
        id = graphene.Int()
        password = graphene.String()
        password2 = graphene.String()

    @login_required
    def mutate(self, info, id, password, password2):
        if password != password2:
            raise Exception("Las contraseñas no coinciden")
        user = User.objects.get(id=id)
        user.set_password(password)
        user.save()
        change = ChangePasswordType(status=True, message="Se modifico la contraseña correctamente")
        return ChangePassword(status=change)
