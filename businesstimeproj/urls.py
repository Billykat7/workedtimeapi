from django.conf.urls import url
from django.contrib import admin
from businesstimeapp import views
# from django.urls import path


urlpatterns = [
    url(r'^$', views.homePage, name='homePage'),
    url(r'^timeworked/?$', views.timeworked, name='timeworked'),
]