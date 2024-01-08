from django.conf.urls import  url
from complaint import  views
urlpatterns=[
    url('ad_v_post_rply/',views.ad_v_post_rply),
    url('complt/',views.add_complaint),
    url('reply_v/',views.add_reply_view),
    url('v_cmplnt/',views.add_view_cmplnt),
    url('o_v_reply/', views.ad_v_rply),
    url('send_rply/(?P<idd>\w+)',views.ad_reply)
]
