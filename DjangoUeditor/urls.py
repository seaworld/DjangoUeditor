#coding:utf-8
from django import VERSION

from views import get_ueditor_controller
from django.conf.urls import url, include

urlpatterns = [
    url(r'^controller/$', get_ueditor_controller)
]
