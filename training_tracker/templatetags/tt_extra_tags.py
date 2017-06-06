from django import template
from ..custom_classes.charts import LineGraph
from ..models import Runner, Run, Mile
from django.urls import reverse

# variable to register extra tabs
register = template.Library()

# custom tag to include line_chart.html
# gets context data to display a chart
# plugs line_chart template into another template - see view_runs as an example
@register.inclusion_tag('training_tracker/line_chart.html')
def run_history_chart_context(runner_id):
    # get run history for the runner with the given runner_id
    history = Runner.objects.get(pk=runner_id).get_run_history()

    # get context data for a line graph that displays history
    graph = LineGraph()
    context = graph.get_context_data(run_history=history)

    return context

# tag used to add active class to active nav link
@register.simple_tag
def navactive(request, urls):
    if request.path in ( reverse(url) for url in urls.split() ):
        return "active"
    return ""