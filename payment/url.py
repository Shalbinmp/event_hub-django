from django.conf.urls import  url
from payment import  views
urlpatterns=[
    url('ad_v_payment/',views.ad_veiw_paymnt),
    url('o_v_payment/',views.ad_owner_v_paymnt),
    url('payment/(?P<idd>\w+)',views.ad_paymnt),
    url('v_payment/',views.ad_v_payment),
]