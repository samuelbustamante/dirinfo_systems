# -*- coding: utf-8 -*-

from django.contrib.auth.models import User
from xmlrpc.client import ServerProxy


class AuthenticateBackend(object):
    """Authenticate Backend
    """
    def __init__(self):
        self.domain = 'unsl.edu.ar'
        self.proxy_url = 'http://unslid.unsl.edu.ar:80/xmlrpc/server.php'
        self.mailbox_url = 'mailbox.unsl.edu.ar'

    def authenticate(self, username=None, password=None):
        # Validate User exist
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return None
        # Validate XML-RPC
        server = ServerProxy(self.proxy_url)
        validate = server.mail.validate(username, password, self.mailbox_url)
        if validate:
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
