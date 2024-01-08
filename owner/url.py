from django.conf.urls import  url
from owner import  views
urlpatterns=[
    url('ad_mng_owner/',views.ad_mng_owner),
    url('event_manager/',views.ad_eventmngr),
    url('ownapp/(?P<idd>\w+)',views.apprv),
    url('rrrrr/(?P<idd>\w+)',views.rjct),
    url('vw/',views.vw_audi),
    url('profile/',views.mng_profile),
    url('edit/(?P<idd>\w+)',views.edit),
    url('delete/(?P<idd>\w+)',views.delete)

]