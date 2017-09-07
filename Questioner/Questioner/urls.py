from django.conf.urls import include, url
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', landing_page),
    url(r'^get_questions/(?P<api_key>[\w\-]+)/$', get_questions),
    url(r'^dashboard_data/$', dashboard_data),
]
