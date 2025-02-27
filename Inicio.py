import tensorflow as tf
import numpy as np

celsius = np.array([-40, -10, 0, 8, 15, 22, 38], dtype=float)
farenheit = np.array([-40, 14, 32, 46, 59, 72, 100], dtype=float)

#capa = tf.keras.layers.Dense(units=1, input_shape=[1])
#modelo=tf.keras.Sequential([capa])
oculta1 = tf.keras.layers.Dense(units=3, input_shape=[1])
oculta2 = tf.keras.layers.Dense(units=3)
salida = tf.keras.layers.Dense(units=1)
modelo = tf.keras.Sequential([oculta1, oculta2, salida])

modelo.compile(
    optimizer=tf.keras.optimizers.Adam(0.1),
    loss='mean_squared_error'
 )

print("Comenzando Entrenamiento...")
historial = modelo.fit(celsius, farenheit, epochs=1000, verbose=False)
print("Modelo Entrenado!")

import matplotlib.pyplot as plt
plt.xlabel("# Epoca")
plt.ylabel("Magnitud de Pérdida")
plt.plot(historial.history["loss"])

print("Hagamos una predicción!")
resultado = modelo.predict(np.array([100.0]))
print("el resultado es: " + str(resultado[0][0]) + " farenheit!")

print("Variables internas del modelo")
#print(capa.get_weights())
print(oculta1.get_weights())
print(oculta2.get_weights())
print(salida.get_weights())