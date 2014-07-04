
from django.conf.urls import patterns, include, url
from questions import views

urlpatterns = patterns(
    '',
    url(r'^$', views.index, name = 'index'),
    url(r'^(?P<id>\d+)/$', views.detail, name = 'detail'),
    url(r'^(?P<id>\d+)/results/$', views.results, name = 'results'),
    url(r'^(?P<id>\d+)/votes/$', views.votes, name = 'votes')
)
