from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^shoppingcart/$', 'cart.views.cart')
)