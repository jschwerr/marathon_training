import math
import numpy as np

class RiegelPredictor:
    def __init__(self, runs):
        self.runs = runs
        self.times = []
        self.speeds = []
        self.meters = []
        self.coefficient = 0

        if len(runs) > 0:
            for r in runs:
                time = self.get_seconds(r.hours, r.minutes, r.seconds)
                mil = r.tot_distance
                met = mil * 1609.344

                self.times.append(time)
                self.speeds.append(met/time)
                self.meters.append(met)

            self.coefficient = self.get_riegel_coefficient(self.speeds,self.meters)

    def predict_marathon_time(self):
        if len(self.runs) > 1:
            avg_time = np.array(self.times).mean()
            avg_dist = np.array(self.meters).mean()
            tot_runs = len(self.meters)

            runs_weight = 10

            alpha = runs_weight / (runs_weight + tot_runs)

            coeff = alpha * 1.06 + (1 - alpha) * self.coefficient

            print(alpha, coeff)
            marathon_seconds = avg_time * (((26.2 * 1609.344) / avg_dist) ** coeff)
            m,s = divmod(marathon_seconds,60)
            h,m = divmod(m,60)

            return "You're on track to run a " + "%d:%02d:%02d" % (h, m, s) + " marathon!"

        else:
            return "You currently have " + str(len(self.runs)) + " runs entered. Add more runs to " + \
            "get your marathon prediction!"
    def get_seconds(self, hours, minutes, seconds):
        return (hours * (60 ** 2)) + (minutes * 60) + seconds

    def get_riegel_coefficient(self, speeds, meters):
        if len(speeds) <= 1:
            return 1.06
        else:
            ln_s = [math.log(x, math.e) for x in speeds]
            ln_m = [math.log(x, math.e) for x in meters]

            return np.polyfit(ln_m,ln_s,1)[0] * -1 + 1



