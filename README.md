
> ⚠️ Este proyecto está actualmente en desarrollo. Algunas funcionalidades o resultados pueden cambiar.


# 🛒 Market Basket Analysis en el Retail

![portada](imagenes/portada.png)

Este proyecto analiza patrones de compra en supermercados mediante técnicas de *Market Basket Analysis*. Su objetivo es descubrir asociaciones frecuentes entre productos para mejorar decisiones de marketing y promociones cruzadas.



## Objetivo del proyecto

Desarrollar un sistema de análisis de cestas de la compra que permita identificar combinaciones de productos frecuentemente adquiridos juntos. Esta información puede utilizarse para mejorar estrategias de venta cruzada, recomendaciones personalizadas y diseño de promociones.



## Qué problema soluciona

Las cadenas de supermercados gestionan miles de productos simultáneamente, lo que dificulta comprender los hábitos de compra de los clientes. Sin un análisis estructurado, se pierden oportunidades de generar mayor valor a través de recomendaciones inteligentes y promociones basadas en datos.

Este proyecto resuelve esa necesidad mediante la identificación automática de productos comprados conjuntamente, optimizando las acciones comerciales.


## Contexto del problema

En el sector del retail, comprender los patrones de compra es clave para aumentar las ventas y mejorar la experiencia del cliente. Las técnicas de *Market Basket Analysis* permiten extraer reglas de asociación a partir del histórico de transacciones, revelando afinidades entre productos como “quien compra pan también compra mantequilla”.

Estas técnicas han sido utilizadas con éxito en e-commerce, supermercados y servicios por sus aplicaciones directas en *product bundling*, *layout optimization* y *targeted marketing*.


## Datos utilizados


- **Fuente**: [Market Basket Analysis Dataset en Kaggle](https://www.kaggle.com/datasets/aslanahmedov/market-basket-analysis)

- **Licencia**: Los archivos de datos están licenciados como © Original Authors según se indica en la página del dataset.

- **Contenido**:

  - `InvoiceNo`: ID de la factura (una compra).

  - `StockCode` y `Description`: Identificador y nombre del producto.

  - `Quantity`: Número de unidades adquiridas.

  - `InvoiceDate`: Fecha y hora de la compra.

  - `Country`: País del comprador.


## Metodología

1. **Análisis exploratorio**:

   - Estadísticas descriptivas.

   - Visualizaciones de productos más vendidos.

   - Comportamiento por país y frecuencia de compra.


2. **Preprocesamiento**:

   - Filtrado de datos relevantes.

   - Transformación a formato *basket* (cliente vs productos).

   - Codificación binaria.

3. **Modelado con Apriori + Reglas de Asociación**:

   - Generación de ítems frecuentes.

   - Extracción de reglas utilizando métricas como *support*, *confidence* y *lift*.

   - Interpretación de asociaciones relevantes y no triviales.



## Estructura del proyecto

```
Market-Basket-Analysis/
├── data/
│   ├── retail.xlsx                          # Dataset original
│   ├── retail_limpio.csv                    # Datos limpios tras el preprocesamiento
│   ├── retail_transacciones_transformado.csv # Datos en formato transacción
│   ├── retail_uk_transformado.csv           # Datos filtrados para Reino Unido
│   └── rules_uk.csv                         # Reglas generadas con Apriori
│
├── imagenes/
│   └── funcionamiento-apriori-modelo.png    # Visualizaciones de soporte para el README o resultados
│
├── notebooks/
│   ├── 01-analisis-exploratorio.ipynb       # Análisis inicial del dataset
│   ├── 02-preprocesamiento.ipynb            # Limpieza y transformación de datos
│   └── 03-modelo-market-basket_uk.ipynb     # Aplicación del modelo Apriori
│
├── src/
│   ├── soporte_exploracion.py               # Funciones auxiliares para el EDA
│   └── soporte_modelo.py                    # Funciones auxiliares para modelado
│
└── README.md                                # Documentación del proyecto
```

---

## Tecnologías y librerías utilizadas

- **Lenguaje**: Python 3.12

- **Entorno**: Jupyter Notebooks

- **Librerías principales**:

  - `pandas`, `numpy`: manipulación de datos

  - `matplotlib`, `seaborn`: visualización

  - `mlxtend`: implementación de Apriori y reglas de asociación

  - `scikit-learn`: soporte para transformaciones


## Instalación

Para instalar las dependencias del proyecto, ejecuta:

```bash
pip install -r requirements.txt
```
Asegúrate de hacerlo dentro de un entorno virtual para evitar conflictos con otros proyectos.


## Posibles mejoras y próximos pasos

- Aplicación del modelo a otros países o periodos temporales.

- Incorporar segmentación de clientes para reglas personalizadas.

- Experimentar con algoritmos alternativos como Eclat o Bayesianos.

- Despliegue del análisis en una interfaz interactiva con Streamlit.


## Autora

Este proyecto fue desarrollado por [AnaAGG](https://www.linkedin.com/in/ana-garcia-garcia-/) como parte de su portfolio profesional en Data Science.
