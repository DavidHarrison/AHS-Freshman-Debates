#!/usr/bin/env python3.4

from django.conf.urls          import patterns, include, url
# Comment the next two lines to disable the admin:
from django.contrib.auth.views import login, logout
from django.contrib            import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',                    'debates.views.splash'),
    url(r'^judge$',               'debates.views.judge'),
    url(r'^view_scores$',         'debates.views.view_scores'),
    url(r'^teacher_selector$',    'debates.views.teacher_selector'),
    url(r'^team_create$',         'debates.views.team_create'),
    url(r'^debate_selector$',     'debates.views.debate_selector'),
    url(r'^post/scoring_upload$', 'debates.views.scoring_upload'), 

    #Google login Urls
    url(r'', include('social.apps.django_app.urls')),
    url(r'^logout/$', logout, {'next_page': '/'}),
    # url(r'^google/login/$', 'django_social_auth.views.login_begin', name='Social-login'),
    # url(r'^google/login-complete/$', 'django_social_auth.views.login_complete', name='Social-complete'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/',}, name='logout'),
    #End Google Urls

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
