from django.conf.urls import  url
from login import  views
urlpatterns=[
    url('login/',views.add_login),
]