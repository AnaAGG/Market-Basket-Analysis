import pandas as pd
from mlxtend.frequent_patterns import apriori, association_rules # para hacer el modelo apriori

def limpiar_nombre(x):
    if isinstance(x, str):
        x = eval(x)
    return ', '.join(x).lower() if isinstance(x, frozenset) else str(x).lower()

def recomendar(producto, dataframe_reglas):
    """
    Devuelve recomendaciones basadas en reglas de asociación para un producto específico.

    Parámetros:
    - producto: string con el nombre del producto
    - reglas: DataFrame de reglas generadas con association_rules

    Devuelve:
    - DataFrame con consequents, confidence y lift, ordenado por lift descendente
    """
    reglas_filtradas = dataframe_reglas[dataframe_reglas['antecedents'].apply(lambda x: producto in x)]
    
    if reglas_filtradas.empty:
        print(f"No se encontraron recomendaciones para '{producto}'")

    recomendaciones = reglas_filtradas[['consequents', 'confidence', 'lift']]
    return recomendaciones.sort_values(by='lift', ascending=False).reset_index(drop=True)

def mostrar_recomendaciones_interactivas(producto, dataframe_reglas):
    recomendaciones = recomendar(producto, dataframe_reglas)
    if recomendaciones is not None and not recomendaciones.empty:
        display(recomendaciones)
        
        
def generar_reglas_interactivo(min_support, min_confidence, dataframe):
    itemsets = apriori(dataframe, min_support=min_support, use_colnames=True)
    reglas = association_rules(itemsets, metric="confidence", min_threshold=min_confidence)
    print(f"🔍 Reglas generadas: {reglas.shape[0]}")
    display(reglas[['antecedents', 'consequents', 'support', 'confidence', 'lift']].head(10))
