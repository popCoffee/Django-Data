from django.conf.urls import url
from . import views

from consumption.models import Customer, Reading

urlpatterns = [
    url(r'^$', views.summary, name = 'homepg'),
    url(r'^summary/', views.summary),
    url(r'^detail/', views.detail, name = 'detail'),

]
