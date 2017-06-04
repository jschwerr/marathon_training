from .apps import TrainingTrackerConfig
from django.apps import apps

class run_history:
    def __init__(self, runner_id):
        Runner = apps.get_model(app_label='training_tracker',model_name='Runner')
        Run = apps.get_model(app_label='training_tracker',model_name='Run')
        Mile = apps.get_model(app_label='training_tracker',model_name='Mile')

        self.data = {}
        self.runner = Runner.objects.get(pk=runner_id)
        self.runs = Run.objects.filter(runner_id=runner_id).order_by('date')

        self.data['runner'] = self.runner.name
        self.data['runs'] = []
        for run in self.runs:
            rtemp = {}
            rtemp['date'] = run.date
            rtemp['run_id'] = run.pk
            rtemp['run_number'] = run.run_number
            rtemp['total_distance'] = run.tot_distance
            rtemp['hours'] = run.hours
            rtemp['minutes'] = run.minutes
            rtemp['seconds'] = run.seconds
            rtemp['miles'] = []

            miles = Mile.objects.filter(run_id=run.pk)

            for mile in miles:
                mtemp = {}
                mtemp['mile_id'] = mile.pk
                mtemp['mile_number'] = mile.mile_number
                mtemp['minutes'] = mile.minutes
                mtemp['seconds'] = mile.seconds

                rtemp['miles'].append(mtemp)

            self.data['runs'].append(rtemp)

    def get_data(self):
        return self.data