from django import template
from ..custom_classes.charts import LineGraph
from ..models import Runner, Run, Mile
from django.urls import reverse

register = template.Library()

@register.inclusion_tag('training_tracker/line_chart.html')
def run_history_chart_context(runner_id):
    history = Runner.objects.get(pk=runner_id).get_run_history()

    graph = LineGraph()
    context = graph.get_context_data(run_history=history)

    return context

@register.simple_tag
def navactive(request, urls):
    if request.path in ( reverse(url) for url in urls.split() ):
        return "active"
    return ""