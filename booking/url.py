from django.conf.urls import  url
from booking import  views
urlpatterns=[
    url('ad_bkg/(?P<idd>\w+)',views.ad_bkg),
    url('o_v_manage_booking/', views.ad_view_mng_bkg),
    url('v_apprvd_booking_pay/', views.manage),
    url('apprv/(?P<idd>\w+)', views.apprv),
    url('reject/(?P<idd>\w+)',views.reject),
]