from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from training_tracker.custom_classes.charts import LineGraph

from training_tracker.custom_classes.run_history import run_history
from .models import Runner, Run, Mile


# Create your views here.

# home page view
def index(request):
    # pass runners context to the template
    runners = Runner.objects.order_by('name')[:]
    context = {'runners' : runners,}

    # render the template
    return render(request, 'training_tracker/index.html', context)

# add run form view
def add_run(request):
    # pass runners context to the template
    runners = Runner.objects.order_by('name')[:]
    return render(request, 'training_tracker/add_run.html', {'runners' : runners})

# add runner form view
def add_runner(request):
    return render(request, 'training_tracker/add_runner.html', {})

# add miles form view
def add_miles(request, run_id):
    # get the run by its primary key
    run = Run.objects.get(pk=run_id)

    # get a range of miles to loop through
    miles = range(int(run.tot_distance))
    return render(request, 'training_tracker/add_miles.html', {'run':run, 'miles':miles})

# post a run to the db
def post_run(request):

    # foreign key runner field
    post_pk = request.POST['runner']
    # date field
    post_date = request.POST['run-date']
    # tot_distance field
    post_distance = request.POST['tot-distance']
    # hours field
    post_hours = request.POST['hours']
    # minutes field
    post_minutes = request.POST['minutes']
    # seconds field
    post_seconds = request.POST['seconds']

    # create a new Run instance and assign fields from post to it
    run = Run()
    run.runner_id = post_pk
    run.date = post_date
    # add 1 to the current amount of runs that the runner has recorded
    run.run_number = Run.objects.filter(pk = post_pk).count() + 1
    run.tot_distance = post_distance
    run.hours = post_hours
    run.minutes = post_minutes
    run.seconds = post_seconds

    # save the run to the db
    run.save()

    # redirect to the add miles form with the run's primary key as a url parameter
    return HttpResponseRedirect(reverse('training_tracker:add_miles', args=(run.pk,)))

# post a runner to the db
def post_runner(request):

    # name field
    post_name = request.POST['runner-name']
    # age field
    post_age = request.POST['runner-age']
    # hours_goal field
    post_hours = request.POST['hours']
    # minues_goal field
    post_minutes = request.POST['minutes']
    # seconds_goal field
    post_seconds = request.POST['seconds']

    # create a new Runner instance and assign fields from post to it
    runner = Runner()
    runner.name = post_name
    runner.age = post_age
    runner.hours_goal = post_hours
    runner.minutes_goal = post_minutes
    runner.seconds_goal = post_seconds

    # save the runner to the db
    runner.save()

    # redirect to the home page
    return HttpResponseRedirect(reverse('training_tracker:index'))

# post miles to the db
def post_miles(request, run_id):
    # get the run associated with the miles by the pk
    run = Run.objects.get(pk=run_id)

    # loop through each mile
    for i in range(int(run.tot_distance)):
        # access minutes and seconds for each mile
        # mile #1 for example will have keys of minutes1 and seconds1
        minutes_key = "minutes" + str(i + 1)
        seconds_key = "seconds" + str(i + 1)

        minutes = request.POST[minutes_key]
        seconds = request.POST[seconds_key]

        # create a new Mile instance and and assign fields from post to it
        mile = Mile()

        mile.run_id = run_id
        mile.mile_number = i
        mile.minutes = minutes
        mile.seconds = seconds

        # save the mile to the db
        mile.save()

    # redirect to the home page
    return HttpResponseRedirect(reverse('training_tracker:index'))

# view run data for runners
def view_runs(request):

    # get run histories for each runner
    runners = Runner.objects.all()
    run_histories = []

    for runner in runners:
        history = run_history(runner.pk).get_data()
        run_histories.append(history)

    # add run_histories to context
    context = {
        "run_histories" : run_histories
    }

    return render(request, 'training_tracker/view_runs.html', context)

# render a line graph
def line_graph(request, runner_id):

    # get history for runner based on runner_id
    history = Runner.objects.get(pk=runner_id).get_run_history()

    # get context data for line graph
    graph = LineGraph()
    context = graph.get_context_data(run_history=history)

    # render the template for line_chart
    return render(request, 'training_tracker/line_chart.html', context)