import matplotlib.pyplot as plt
from prettytable import PrettyTable
from metrics.metrics import Metrics

class Export:
    def __init__(self,metrics:Metrics,title_boxplot:str,label_boxplot:str,file_name:str)->None:
        self.metrics = metrics
        self.title_boxplot = title_boxplot
        self.label_boxplot = label_boxplot
        self.file_name = file_name

    def gerenate(self):
        # Criar a tabela
        table = PrettyTable()
        table.field_names = ["Mean", "Min", "Max","STD"]
        # Adicionar dados à tabela
        table.add_row([self.metrics.mean(),self.metrics.min(),self.metrics.max(),self.metrics.standard_deviation()])

        # Imprimir a tabela
        print(table)

        # Generate boxplot
        fig, ax = plt.subplots()
        ax.boxplot(self.metrics.results)
        ax.set_title(self.title_boxplot)
        ax.set_ylabel(self.label_boxplot)
        
        # Save file
        fig.savefig('./out/'+self.file_name+'.png')