from django.apps import apps

class run_history:

    # init with runner_id to get run_history for a specified runner
    def __init__(self, runner_id):
        # initialize models to access data objects
        Runner = apps.get_model(app_label="training_tracker",model_name="Runner")
        Run = apps.get_model(app_label="training_tracker",model_name="Run")
        Mile = apps.get_model(app_label="training_tracker",model_name="Mile")

        # data will be a json like object
        # e.g.
        # {
        #   "runner": "Jacob Schwerr",
        #   "runs": [
        #     {
        #       "date": "June 1 2017",
        #       "run_id": 3,
        #       "run_number": 1,
        #       "total_distance": 1,
        #       "hours": 0,
        #         "minutes": 0,
        #         "seconds": 0,
        #         "miles": [
        #           {
        #               "mile_id": 1,
        #               "mile_number": 0,
        #               "minutes": 8,
        #               "seconds": 0
        #           }
        #        ]
        #     }
        #   ]
        # }

        self.data = {}

        # get runner and runs based on runner_id
        self.runner = Runner.objects.get(pk=runner_id)
        self.runs = Run.objects.filter(runner_id=runner_id).order_by("date")

        # add runners name, id, and an empty list of runs to data
        self.data["runner"] = self.runner.name
        self.data["runner_id"] = self.runner.pk
        self.data["runs"] = []

        # if the runner has no recorded runs leave data as it is
        if not self.runs: return

        # add a run object to runs for each run
        for run in self.runs:
            rtemp = {}
            rtemp["date"] = run.date
            rtemp["run_id"] = run.pk
            rtemp["run_number"] = run.run_number
            rtemp["total_distance"] = run.tot_distance
            rtemp["hours"] = run.hours
            rtemp["minutes"] = run.minutes
            rtemp["seconds"] = run.seconds
            rtemp["miles"] = []

            # get all miles for a given run by accessing the runs primary key
            miles = Mile.objects.filter(run_id=run.pk)

            # add a mile object to miles for each mile
            for mile in miles:
                mtemp = {}
                mtemp["mile_id"] = mile.pk
                mtemp["mile_number"] = mile.mile_number
                mtemp["minutes"] = mile.minutes
                mtemp["seconds"] = mile.seconds

                rtemp["miles"].append(mtemp)

            # append the run to runs
            self.data["runs"].append(rtemp)

    # return run_history data
    def get_data(self):
        return self.data