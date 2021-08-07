from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'^api/customers/$', views.customers_list),
    url(r'^api/customers/(?P<pk>[0-9]+)$', views.customers_detail),
]