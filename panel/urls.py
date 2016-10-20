from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.get_all_projects, name='projects_list'),
    url(r'^data/(?P<id>\d+)/$', views.show_charts, name="show_charts"),
]
