# Enlgish Version
[![en](https://img.shields.io/badge/lang-en-red.svg)](https://github.com/jonatasemidio/multilanguage-readme-pattern/blob/master/README.md)

# Analiza skupień w fizyce jądrowej

## Wykorzystanie metod uczenia maszynowego do identyfikacji cząstek w różnych eksperymentach fizyki jądrowej i cząstek

Celem pracy było przetestowanie dostępnych algorytmów do analizy sku-
pień na danych pochodzących z eksperymentów fizyki jądrowej i cząstek.

Po przeanalizowaniu wszystkich wyników najlepszym algorytmem okazał
się algorytm DBSCAN. Charakteryzował się on stosunkowo krótkim czasem
wykonywania obliczeń co pozwoliło na lepsze dostrojenie hiperparametrów.
Wyniki na wykresach były zbliżone wynikom oczekiwanym przez zespół fi-
zyków. Na wyróżnienie zasługuje również algorytm afCEC.

## Dane
Dane pochodzić będą z kilku eksperymentów fizyki jądrowej i cząstek. Bardzo często identyfikację produktów reakcji jądrowych przeprowadza się
mając do dyspozycji sygnały z dwóch detektorów, ułożonych w stos, dzia-
łających w koincydencji. Efektem tego jest dwuwymiarowy plot, na którym
poszczególne izotopy tworzą różnego rodzaje skupienia.

<p align="center" width="100%">
    <img width="50%" src="https://github.com/ThePiekorz/Analiza_skupien_w_fizyce_jadrowej/blob/main/Plots/c12_data.png"> 
</p>

Głównym celem pracy było znalezienie optymalnych algorytmów klasteryzacji dla poszczególnych zestawów danych, który został osiągnięty poprzez analizę dostępnych rozwiązań. W ramach pracy skupiono się na wytrenowaniu modeli z użyciem różnych hiperparametrów oraz analizie wykresów (sprawdź tune_hyperparameters). Przeprowadzone analizy pokazały skuteczność zaproponowanych rozwiązań oraz ich przydatność w praktyce.

<p align="center" width="100%">
    <img width="50%" src="https://github.com/ThePiekorz/Analiza_skupien_w_fizyce_jadrowej/blob/main/Plots/Python_Kmeans/Kmeans_1.png"> 
</p>

## TUNER czyli dostrajanie hiperparametrów

W ramach pracy skupiono się na wytrenowaniu modeli z użyciem różnych
hiperparametrów oraz analizie wykresów. Wyniki uzyskane podczas badań
zostały przeanalizowane w celu dostosowania wykresów do zamierzonych re-
zultatów. Kolejnym krokiem było dostrojenie hiperparametrów z użyciem tu-
nera GridSearchCV/HalvingGridSearch oraz ponowna analiza wykresów z użyciem najlepszych
parametrów wskazanych przez tuner.

<p align="center" width="100%">
    <img width="50%" src="https://github.com/ThePiekorz/Analiza_skupien_w_fizyce_jadrowej/blob/main/tuning_scripts/tune_preview.png"> 
</p>





