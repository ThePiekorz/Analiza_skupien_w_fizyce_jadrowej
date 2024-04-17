# Cluster analysis in nuclear physics

## Using machine learning methods to identify particles in various nuclear and particle physics experiments 

The aim of the study was to test available algorithms for cluster analysis on data from nuclear and particle physics experiments.

After analysing all the results, the best algorithm turned out to be the
DBSCAN algorithm. It was characterised by a relatively short
to perform the calculations, which allowed for better tuning of the hyperparameters.
The results on the graphs were close to the results expected by the team of fi-
physicists. The afCEC algorithm also deserves a mention.

## Data
Very often, the identification of nuclear reaction products is performed
with signals from two detectors in a stack, operating in coincidence.
signals from two detectors operating in coincidence. This results in a two-dimensional plot in which the individual isotopes
individual isotopes form different types of clusters.

<p align="center" width="100%">
    <img width="50%" src="https://github.com/ThePiekorz/Analiza_skupien_w_fizyce_jadrowej/blob/main/Plots/c12_data.png"> 
</p>

The main aim of the work was to find optimal clustering algorithms for particular data sets, which was achieved by analysing the available solutions. The work focused on training models using different hyperparameters and analysing graphs (check tune_hyperparameters). The analyses carried out showed the effectiveness of the proposed solutions and their usefulness in practice.

<p align="center" width="100%">
    <img width="50%" src="https://github.com/ThePiekorz/Analiza_skupien_w_fizyce_jadrowej/blob/main/Plots/Python_Kmeans/Kmeans_1.png"> 
</p>

## TUNER aka fine-tuning of hyperparameters

The work focused on training models using various
hyperparameters and graph analysis. The results obtained during the study
were analysed in order to adapt the graphs to the intended re-
results. The next step was to tune the hyperparameters using the tu-
GridSearchCV/HalvingGridSearch tuner and re-analysis of the graphs using the best
parameters indicated by the tuner.


<p align="center" width="100%">
    <img width="50%" src="https://github.com/ThePiekorz/Analiza_skupien_w_fizyce_jadrowej/blob/main/tuning_scripts/tune_preview.png"> 
</p>





