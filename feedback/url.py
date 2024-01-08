from django.conf.urls import  url
from feedback import  views
urlpatterns=[
    url('ad_v_feedback/',views.add_v_fedbck),
    url('feedback/',views.ad_feedback),
    url('view_fedbck/',views.view_feedback),
]