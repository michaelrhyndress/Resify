from django.conf.urls import patterns, include, url

from ATS.views import BulkKeywords

urlpatterns = patterns('',
    url(r'^add/keyword/bulk$', BulkKeywords.as_view(), name="bulkAdd"),
)