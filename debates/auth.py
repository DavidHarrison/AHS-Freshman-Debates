#!/usr/bin/env python2.7
#file: auth.py

from   django.contrib.auth.models import User
from   openid.consumer.consumer   import SUCCESS
from   django.core.mail           import mail_admins
import logging

logger = logging.getLogger(u'logview.debugger')


class GoogleBackend(object):
    logger.debug(u'Getting into start of GoogleBackend')
    def authenticate(self, openid_response):
        if openid_response is None:
            logger.debug(u'There is no response')
            return None
        if openid_response.status != SUCCESS:
            logger.debug(u'Response is a SUCCESS')
            return None
        google_email = openid_response.getSigned(u'http://openid.net/srv/ax/1.0',u'value.email')
        logger.debug(u'Users email =', google_email)
        google_firstname = openid_response.getSigned(u'http://openid.net/srv/ax/1.0',u'value.firstname')
        logger.debug(u'Users firstname =', google_firstname)
        google_lastname = openid_response.getSigned(u'http://openid.net/srv/ax/1.0',u'value.lastname')
        logger.debug(u'Users lastname =', google_lastname)
        #try:
            #user = User.objects.get(username=google_email)
            # Make sure that the e-mail is unique.
        user = User.objects.get(email=google_email)
        if User.DoesNotExist:
            user = User.objects.create_user(google_firstname, google_email, u'password')
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
