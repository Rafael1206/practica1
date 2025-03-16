import numpy as np
import matplotlib.pyplot as plt

# Definir parámetros
fs = 200            # Frecuencia de muestreo del inciso (b)
#fs = 75             # Frecuencia de muestreo del inciso (c)
N = 20              # Número de muestras
T_s = 1 / fs        # Período de muestreo

# Definir el rango de tiempo continuo
t = np.linspace(0, (N-1)*T_s, 1000)             # Tiempo continuo
x_continuo = 3 * np.cos(100 * np.pi * t)        # Señal continua

# Definir muestras discretas
t_discreto = np.arange(0, N) * T_s              # Instantes de muestreo
x_discreto = 3 * np.cos(100 * np.pi * t_discreto)  # Señal muestreada

# Graficar señal continua
plt.figure(figsize=(10, 5))
plt.plot(t, x_continuo, label='Señal Continua', color='b')
plt.stem(t_discreto, x_discreto, linefmt='r-', markerfmt='ro', basefmt='r', label='Muestras')
plt.xlabel('Tiempo (s)')
plt.ylabel('Amplitud')
plt.title('Señal Continua y Muestreada (fs = 200 Hz)')
#plt.title('Señal Continua y Muestreada (fs = 75 Hz)')
plt.grid()
plt.legend()
plt.show()
