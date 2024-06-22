from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from interfaz_osciloscopio_v4 import Osciloscopio
from config_boton import configuracion_boton
from diccionario_boton import colores_boton
from intefaz_FuenteContinua_v2 import FuenteContinua



color1 = '#020f12'
color2 = '#05d7ff'
color3 = '#65e7ff'
color4 = 'BLACK'
highlightcolor=color2

#revisar bibliotecas, no todas seran usadas

class Main_window:

#Para evitar fallos es necesario copiar las clases Osciloscopio y FuenteContinua que se importan de sus respectivos ficheros
    def osciloscopio_window(self):
        osciloscopio_clase = Osciloscopio()

    def fuente_tensioncontinua_window (self):
        fuentecontinua_clase = FuenteContinua ()
    
#Creamos la ventana y Main General de nuestra App
    def __init__(self,Main) -> None:
        
        Main.title('INSTRUMENTACION EN REMOTO')
        Main.geometry('600x600')
        Main.resizable(width=False, height=False)
        Frame1 = Frame(Main, bg=color1, pady=40)
        Frame1.pack(fill=BOTH, expand=True) #Empaqueta el marco dentro de la ventana principal. fill=BOTH indica que el marco debe expandirse tanto horizontal como verticalmente para llenar todo el espacio disponible
        Frame1.columnconfigure(0, weight=1)
        Frame1.rowconfigure(0, weight=1)
        Frame1.rowconfigure(1, weight=1)

        
    # Buttons
        gen_senal_button = Button(Frame1,text='Fuente VCC',
                                    command=self.fuente_tensioncontinua_window, #Llamamos a la funcion local de este fichero fuente_tension_continua_window para que copie la clase FuenteContinua
                                    **colores_boton) #Los dos asteriscos son para desempaquetar el diccionario en argumentos de palabras clave
                                                    #El diccionario se extrae del fichero diccionario boton
        gen_senal_button.pack(side=TOP, padx=50, pady=50) 

        osciloscopio_button = Button(Frame1, text='Osciloscopio', 
                                     command=self.osciloscopio_window,  #Cuando se pulsa se entra al fichero osciloscopio. 
                                     **colores_boton)
        osciloscopio_button.pack(side=TOP, padx=50, pady=50)
        configuracion_boton(gen_senal_button)
        configuracion_boton(osciloscopio_button)
        


window = Tk()
main_window = Main_window(window)
window.mainloop()