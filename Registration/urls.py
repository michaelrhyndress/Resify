from django.conf.urls import patterns, include, url

from Registration.views import Registration, Resume, Homepage, Login

urlpatterns = patterns('',
    url(r'^register$', Registration.as_view(), name="register"),
    url(r'^check_handle$', 'Registration.views.checkURL', name='check_handle'),
    url(r'^(?P<handle>\w+)/$', Resume.as_view(), name="resify_resume"),
    url(r'^$', Homepage.as_view(), name="resify_home"),
    url(r'^login$', Login.as_view(), name='login'),
    url(r'^logout$', 'Registration.views.logout', name='logout'),
    url(r'^setup/skip$', 'Registration.views.skipSetup', name='skip'),
    url(r'^setup$', 'Registration.views.Homepage', name='setup'),
    url(r'^save$', 'Registration.views.saveResume', name='save_resume'),
)