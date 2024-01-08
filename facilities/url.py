from django.conf.urls import  url
from facilities import  views
urlpatterns=[
    url('ad_v_faclity/',views.ad_view_facilities),
    url('facility/',views.ad_facility),
    url('view_faclty/',views.v_faclities),

]