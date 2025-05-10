# setup.py
# Este script configura py2app para convertir el archivo temporizador.py en una app de macOS

from setuptools import setup  # Importa la función setup de setuptools

# Lista de scripts principales
APP = ['temporizador.py']

# Archivos que deben incluirse con la app (como el sonido)
DATA_FILES = ['alarma.mp3']

# Opciones para py2app
OPTIONS = {
    'argv_emulation': True,  # Necesario para que el sistema maneje bien eventos de teclado/ratón
    # 'iconfile': 'icon.icns',  # Ícono desactivado por ahora
    'packages': ['tkinter'],  # Incluimos tkinter para evitar que quede afuera
}

# Configuración final
setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)