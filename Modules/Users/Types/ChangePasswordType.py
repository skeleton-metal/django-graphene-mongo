import graphene


class ChangePasswordType(graphene.ObjectType):
    status = graphene.Boolean()
    message = graphene.String()
