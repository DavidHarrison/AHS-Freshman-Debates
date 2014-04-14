#!/usr/bin/env python2.7

from django.conf.urls          import patterns, include, url
# Comment the next two lines to disable the admin:
from django.contrib.auth.views import login, logout
from django.contrib            import admin

admin.autodiscover()

urlpatterns = patterns(u'',
    url(ur'^$',                    u'debates.views.splash'),
    url(ur'^judge$',               u'debates.views.judge'),
    url(ur'^view_scores$',         u'debates.views.view_scores'),
    url(ur'^teacher_selector$',    u'debates.views.teacher_selector'),
    url(ur'^team_create$',         u'debates.views.team_create'),
    url(ur'^debate_selector$',     u'debates.views.debate_selector'),
    url(ur'^post/scoring_upload$', u'debates.views.scoring_upload'), 

    #Google login Urls
    url(ur'', include(u'social.apps.django_app.urls')),
    url(ur'^logout/$', logout, {u'next_page': u'/'}),
    # url(r'^google/login/$', 'django_social_auth.views.login_begin', name='Social-login'),
    # url(r'^google/login-complete/$', 'django_social_auth.views.login_complete', name='Social-complete'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/',}, name='logout'),
    #End Google Urls

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(ur'^admin/', include(admin.site.urls)),
)
