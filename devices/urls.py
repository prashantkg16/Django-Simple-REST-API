from django.conf.urls import url
from . import views, rests

app_name='devices'
urlpatterns = [  
    url(r'^api/(?P<api_method>\S+)$', rests.api_expose,  name='api expose getters'),
    ]