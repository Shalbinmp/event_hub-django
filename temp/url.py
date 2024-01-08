from django.conf.urls import  url
from temp import  views
urlpatterns=[
    url('admin_home/',views.admin_home),
    url('event_home/',views.Event_home),
    url('main_home/',views.main_home),
    url('user_home/',views.user_home),
    url('view_admin/',views.view_admin),
    url('v_event_m/',views.view_event_m),
    url('viw_user/',views.view_user),
    url('add_event/',views. add_event)

]