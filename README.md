# Analiza skupień w fizyce jądrowej

## Wykorzystanie metod uczenia maszynowego do identyfikacji cząstek w różnych eksperymentach fizyki jądrowej i cząstek

Celem pracy było przetestowanie dostępnych algorytmów do analizy sku-
pień na danych pochodzących z eksperymentów fizyki jądrowej i cząstek.
Bardzo często identyfikację produktów reakcji jądrowych przeprowadza się
mając do dyspozycji sygnały z dwóch detektorów, ułożonych w stos, dzia-
łających w koincydencji. Efektem tego jest dwuwymiarowy plot, na którym
poszczególne izotopy tworzą różnego rodzaje skupienia.

<p align="center" width="100%">
    <img width="50%" src="https://github.com/ThePiekorz/Analiza_skupien_w_fizyce_jadrowej/blob/main/Dane_podstawowe_plot/c12_data.png"> 
</p>

Do odróżnienia skupień użyto nienadzorowanych metod uczenia maszynowego takich jak DBSCAN, OPTICS, MeanShift czy afCEC. Duża część z nich jest
zaimplementowana w bibliotece SciKitLearn.
