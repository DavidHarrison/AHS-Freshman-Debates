#!/usr/bin/env python3.4
#file: auth.py

from   django.contrib.auth.models import User
from   openid.consumer.consumer   import SUCCESS
from   django.core.mail           import mail_admins
import logging

logger = logging.getLogger('logview.debugger')


class GoogleBackend(object):
    logger.debug('Getting into start of GoogleBackend')
    def authenticate(self, openid_response):
        if openid_response is None:
            logger.debug('There is no response')
            return None
        if openid_response.status != SUCCESS:
            logger.debug('Response is a SUCCESS')
            return None
        google_email = openid_response.getSigned('http://openid.net/srv/ax/1.0','value.email')
        logger.debug('Users email =', google_email)
        google_firstname = openid_response.getSigned('http://openid.net/srv/ax/1.0','value.firstname')
        logger.debug('Users firstname =', google_firstname)
        google_lastname = openid_response.getSigned('http://openid.net/srv/ax/1.0','value.lastname')
        logger.debug('Users lastname =', google_lastname)
        #try:
            #user = User.objects.get(username=google_email)
            # Make sure that the e-mail is unique.
        user = User.objects.get(email=google_email)
        if User.DoesNotExist:
            user = User.objects.create_user(google_firstname, google_email, 'password')
            user.lastname = google_lastname
            user.save()
            user = User.objects.get(username=google_email)
            return user

        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
