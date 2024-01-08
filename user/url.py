from django.conf.urls import  url
from user import  views
urlpatterns=[
    url('userreg/',views.add_userreg),
    url('view_us/', views.view_user)
    ]