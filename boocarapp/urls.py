from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.car_items, name='car_items'),
]