class Constants:
    def __init__(self,algorithm:str,file_name:str)->None:
        self.algorithm = algorithm
        self.file_name = file_name

    def texts(self):
        # a,b,c ou d
        alternative = self.file_name.split('./data/')[1].split('.')[0]

        # 1 ou 2
        evaluate_number_in_str =  '1' if alternative == 'a' or 'b' else '2'

        # Boxplot HC - (1-a)
        title_boxplot = 'Boxplot ' + self.algorithm + ' - (' + evaluate_number_in_str + '-' + alternative
        label_boxplot = 'Value of objective function'
        
        # HC_1_a
        final_file_name = self.algorithm + '_' + evaluate_number_in_str + '_' + alternative

        return title_boxplot,label_boxplot, final_file_name