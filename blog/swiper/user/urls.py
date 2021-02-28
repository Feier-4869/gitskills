from django.conf.urls import  url
from . import views

urlpatterns=[
    url(r'^index/$', views.index, name='abc'),
    url(r'^list/$',  views.list),
    # url(r'^info/(\w+)/(\d+)/$', views.info),
    # url(r'^info/(?p<name>\w+)/(?p<age>\d+)/$', views.info),
    url(r'^info/(\w+)/(\d+)/$', views.info),
    url(r'^infos/$', views.infos),
    url(r'^posts/$', views.posts),
    url(r'^puts/$', views.puts),
    url(r'^tourl/$', views.tourl),
    url(r'^finds/$', views.finds),
    url(r'^connects/$', views.connects),

]