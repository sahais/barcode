from django.conf.urls import include, url
from . import views

app_name = 'sampling_event'

urlpatterns = [

    url(r'^$', views.index, name='index'),
    #url(r'^$', views.IndexView.as_view(), name='index'),

    url(r'^register/$', views.UserFormView.as_view(), name='register'),


    #sampling_event/001
    url(r'^(?P<sampleEvent_id>[0-9]+)/$', views.detail, name='detail'),

    url(r'^sampleEvent/add/$', views.sampleEventCreate.as_view(), name='sampleEvent-add'),

    url(r'^sampleEvent/(?P<pk>[0-9]+)/$', views.sampleEventUpdate.as_view(), name='sampleEvent-update'),

    url(r'^sampleEvent/(?P<pk>[0-9]+)/delete/$', views.sampleEventDelete.as_view(), name='sampleEvent-delete'),





    # sampling_event/sample/1
    url(r'^sample/(?P<pk>[0-9]+)/$', views.sampleIndex, name='sample-index'),



    url(r'^sample/add/$', views.sampleCreate.as_view(), name='sample-add'),

    url(r'^sample/(?P<pk>[0-9]+)/$', views.sampleUpdate.as_view(), name='sample-update'),

    url(r'^sample/(?P<pk>[0-9]+)/delete/$', views.sampleDelete.as_view(), name='sample-delete'),

]
