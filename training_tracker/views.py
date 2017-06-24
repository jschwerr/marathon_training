from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from training_tracker.custom_classes.charts import LineGraph
from training_tracker.custom_classes.RiegelPredictor import RiegelPredictor

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django import forms
from django.forms import formset_factory
from .forms import UserForm, RunnerForm, RunForm, MileForm

from training_tracker.custom_classes.run_history import run_history
from .models import Runner, Run, Mile

from django.views.generic import UpdateView


# Create your views here.

# home page view
def index(request):
    # pass runners context to the template
    runners = Runner.objects.order_by('user')[:]
    context = {'runners': runners, }

    # render the template
    return render(request, 'training_tracker/index.html', context)

def register(request):

    if request.method == 'POST':
        uf = UserForm(data=request.POST)
        rf = RunnerForm(data=request.POST)

        if uf.is_valid() and rf.is_valid():
            user = uf.save(commit=False)

            username = user.username
            email = user.email
            password = user.password

            if not (User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists()):
                user = uf.save()
                user.set_password(password)
                user.save()

                print(user)
                runner = rf.save(commit=False)
                runner.user = user
                rf.save()

                user_auth = authenticate(username = username, password = password)
                login(request, user_auth)

                return HttpResponseRedirect('/')
            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        uf = UserForm()
        rf = RunnerForm()

        return render(request, 'training_tracker/register.html', {'uf' : uf, 'rf' : rf})

# add run form view
def add_run(request):
    if request.method == 'POST':
        rf = RunForm(request.POST)
        if rf.is_valid():
            run = rf.save(commit=False)
            runner_id = request.user.runner.pk
            run.runner_id = runner_id
            run.run_number = Run.objects.filter(pk=runner_id).count() + 1
            run.save()

            # redirect to the add miles form with the run's primary key as a url parameter
            return HttpResponseRedirect(reverse('training_tracker:add_miles', args=(run.pk,)))
    else:
        form = RunForm()

    return render(request, 'training_tracker/add_run.html', {"form":form})


# add miles form view
def add_miles(request, run_id):
    run = Run.objects.get(pk=run_id)
    numMiles = int(run.tot_distance)

    MileFormSet = formset_factory(MileForm, extra = numMiles)

    if request.method == 'POST':
        mf = MileFormSet(request.POST)
        mn = 1

        for mile in mf:
            if mile.is_valid():
                # get the run by its primary key
                m = mile.save(commit=False)
                m.run_id = run_id
                m.mile_number = mn
                m.save()

                mn += 1
        return HttpResponseRedirect(reverse('training_tracker:index'))

    else:
        # get a range of miles to loop through
        form_set = MileFormSet()
    return render(request, 'training_tracker/add_miles.html', {'form_set': form_set})

from django.contrib import messages

class edit_runner(UpdateView):
    form_class = RunnerForm
    fields = ['age','hours_goal','minutes_goal','seconds_goal']

# def edit_runner(request):
#     if request.method == 'POST':
#         rf = RunnerForm(data=request.POST, edit=False)
#         if rf.is_valid():
#             runner = Runner.objects.get(pk=request.user.runner.pk)
#             rf = RunnerForm(data=request.POST, instance=runner)
#             r = rf.save()
#
#             # redirect to the add miles form with the run's primary key as a url parameter
#             return HttpResponseRedirect(reverse('training_tracker:index'))
#     else:
#         form = RunnerForm()
#
#         return render(request, 'training_tracker/edit_runner.html', {"form" : form})

# view run data for runners
def view_runs(request):
    context = {}
    if not request.user.is_anonymous():
        runs = Run.objects.filter(runner=request.user.runner.pk)
        prediction_msg = RiegelPredictor(runs).predict_marathon_time()
        rh = run_history(request.user.runner.pk).get_data()
        context = {'run_history': rh, 'prediction_msg': prediction_msg}
    return render(request, 'training_tracker/view_runs.html', context)


# view goals for each runner
def view_goals(request):
    return render(request, 'training_tracker/view_goals.html')


# render a line graph
def line_graph(request, runner_id):
    # get history for runner based on runner_id
    history = User.objects.get(pk=runner_id).get_run_history()

    # get context data for line graph
    graph = LineGraph()
    context = graph.get_context_data(run_history=history)

    # render the template for line_chart
    return render(request, 'training_tracker/line_chart.html', context)
