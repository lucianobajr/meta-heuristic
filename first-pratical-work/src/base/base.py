import pandas as pd
import sys

from metrics.metrics import Metrics
from core.packages.hill_climping import HillClimbing
from core.packages.ils import ILS
from export.export import Export

import numpy as np

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

        # number_text_to_title = 1 if self.csv_file_name.split('.')[0] == 'a' or 'b' else 2 

        title_boxplot_ils = 'Boxplot ILS - Evaluate-'+ self.csv_file_name.split('.')[0]
        file_name_ils = 'ILS-' + self.csv_file_name.split('.')[0]
        
        title_boxplot_hc = 'Boxplot HC - Evaluate' + self.csv_file_name.split('.')[0]
        file_name_hc = 'HC-' + self.csv_file_name.split('.')[0]
        
        export_hill_climbing = Export(metrics_hc,"HC",title_boxplot_hc,'Value of objective function',file_name_hc)
        export_ils = Export(metrics_ils,"ILS",title_boxplot_ils,'Value of objective function',file_name_ils)
        
        hill_climbing = HillClimbing(x_low=x_low,x_high=x_high,y_low=y_low,y_high=y_high,type=evaluate)
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

        for i    in range(30):
            result = hill_climbing.heuristic()    
            metrics_hc.insert_result(result)
            problem, value = ils.heuristic()
            metrics_ils.insert_result(value)

        export_hill_climbing.gerenate()
        export_ils.gerenate()
        
def bootstrap():

    base = Base(csv_file_name=sys.argv[2])
    base.run()