from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.get_all_projects, name='projects_list'),
    url(r'^data/(?P<id>\d+)/$', views.show_charts, name="show_charts"),
    url(r'^data/milestones/(?P<id>\d+)/$', views.get_milestones_stats, name="show_milestone"),
    url(r'^showbar/(?P<id>\d+)/$', views.show_panel, name="show_panel"),
]
