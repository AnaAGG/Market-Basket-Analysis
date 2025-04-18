import pandas as pd

def exploracion_dataframe(dataframe, mostrar_unicos=True, max_unicos=10, mostrar_descriptivas=True):
    """
    Realiza un análisis exploratorio básico de un DataFrame.

    Parámetros:
    - dataframe (DataFrame): DataFrame a explorar.
    - mostrar_unicos (bool): Mostrar valores únicos en columnas categóricas.
    - max_unicos (int): Número máximo de valores únicos a mostrar por columna.
    - mostrar_descriptivas (bool): Mostrar estadísticas descriptivas de columnas numéricas.

    """
    print(f"\nEl dataframe tiene {dataframe.shape[0]} filas y {dataframe.shape[1]} columnas.")
    print("-" * 60)
    
    # Duplicados
    duplicados = dataframe.duplicated().sum()
    porcentaje_duplicados = round((duplicados / dataframe.shape[0]) * 100, 2)
    print(f"Filas duplicadas: {duplicados} que corresponde con un {porcentaje_duplicados} % del total de los datos")
    print("-" * 60)

    # Nulos
    dataframe_nulos = dataframe.isnull().mean() * 100
    dataframe_nulos = dataframe_nulos[dataframe_nulos > 0].sort_values(ascending=False)
    if dataframe_nulos.empty:
        print("No hay valores nulos.")
    else:
        print("Columnas con valores nulos (%):")
        display(dataframe_nulos.to_frame(name="%_nulos"))
    print("-" * 60)

    # Tipos de datos
    print("Tipos de datos:")
    display(pd.DataFrame(dataframe.dtypes, columns=["tipo_dato"]))
    print("-" * 60)

    # Columnas constantes
    constantes = [col for col in dataframe.columns if dataframe[col].nunique() == 1]
    if constantes:
        print(f"Columnas constantes (1 valor único): {constantes}")
    else:
        print("No hay columnas constantes.")
    print("-" * 60)

    # Columnas categóricas
    cat_cols = dataframe.select_dtypes(include="object").columns.tolist()
    if cat_cols:
        print(f"Columnas categóricas: {cat_cols}")
        if mostrar_unicos:
            for col in cat_cols:
                print(f"\n{col.upper()} - valores únicos:")
                display(dataframe[col].value_counts(dropna=False).head(max_unicos))
    else:
        print("No hay columnas categóricas.")
    print("-" * 60)

    # Columnas numéricas
    num_cols = dataframe.select_dtypes(include="number").columns.tolist()
    if num_cols and mostrar_descriptivas:
        print("Estadísticas de columnas numéricas:")
        display(dataframe[num_cols].describe().T)
    elif not num_cols:
        print("No hay columnas numéricas.")
    print("-" * 60)
    
    
def clasificar_cesta(n, p25, p75, p95):
    """
    Clasifica una factura según el número de productos únicos.

    Parámetros:
    - n (int): número de productos únicos en la factura
    - p25, p75, p95 (float): percentiles de referencia

    Retorna:
    - str: categoría de tamaño de cesta ("Pequeña", "Media", "Grande", "Muy grande")
    """
    if n <= p25:
        return "Pequeña"
    elif n <= p75:
        return "Media"
    elif n <= p95:
        return "Grande"
    else:
        return "Muy grande"