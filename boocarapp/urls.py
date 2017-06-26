from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.car_items, name='car_items'),
    url(r'/go_for_it/(?P<item>\w{0,50})', views.go_for_it, name='go_for_it'),
    url(r'index', views.car_items, name='car_items')
]