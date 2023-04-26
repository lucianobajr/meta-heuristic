from base.base import bootstrap

if __name__ == "__main__":
    bootstrap()


    ''' 
    # Executa o algoritmo 30 vezes
    metrics_hc = Metrics()
    metrics_ils = Metrics()
    export_hill_climbing = Export(metrics_hc,'Boxplot of HC results','Value of objective function','HC')
    export_ils = Export(metrics_ils,'Boxplot of ILS results','Value of objective function','ILS')

    hill_climbing = HillClimbing(-5, 5, -5, 5,"first")

    ils = ILS(
        step_size=1,
        max_iterations=1000, 
        max_restarts=5,
        x_low=-5, 
        x_high=5, 
        y_low=-5, 
        y_high=5,
        type="first"
    )

    for i in range(30):
        result = hill_climbing.heuristic()    
        metrics_hc.insert_result(result)
        solution, value = ils.ils()
        metrics_ils.insert_result(value)
        
        # print(f"Iteração {i+1}: {result}")
    
    export_hill_climbing.gerenate()
    export_ils.gerenate()
    '''
