from django.conf.urls import patterns, include, url

from Business.views import BusinessHomepage

urlpatterns = patterns('',
    url(r'^business$', BusinessHomepage.as_view(), name="business"),
)