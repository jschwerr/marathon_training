from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import Runner, Run, Mile
# Create your views here.

def index(request):
    runners = Runner.objects.order_by('name')[:]
    context = {'runners' : runners,}
    return render(request, 'training_tracker/index.html', context)

def add_run(request):
    runners = Runner.objects.order_by('name')[:]
    return render(request, 'training_tracker/add_run.html', {'runners' : runners})

def add_runner(request):
    return render(request, 'training_tracker/add_runner.html', {})

def add_miles(request, run_id):
    run = Run.objects.get(pk=run_id)
    num_miles = int(run.tot_distance)
    miles = range(num_miles)
    return render(request, 'training_tracker/add_miles.html', {'run':run, 'num_miles': num_miles, 'miles':miles})

def post_run(request):

    post_pk = request.POST['runner']
    post_date = request.POST['run-date']
    post_distance = request.POST['tot-distance']
    post_hours = request.POST['hours']
    post_minutes = request.POST['minutes']
    post_seconds = request.POST['seconds']

    run = Run()
    run.runner = Runner.objects.get(pk = post_pk)
    run.date = post_date
    run.run_number = Run.objects.filter(pk = post_pk).count() + 1
    run.tot_distance = post_distance
    run.hours = post_hours
    run.minutes = post_minutes
    run.seconds = post_seconds

    run.save()

    return HttpResponseRedirect(reverse('training_tracker:add_miles', args=(run.pk,)))

def post_runner(request):
    post_name = request.POST['runner-name']
    post_age = request.POST['runner-age']
    post_hours = request.POST['hours']
    post_minutes = request.POST['minutes']
    post_seconds = request.POST['seconds']

    runner = Runner()
    runner.name = post_name
    runner.age = post_age
    runner.hours_goal = post_hours
    runner.minutes_goal = post_minutes
    runner.seconds_goal = post_seconds

    runner.save()

    return HttpResponseRedirect(reverse('training_tracker:index'))

def post_miles(request, run_id):
    run = Run.objects.get(pk=run_id)

    for i in range(int(run.tot_distance)):
        minutes_key = "minutes" + str(i + 1)
        seconds_key = "seconds" + str(i + 1)

        minutes = request.POST[minutes_key]
        seconds = request.POST[seconds_key]

        mile = Mile()

        mile.run = run
        mile.mile_number = i
        mile.minutes = minutes
        mile.seconds = seconds

        mile.save()

    return HttpResponseRedirect(reverse('training_tracker:index'))

def view_runs(request):
    runners = Runner.objects.all()
    run_histories = []

    for runner in runners:
        run_history = []
        runs = Run.objects.filter(runner = runner.pk).order_by('date')

        for run in runs:
            miles = Mile.objects.filter(run = run.pk).order_by('mile_number')
            mile_history = []

            for mile in miles:
                mile_history.append({"mile":mile})

            run_history.append({"run":mile_history})

        run_histories.append(
            {
                "name":runner.name,
                "run_history":run_history
            })

    context = {
        "run_histories" : run_histories
    }

    return render(request, 'training_tracker/view_runs.html', context)