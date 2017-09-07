from django.conf.urls import include, url
from django.contrib import admin
from views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^get_questions/$', get_questions),
]
