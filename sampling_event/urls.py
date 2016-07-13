from django.conf.urls import include, url
from . import views

app_name = 'sampling_event'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    #url(r'^$', views.IndexView.as_view(), name='index'),

    #sampling_event/001
    url(r'^(?P<sampleEvent_id>[0-9]+)/$',views.detail, name='detail'),

    url(r'^add/$', views.sampleEventCreate.as_view(), name='sampleEvent - add'),
]
