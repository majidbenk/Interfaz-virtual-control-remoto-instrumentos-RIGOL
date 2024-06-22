from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt

color1 = '#020f12'
color2 = '#05d7ff'
color3 = '#65e7ff'
color4 = 'BLACK'
highlightcolor=color2
def configuracion_boton (boton):

    def boton_entrada(event):
            boton.config(
                highlightbackground=color3,
                highlightcolor=color3,
                background=color3,
                foreground=color4,
            )

    def boton_salida(event):
            boton.config(
                highlightbackground=color2,
                highlightcolor=highlightcolor,
                background=color1,
                foreground=color2,
            )
            
    boton.bind('<Enter>', boton_entrada)
    boton.bind('<Leave>', boton_salida)
