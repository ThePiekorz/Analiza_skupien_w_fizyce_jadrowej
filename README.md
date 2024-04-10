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

Głównym celem pracy było znalezienie optymalnych algorytmów klasteryzacji dla poszczególnych zestawów danych, który został osiągnięty poprzez analizę dostępnych rozwiązań. W ramach pracy skupiono się na wytrenowaniu modeli z użyciem różnych hiperparametrów oraz analizie wykresów (sprawdź tune_hyperparameters). Przeprowadzone analizy pokazały skuteczność zaproponowanych rozwiązań oraz ich przydatność w praktyce.

<p align="center" width="100%">
    <img width="50%" src="https://github.com/ThePiekorz/Analiza_skupien_w_fizyce_jadrowej/blob/main/Python_DBSCAN/Data_2.png"> 
</p>

Po przeanalizowaniu wszystkich wyników najlepszym algorytmem okazał
się algorytm DBSCAN. Charakteryzował się on stosunkowo krótkim czasem
wykonywania obliczeń co pozwoliło na lepsze dostrojenie hiperparametrów.
Wyniki na wykresach były zbliżone wynikom oczekiwanym przez zespół fi-
zyków. Na wyróżnienie zasługuje również algorytm afCEC.






