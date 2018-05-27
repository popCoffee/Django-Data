from django.conf.urls import url
from . import views

from consumption.models import Customer, Reading

urlpatterns = [
    url(r'^$', views.home, name = 'initial'),
    url(r'^summary/', views.summary, name = 'homepg'),
    url(r'^detail/', views.detail, name = 'detail'),

]
