DOCUMENTACIÓN DEL PROYECTO - TEMPORIZADOR POMODORO
==================================================

Este archivo documenta el funcionamiento completo del script `temporizador.py`, línea por línea.

--------------------------------------------------
IMPORTACIONES
--------------------------------------------------
import tkinter as tk
from tkinter import messagebox
import time
import threading
import os

- tkinter: crea interfaces gráficas (ventanas, botones, etiquetas, etc.)
- messagebox: submódulo de tkinter para mostrar ventanas emergentes.
- time: usado para pausas con `sleep`.
- threading: permite ejecutar el temporizador sin congelar la interfaz.
- os: usado para reproducir el sonido al finalizar cada ciclo.

--------------------------------------------------
CONSTANTES DE TIEMPO
--------------------------------------------------
TIEMPO_TRABAJO = 25
TIEMPO_DESCANSO = 5

- Definen la duración en minutos de los ciclos de trabajo y descanso.

--------------------------------------------------
FUNCIÓN: ejecutar_temporizador
--------------------------------------------------
def ejecutar_temporizador(minutos, mensaje, callback):

- Ejecuta una cuenta regresiva en segundos.
- Al finalizar, reproduce un sonido y ejecuta una función de continuación (callback).

Dentro del bucle:
- Formatea el tiempo como MM:SS
- Actualiza la etiqueta en pantalla
- Espera 1 segundo por iteración

Al finalizar:
- Reproduce un sonido con `afplay` (solo en macOS)
- Llama a la función `callback()` para continuar con el ciclo.

--------------------------------------------------
FUNCIÓN: iniciar_ciclo
--------------------------------------------------
def iniciar_ciclo():

- Desactiva el botón
- Cambia el texto de estado a "Sesión de trabajo"
- Lanza un hilo para el temporizador de trabajo
- Al terminar, llama a `iniciar_descanso`

--------------------------------------------------
FUNCIÓN: iniciar_descanso
--------------------------------------------------
def iniciar_descanso():

- Cambia el estado a "Descanso"
- Lanza un hilo para el temporizador de descanso
- Al terminar, llama a `preguntar_otra_vez`

--------------------------------------------------
FUNCIÓN: preguntar_otra_vez
--------------------------------------------------
def preguntar_otra_vez():

- Muestra un cuadro de diálogo `¿Querés hacer otro ciclo?`
- Si elige "Sí", comienza otro ciclo.
- Si elige "No", muestra mensaje final y resetea la interfaz.

--------------------------------------------------
INTERFAZ GRÁFICA
--------------------------------------------------
ventana = tk.Tk()
ventana.title("Pomodoro Minimalista")
ventana.geometry("300x200")

- Crea la ventana principal

etiqueta_estado = tk.Label(...)
etiqueta_tiempo = tk.Label(...)
boton_inicio = tk.Button(...)

- Etiquetas y botón que forman la interfaz
- El botón inicia el ciclo

--------------------------------------------------
BUCLE PRINCIPAL
--------------------------------------------------
ventana.mainloop()

- Mantiene la ventana activa y funcionando