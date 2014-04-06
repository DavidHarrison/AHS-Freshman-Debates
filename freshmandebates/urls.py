from django.conf.urls          import patterns, include, url
# Comment the next two lines to disable the admin:
from django.contrib.auth.views import login, logout
from django.contrib            import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$',                    'debates.views.splash'),
    url(r'^judge$',               'debates.views.judge'),
    url(r'^teacher$',             'debates.views.teacher'),
    url(r'^teacher_selector$',    'debates.views.teacherselector'),
    url(r'^team_create$',         'debates.views.teamcreate'),
    url(r'^debate_selector$',     'debates.views.debateselector'),
    url(r'^post/scoring_upload$', 'debates.views.handle', name='judging'), 
    url(r'^new_user_logIn$',      'debates.views.new_user', name = 'newuser'),
    url(r'^excel_upload$',        'debates.views.test_flowcell',
                                  name = 'ExcelUpload'),
    #url(r'^add_students$',       'debates.views.databasesetup', name = 'data'),

    #Google login Urls
    url(r'', include('social_auth.urls')),
    url(r'^logout/$', logout, {'next_page': '/'}),
    # url(r'^google/login/$', 'django_social_auth.views.login_begin', name='Social-login'),
    # url(r'^google/login-complete/$', 'django_social_auth.views.login_complete', name='Social-complete'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/',}, name='logout'),
    #End Google Urls

    # Examples:
    # url(r'^$', 'freshmandebates.views.home', name='home'),
    # url(r'^freshmandebates/', include('freshmendebates.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
