import sys
import pandas as pd

from constants.constants import Constants
from core.packages.hill_climping import HillClimbing
from core.packages.ils import ILS
from export.export import Export
from metrics.metrics import Metrics

class Base:
    def __init__(self,csv_file_name:str)->None:
        self.csv_file_name = csv_file_name

    def run(self):
        base = pd.read_csv(self.csv_file_name)

        evaluate = base['evaluate'][0]
        
        x_low=int(base['x_low'][0])
        x_high=int(base['x_high'][0])
        y_low=int(base['y_low'][0])
        y_high=int(base['y_high'][0])

        metrics_hc = Metrics()
        metrics_ils = Metrics()

        constants_hc = Constants(algorithm="HC",file_name=self.csv_file_name)        
        title_boxplot_hc,label_boxplot_hc, final_file_name_hc = constants_hc.texts()
        
        export_hill_climbing = Export(
            metrics=metrics_hc,
            algorithm="HC",
            title_boxplot=title_boxplot_hc,
            label_boxplot=label_boxplot_hc,
            file_name=final_file_name_hc
        )
        
        constants_ils = Constants(algorithm="ILS",file_name=self.csv_file_name)        
        title_boxplot_ils,label_boxplot_ils, final_file_name_ils = constants_ils.texts()

        export_ils = Export(
            metrics=metrics_ils,
            algorithm="ILS",
            title_boxplot=title_boxplot_ils,
            label_boxplot=label_boxplot_ils,
            file_name=final_file_name_ils
        )
        
        hill_climbing = HillClimbing(
            x_low=x_low,
            x_high=x_high,
            y_low=y_low,
            y_high=y_high,
            type=evaluate
        )

        ils = ILS(
            step_size=1,
            max_iterations=100, 
            max_restarts=5,
            x_low=x_low, 
            x_high=x_high, 
            y_low=y_low,
            y_high=y_high,
            type=evaluate
        )

        for _ in range(30):
            result = hill_climbing.heuristic()    
            metrics_hc.insert_result(result)
            _, value = ils.heuristic()
            metrics_ils.insert_result(value)

        export_hill_climbing.gerenate()
        export_ils.gerenate()
        
def bootstrap():
    base = Base(csv_file_name=sys.argv[2])
    base.run()