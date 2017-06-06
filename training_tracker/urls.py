from django.conf.urls import url

from . import views

app_name = 'training_tracker'
urlpatterns = [
    # /training_tracker/ -> show home page
    url(r'^$', views.index, name="index"),
    # /training_tracker/add_run -> show add run form
    url(r'^add_run/$', views.add_run, name="add_run"),
    # /training_tracker/add_runner -> show add runner form
    url(r'^add_runner/$', views.add_runner, name="add_runner"),
    # /training_tracker/add_miles/run/(run_id) -> show add miles for for given run
    url(r'^add_miles/run/(?P<run_id>[0-9]+)$', views.add_miles, name="add_miles"),
    # /training_tracker/post_run -> url to handle logic for posting a run
    url(r'^post_run/$', views.post_run, name="post_run"),
    # /training_tracker/post_runner -> url to handle logic for posting a runner
    url(r'^post_runner/$', views.post_runner, name="post_runner"),
    # /training_tracker/post_miles/run/(run_id) -> url to handle logic for posting a mile for a run
    url(r'^post_miles/run/(?P<run_id>[0-9]+)$', views.post_miles, name="post_miles"),
    # /training_tracker/view_runs -> show runs
    url(r'^view_runs/$', views.view_runs, name="view_runs"),
    # /training_tracker/charts/line/(run_id) -> show line_graph for given runner
    url(r'^charts/line/(?P<runner_id>[0-9]+)$', views.line_graph, name="line_graph"),
]
