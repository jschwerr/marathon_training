import plotly.offline as opy
import plotly.graph_objs as gobs
from django.views.generic.base import TemplateView
import datetime

class LineGraph(TemplateView):
    # def __init__(self, template_name):
    #     self.template_name = 'training_tracker/line_chart'

    def get_context_data(self, run_history, **kwargs):
        context = super(LineGraph, self).get_context_data(**kwargs)

        run_dates = []
        date_and_distance = []

        for run in run_history['runs']:
            run_dates.append(run["date"])
            date_and_distance.append({"date": run["date"], "total_distance": run["total_distance"]})

        start_date = min(run_dates)
        end_date = max(run_dates)

        second_in_a_day = 86400

        dates = []

        for x in range(int(((end_date - start_date).total_seconds())/second_in_a_day) + 1):
            dates.append(start_date + datetime.timedelta(days=x))

        x = [date for date in dates]
        y = []

        for date in dates:
            if date in run_dates:
                for dr in date_and_distance:
                    if date == dr["date"]:
                        y.append(dr["total_distance"])
            else:
                y.append(0)

        print(y)

        trace1 = gobs.Scatter(x=x, y=y, marker={'color': 'red', 'symbol': 104, 'size': "10"},
                            mode="lines", name='1st Trace')

        data = gobs.Data([trace1])
        layout = gobs.Layout(title="Distance Ran", xaxis={'title': 'Date'}, yaxis={'title': 'Distance'})
        figure = gobs.Figure(data=data, layout=layout)
        div = opy.plot(figure, auto_open=False, output_type='div')

        context['graph'] = div

        return context

