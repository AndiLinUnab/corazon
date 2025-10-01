# Predictor de Problemas Cardiacos

## Descripción

Esta aplicación permite predecir si una persona sufrirá o no de problemas cardíacos en base a su **edad** y **nivel de colesterol**. El modelo fue entrenado utilizando un clasificador **Support Vector Classifier (SVC)** y un conjunto de datos que contiene información sobre la edad, el colesterol y si la persona tiene problemas cardíacos o no.

La aplicación toma los valores de **edad** y **colesterol** a través de sliders interactivos y realiza una predicción utilizando el modelo entrenado. La predicción se muestra con una imagen que depende de si el resultado es positivo o negativo para problemas cardíacos.

## Características

- **Entrada**: Edad (25-80 años), Colesterol (120-600 mg/dl)
- **Predicción**: 0 (No problemas cardíacos), 1 (Posibles problemas cardíacos)
- **Salida**: Imagen dependiendo de la predicción (Imagen feliz si la predicción es 0, alerta si es 1)
- **Tecnologías**:
  - **Streamlit**: Framework para crear aplicaciones web interactivas.
  - **scikit-learn**: Para el modelo de clasificación SVC.
  - **Joblib**: Para cargar el modelo y el escalador guardados.
  - **NumPy** y **Pandas**: Para manejo de datos.

## Instalación

### Requisitos

1. Python 3.x
2. Las dependencias necesarias están listadas en el archivo `requirements.txt`.

### Pasos para instalar

1. **Clona o descarga el proyecto**:

   ```bash
   git clone https://github.com/tu_usuario/tu_repositorio.git

