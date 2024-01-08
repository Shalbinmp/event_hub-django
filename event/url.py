from django.conf.urls import  url
from event import  views
urlpatterns=[
    url('ad_v_events/',views.add_view_events),
    url('event/',views.add_event),
    url('user_view/(?P<idd>\w+)', views.user_v_event),

]