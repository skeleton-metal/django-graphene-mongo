from Modules.Users.models import Mail
from graphene_django import DjangoObjectType


class MailType(DjangoObjectType):
    class Meta:
        model = Mail
