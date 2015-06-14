from django.conf.urls import patterns, include, url

urlpatterns = patterns('', 
    url(r'^promotion/special/(?P<special_id>\d+)/$', 'promotion.views.special'),
)