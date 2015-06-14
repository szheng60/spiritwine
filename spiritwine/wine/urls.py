from django.conf.urls import patterns, include, url


urlpatterns = patterns('', 
    url(r'^home/$', 'wine.views.home'),
    url(r'^catagory/(?P<catagory_name>.+)/$', 'wine.views.catagory'),
    url(r'^showwine/(?P<model_name>.+)/(?P<object_name>.+)/(?P<object_id>\d+)/$', 'wine.views.showwine'),
    url(r'^type/(?P<type_name>.+)/$', 'wine.views.viewType'),
)
