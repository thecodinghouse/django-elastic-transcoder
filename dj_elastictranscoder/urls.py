from django.urls import re_path as url

from dj_elastictranscoder.views import endpoint as transcoder_endpoint

urlpatterns = (url(r'^endpoint/$', transcoder_endpoint, name='transcoder_endpoint'),)

