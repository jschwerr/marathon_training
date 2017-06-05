from django.conf.urls import url

from . import views

app_name = 'training_tracker'
urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add_run/$', views.add_run, name="add_run"),
    url(r'^add_runner/$', views.add_runner, name="add_runner"),
    url(r'^add_miles/run/(?P<run_id>[0-9]+)$', views.add_miles, name="add_miles"),
    url(r'^post_run/$', views.post_run, name="post_run"),
    url(r'^post_runner/$', views.post_runner, name="post_runner"),
    url(r'^post_miles/run/(?P<run_id>[0-9]+)$', views.post_miles, name="post_miles"),
    url(r'^view_runs/$', views.view_runs, name="view_runs"),
    url(r'^charts/line/(?P<runner_id>[0-9]+)$', views.line_graph, name="line_graph"),
]
