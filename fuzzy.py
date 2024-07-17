import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# Definir universos y funciones de membresía
x_magnitud = np.arange(0, 10.1, 0.1)
x_profundidad = np.arange(0, 200.1, 1)

magnitud_bajo = fuzz.trimf(x_magnitud, [0, 0, 6])
magnitud_moderado = fuzz.trimf(x_magnitud, [5, 6, 7])
magnitud_fuerte = fuzz.trimf(x_magnitud, [6, 10, 10])

profundidad_bajo = fuzz.trapmf(x_profundidad, [100, 200, 200, 200])
profundidad_moderado = fuzz.trapmf(x_profundidad, [50, 70, 120, 150])
profundidad_alto = fuzz.trapmf(x_profundidad, [0, 0, 70, 100])

# Visualización de funciones de membresía
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(x_magnitud, magnitud_bajo, 'b', label='Bajo')
plt.plot(x_magnitud, magnitud_moderado, 'g', label='Moderado')
plt.plot(x_magnitud, magnitud_fuerte, 'r', label='Fuerte')
plt.title('Funciones de Membresía - Magnitud')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(x_profundidad, profundidad_bajo, 'b', label='Bajo riesgo')
plt.plot(x_profundidad, profundidad_moderado, 'g', label='Riesgo moderado')
plt.plot(x_profundidad, profundidad_alto, 'r', label='Alto riesgo')
plt.title('Funciones de Membresía - Profundidad')
plt.legend()

plt.tight_layout()
plt.show()
