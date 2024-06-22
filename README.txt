Proyecto: Elaboracion de una interfaz visual en python mediante el uso de bibliotecas Tkinter y matplotlib. 
Objetivo: Control remoto de instrumentos RIGOL (osciloscopio y fuente tension continua) a traves de comunicacion PYVISA.
Resultados: Control de instrumentos y aplicacion para dibujar curva IDS para la fuente de tension DP800 y aplicacion consistente en graficar señales en pantalla pc en tiempo real del osciloscopio DS1000
Advertencia: Imprescindible estar conectado a tu instrumento via GPIB, USB, TCP/IP, etc para el buen funcionamiento


___________

Main_App.py -> Main que llama a los ficheros de cada instrumento,
Fichero del instrumento osciloscopio DS1000: interfaz_osciloscopio_v4.py
Fichero del instrumento fuente tension continua DP800: interfaz_Fuentecontinua_v2.py
Ficheros de configuracion de botones (interaccion con raton + colores y atributos): config_boton.py    /      diccionario_boton.py
Comandos extra no usados para tener control absoluto del osciloscopio: Comandos_extra_RIGOL_DS1000.png