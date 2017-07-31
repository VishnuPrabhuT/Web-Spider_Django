from django.conf.urls import url

from profiles.views import Index
from . import views
urlpatterns = [
    url(r'^hello$', views.hello, name='hello'),
    url(r'^index/$', Index.as_view())
]