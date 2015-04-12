from django.conf.urls import patterns, include, url
from django.contrib import admin, auth

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.auth.views',
    url(r'^login/$', 'login', {'template_name': 'login.html'}, name='resify_login'),
    url(r'^logout/$', 'logout', {'next_page': '/'}, name='resify_logout'),
)

urlpatterns += patterns('',
    url(r'^', include('Registration.urls')),
)

urlpatterns += patterns('',
    url(r'^', include('ATS.urls')),
)