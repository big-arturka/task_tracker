from .models import CustomUser
from django.core.mail import EmailMessage

def mailing(email):
    super_users = CustomUser.objects.filter(is_superuser=True)
    email_lst = []
    for user in super_users:
        email_lst.append(user.email)
    subject = 'Hello!'
    body = f'User {email} registered in database as staff, please check him!'
    send_email = EmailMessage(subject=subject, body=body, to=email_lst)
    send_email.send()
