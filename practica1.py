import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square, sawtooth
#crear funciones de salida------------------------------------------------------
def impulso_unitario(n):
    return np.where(n == 0, 1, 0)

def escalon_unitario(n):
    return np.where(n >= 0, 1, 0)

def funcion_seno(n, F):
    return np.sin(2 * np.pi * F * n)

def funcion_coseno(n, F):
    return np.cos(2 * np.pi * F * n)

def funcion_exponencial(n, W):
    return np.exp(W * n)

def funcion_exponencial_compleja(n, W):
    return np.exp(1j * 2 * np.pi * W * n)

def coseno_amortiguado(n, F, a):
    return np.cos(2 * np.pi * F * n) * a**n

def senal_cuadrada(n, F):
    return square(2 * np.pi * F * n)

def senal_triangular(n, F):
    return sawtooth(2 * np.pi * F * n, 0.5)
# fin de funciones ---------------------------------------------------------
#modificacion de señal-----------------------------------
def modificar_senal(senal, n, desplazamiento=0, escala=1):
    return escala * senal(n - desplazamiento)
#---------------------------------------------------------------------------------------------
#senal:     funcion que genera la señal (impulso_unitario)
#n:     vector de tiempo (o muestra)
#desplazamiento:       coree la señal a la derecha(+) o izquierda(-) 
#escala:       multiplica la señal (cambia amplitud)
#---------------------------------------------------------------------------------------------
#----------------------EJEMPLO-----------------------
#   n = np.arange(-10, 20, 1)
#   escalon_modificado = modificar_senal(escalon_unitario, n, desplazamiento=5, escala=2)
#   graficar_senal(n, escalon_modificado, "Escalón Unitario Desplazado y Escalado")
#----------------------------------------------------
def graficar_senal(n, senal, titulo):
    plt.figure()
    plt.stem(n, senal)
    plt.xlabel("Muestras")
    plt.ylabel("Voltaje")
    plt.title(titulo)
    plt.grid()
    plt.show()

# Definición de intervalos
n1 = np.arange(-10, 10, 1)
n2 = np.arange(0, 20, 1)
n3 = np.arange(0, 25, 1)
n4 = np.arange(0, 75, 1)
n5 = np.arange(0, 20, 1)

# Graficar funciones
graficar_senal(n1, impulso_unitario(n1), "Impulso Unitario")
graficar_senal(n1, escalon_unitario(n1), "Escalón Unitario")
graficar_senal(n1, funcion_seno(n1, 1/10), "Función Seno")
graficar_senal(n1, funcion_coseno(n1, 1/10), "Función Coseno")
graficar_senal(n2, funcion_exponencial(n2, -1/4), "Función Exponencial")
graficar_senal(n3, funcion_exponencial_compleja(n3, 1/3).real, "Función Exponencial Compleja (Real)")
graficar_senal(n4, coseno_amortiguado(n4, 1/20, 0.9), "Coseno Amortiguado")
graficar_senal(n5, senal_cuadrada(n5, 1/10), "Señal Cuadrada")
graficar_senal(n5, senal_triangular(n5, 1/10), "Señal Triangular")
