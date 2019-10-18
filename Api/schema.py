import graphene
import graphql_jwt
import Modules.Users.schema


class Query(Modules.Users.schema.Query, graphene.ObjectType):
    pass


class Mutation(Modules.Users.schema.Mutation, graphene.ObjectType):
    refresh_token = graphql_jwt.Refresh.Field()
    verify_token = graphql_jwt.Verify.Field()
    revoke_token = graphql_jwt.Revoke.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
