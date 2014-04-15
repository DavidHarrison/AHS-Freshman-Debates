#!/usr/bin/env python3.4

from django.conf.urls import patterns, include, url
from django.contrib   import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',                    'debates.views.splash'),
    url(r'^judge$',               'debates.views.judge'),
    url(r'^view_scores$',         'debates.views.view_scores'),
    url(r'^teacher_selector$',    'debates.views.teacher_selector'),
    url(r'^team_create$',         'debates.views.team_create'),
    url(r'^debate_selector$',     'debates.views.debate_selector'),
    url(r'^post/scoring_upload$', 'debates.views.scoring_upload'), 
    #add social name space for social authorization
    url(r'', include('social.apps.django_app.urls', namespace='social')),
    #admin
    url(r'^admin/', include(admin.site.urls)),
    #admin documentation
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
)
