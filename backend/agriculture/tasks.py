import numpy as np
import tensorflow as tf

def train_yield_prediction_model():
    # Dados de exemplo (área plantada em hectares e produtividade em toneladas)
    X = np.array([[1], [2], [3], [4], [5]])  # Área em hectares
    y = np.array([2.5, 5, 7.5, 10, 12.5])   # Produtividade em toneladas

    # Criar um modelo de regressão linear
    model = tf.keras.Sequential([tf.keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer='sgd', loss='mean_squared_error')

    # Treinar o modelo
    model.fit(X, y, epochs=500, verbose=0)

    # Salvar o modelo treinado
    model.save('yield_prediction_model.h5')

def predict_yield(area_in_hectares):
    # Carregar o modelo treinado
    model = tf.keras.models.load_model('yield_prediction_model.h5')

    # Fazer a previsão
    prediction = model.predict(np.array([[area_in_hectares]]))
    return float(prediction[0][0])
