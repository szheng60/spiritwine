from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from rest_framework.urlpatterns import format_suffix_patterns
from wine import api

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'spiritwine.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    (r'^spiritwine/', include('wine.urls')),
    (r'^spiritwine/', include('search.urls')),
    (r'^spiritwine/', include('promotion.urls')),
    #(r'^spiritwine/', include('cart.urls')),
    url(r'^$', 'wine.views.default'),
    url(r'^api/wineinfo/', include('rest_framework.urls', namespace = 'rest_framework')),

    url(r'^registration/$', 'buyer.views.BuyerRegistration'),
    url(r'^login/$', 'buyer.views.LoginRequest'),
    url(r'^logout/$', 'buyer.views.LogoutRequest'),
    # API
    url(r'^api/wine/merlots/$', api.MerlotListAPIView.as_view()),
    url(r'^api/wine/merlots/(?P<pk>[0-9]+)/$', api.MerlotDetailAPIView.as_view()),
    url(r'^api/wine/merlots/(?P<name>.+)/$', api.MerlotListAPIView.as_view()),
)
urlpatterns = format_suffix_patterns(urlpatterns)