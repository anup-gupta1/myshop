from django.conf.urls import url
from . import views
app_name = 'shopbybrand'

urlpatterns = [
    url(r'^$', views.product_list, name='product_list'),
    url(r'^(?P<brand_slug>[-\w]+)/$', views.product_list, name='product_list_by_brand'),
    url(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),

]
