import tkinter as tk  # Módulo para crear interfaces gráficas con ventanas y controles
from tkinter import messagebox  # Para mostrar diálogos interactivos con el usuario
import time  # Módulo para trabajar con el tiempo (pausas, duraciones)
import threading  # Para ejecutar procesos en segundo plano (temporizadores sin bloquear la interfaz)
import os  # Para ejecutar comandos del sistema (en este caso, para reproducir sonidos)

# Constantes de tiempo en minutos
TIEMPO_TRABAJO = 25  # Duración del ciclo de trabajo en minutos
TIEMPO_DESCANSO = 5  # Duración del ciclo de descanso en minutos

# Función que ejecuta un temporizador en segundo plano
def ejecutar_temporizador(minutos, mensaje, callback):
    duracion = minutos * 60  # Convierte los minutos a segundos
    print(f"Duración: {duracion} segundos")  # Imprime la duración en segundos para depuración
    
    while duracion >= 0:  # Bucle que se ejecuta mientras haya tiempo restante
        mins = int(duracion // 60)  # Calcula los minutos restantes y los convierte a entero
        segs = int(duracion % 60)  # Calcula los segundos restantes y los convierte a entero
        tiempo_str = f"{mins:02d}:{segs:02d}"  # Formatea el tiempo para mostrarlo como MM:SS
        etiqueta_tiempo.config(text=tiempo_str)  # Actualiza el texto de la etiqueta para mostrar el tiempo restante
        time.sleep(1)  # Espera 1 segundo antes de continuar con la siguiente iteración
        duracion -= 1  # Resta un segundo a la duración total
    os.system("afplay alarma.mp3")  # Reproduce un sonido cuando termina el temporizador
    callback()  # Llama a la función que maneja el paso siguiente (ya sea descanso o preguntar si seguir)

# Función que maneja un ciclo completo de trabajo y descanso
def iniciar_ciclo():
    boton_inicio.config(state="disabled")  # Desactiva el botón mientras está en ejecución
    etiqueta_estado.config(text="⏳ Sesión de trabajo")  # Muestra el estado actual (trabajo)
    threading.Thread(target=ejecutar_temporizador, args=(TIEMPO_TRABAJO, "Trabajo", iniciar_descanso)).start()  # Inicia el temporizador de trabajo en un hilo separado

def iniciar_descanso():
    etiqueta_estado.config(text="🛋️ Descanso")  # Actualiza el estado a descanso
    threading.Thread(target=ejecutar_temporizador, args=(TIEMPO_DESCANSO, "Descanso", preguntar_otra_vez)).start()  # Inicia el temporizador de descanso en un hilo separado

# Función que pregunta si el usuario quiere continuar con otro ciclo
def preguntar_otra_vez():
    respuesta = messagebox.askyesno("Pomodoro", "¿Querés hacer otro ciclo?")  # Muestra un cuadro de diálogo con opciones sí/no
    if respuesta:  # Si el usuario elige "sí"
        iniciar_ciclo()  # Inicia otro ciclo de trabajo
    else:  # Si el usuario elige "no"
        etiqueta_estado.config(text="✅ Ciclos finalizados")  # Actualiza el estado a "Ciclos finalizados"
        etiqueta_tiempo.config(text="00:00")  # Resetea el tiempo mostrado
        boton_inicio.config(state="normal")  # Vuelve a habilitar el botón para iniciar un nuevo ciclo

# Crear la interfaz gráfica
ventana = tk.Tk()  # Crea una ventana principal
ventana.title("Pomodoro Minimalista")  # Establece el título de la ventana
ventana.geometry("300x200")  # Establece el tamaño de la ventana

# Etiqueta que muestra el estado actual de la sesión (trabajo, descanso)
etiqueta_estado = tk.Label(ventana, text="Listo para comenzar", font=("Helvetica", 14))
etiqueta_estado.pack(pady=10)  # Muestra la etiqueta en la ventana con un margen de 10 píxeles

# Etiqueta que muestra el tiempo restante en formato MM:SS
etiqueta_tiempo = tk.Label(ventana, text="25:00", font=("Helvetica", 36))
etiqueta_tiempo.pack(pady=20)  # Muestra la etiqueta en la ventana con un margen de 20 píxeles

# Botón que inicia el ciclo Pomodoro
boton_inicio = tk.Button(ventana, text="Iniciar ciclo Pomodoro", command=iniciar_ciclo)
boton_inicio.pack(pady=10)  # Muestra el botón en la ventana con un margen de 10 píxeles

# Inicia la ventana
ventana.mainloop()  # Inicia el bucle principal de la interfaz gráfica, manteniendo la ventana activa