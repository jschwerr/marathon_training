from django.conf.urls import url

from . import views

app_name = 'training_tracker'
urlpatterns = [
    # /training_tracker/ -> show home page
    url(r'^$', views.index, name="index"),
    # /training_tracker/regiter/ registration page
    url(r'^register/$', views.register, name="register"),
    # /training_tracker/add_run -> show add run form
    url(r'^add_run/$', views.add_run, name="add_run"),
    # /training_tracker/edit_runner -> edit a runner
    url(r'^edit_runner/$', views.edit_runner, name="edit_runner"),
    # /training_tracker/add_miles/run/(run_id) -> show add miles for for given run
    url(r'^add_miles/(?P<run_id>[0-9]+)$', views.add_miles, name="add_miles"),

    # /training_tracker/view_runs -> show runs
    url(r'^view_runs/$', views.view_runs, name="view_runs"),
    # /training-tracker/view_goals -> show goals
    url(r'view_goals/$', views.view_goals, name="view_goals"),
    # /training_tracker/charts/line/(run_id) -> show line_graph for given runner
    url(r'^charts/line/(?P<runner_id>[0-9]+)$', views.line_graph, name="line_graph"),
]
