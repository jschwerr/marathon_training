from django.db import models

from training_tracker.custom_classes import run_history


# Represents a runner with name, age, and goal information
class Runner(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField()
    hours_goal = models.IntegerField()
    minutes_goal = models.IntegerField()
    seconds_goal = models.IntegerField()

    # printing a runner will return their name
    def __str__(self):
        return self.name

    # returns run history for this runner
    def get_run_history(self):
        data = run_history.run_history(self.pk).get_data()
        return data

# Represents a run. Runner_id associates this run with the runner who recorded it.
# run_number is relative to the runner (e.g. run_number = 1 is the first recorded run for this runner)
# record time and date information for the run
class Run(models.Model):
    runner_id = models.ForeignKey(Runner, on_delete=models.CASCADE)
    run_number = models.IntegerField()
    tot_distance = models.IntegerField(default=0)
    hours = models.IntegerField(default=0)
    minutes = models.IntegerField(default=0)
    seconds = models.IntegerField(default=0)
    date = models.DateField()

    # print string for a run
    def __str__(self):
        return "ID: " + str(self.pk) + \
               ", Miles: " + str(self.tot_distance) + \
               ", Time: " + "{0}:{1}:{2}".format(self.hours, self.minutes, self.seconds)

# Represents a mile. Run_id associates a mile to the run it was recorded for. Mile number is similar to run_number
# record minutes and seconds for the mile
class Mile(models.Model):
    run_id = models.ForeignKey(Run, on_delete=models.CASCADE)
    mile_number = models.IntegerField()
    minutes = models.IntegerField(default=0)
    seconds = models.IntegerField(default=0)

    # print string for mile
    def __str__(self):
        return "ID: " + str(self.run.pk) + \
               ", Mile time: " + "{0}:{1}:{2}".format(self.hours, self.minutes, self.seconds)
