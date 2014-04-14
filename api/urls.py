from django.conf.urls import patterns, include, url

from django.contrib import admin
from job.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'api.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^job/$', JobView.as_view()),
    url(r'^job/create/$', CreateJob.as_view()),
    url(r'^admin/', include(admin.site.urls)),
)
