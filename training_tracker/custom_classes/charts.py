import plotly.offline as opy
import plotly.graph_objs as gobs
from django.views.generic.base import TemplateView
import datetime

# runner history line graph
class LineGraph(TemplateView):
    # def __init__(self, template_name):
    #     self.template_name = 'training_tracker/line_chart'

    # get context to pass to line graph template
    def get_context_data(self, run_history, **kwargs):

        # runner doesn't have any recorded runs
        if not run_history:
            context = {"no_data" : "no data"}
            return context

        # get context from TemplateView super class
        context = super(LineGraph, self).get_context_data(**kwargs)

        # dates a runner has ran
        run_dates = []

        # list of dicts with date and distance for each run
        date_and_distance = []

        for run in run_history['runs']:
            # add the date the runner has ran
            run_dates.append(run["date"])
            # add the date and the distance of the run
            date_and_distance.append({"date": run["date"], "total_distance": run["total_distance"]})

        # date of first run
        start_date = min(run_dates)

        # date of most recent run
        end_date = max(run_dates)

        second_in_a_day = 86400

        # holds each date between start and end dates
        dates = []

        # loop through all dates between start and end date
        for x in range(int(((end_date - start_date).total_seconds())/second_in_a_day) + 1):
            dates.append(start_date + datetime.timedelta(days=x))

        # x axis will be all dates between start and end
        x = [date for date in dates]
        y = []

        # if runner ran on date append total distance to y otherwise append 0 (runner ran 0 miles that day)
        for date in dates:
            if date in run_dates:
                for dr in date_and_distance:
                    if date == dr["date"]:
                        y.append(dr["total_distance"])
            else:
                y.append(0)

        # create line graph

        # trace out x vs. y
        trace1 = gobs.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': "10"},
                            mode="lines", name='1st Trace')

        data = gobs.Data([trace1])
        layout = gobs.Layout(title="Distance Ran", titlefont=dict(size="24px"),xaxis={'title': 'Date'}, yaxis={'title': 'Distance'})
        figure = gobs.Figure(data=data, layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        # add graph to context to be accessed from template
        context['graph'] = div

        return context

