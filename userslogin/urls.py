from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.np_list, name='np_list'),
]