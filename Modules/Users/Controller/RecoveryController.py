from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import EmailMessage
from Modules.Users.models import User
import random
import string
from Api.settings import SENDER_MAIL


def randonPassword(stringLength=6):
    #    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(stringLength))


def recovery(subject, to):
    new_password = randonPassword()
    user = User.objects.get(email=to)
    user.set_password(new_password)
    user.save()

    body = render_to_string('MailRecovery.html', {'password': new_password})
    mail = EmailMessage(subject=subject, body=body, from_email=SENDER_MAIL, to=[to])
    mail.content_subtype = "html"
    mail.send()
