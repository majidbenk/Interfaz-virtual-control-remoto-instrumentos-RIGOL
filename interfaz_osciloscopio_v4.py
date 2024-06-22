from tkinter import *
from tkinter import messagebox
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import pyvisa
from config_boton import configuracion_boton
from diccionario_boton import colores_boton
from diccionario_boton import colores_menu_desplegable
from diccionario_boton import colores_menu_desplegable_opcionX
from diccionario_boton import colores_textbox
from diccionario_boton import colores_checkbox
from diccionario_boton import colores_boton_pequeño
from diccionario_boton import colores_label
from diccionario_boton import colores_label_pequeño
#revisar bibliotecas
color1 = '#020f12'
color2 = '#05d7ff'
color3 = '#65e7ff'
color4 = 'BLACK'
highlightcolor=color2


#-------------------------------------------------
# CREACION VENTANA E INTERFAZ VISUAL :
#------------------------------------------------

class Osciloscopio:
    #def_init__ es un constructor que se llama automáticamente cuando se crea una instancia de la clase.
    def __init__(self) -> None:
        self.Osciloscopio_window = Toplevel() #crea ventana
        self.Osciloscopio_window.title('Osciloscopio')
        self.Osciloscopio_window.geometry('750x500')
        self.Osciloscopio_window.resizable(width=False, height=False)
        Osciloscopio_Frame = Frame(self.Osciloscopio_window , bg=color1, pady=40)
        Osciloscopio_Frame.pack(fill=BOTH, expand=True) #Empaqueta el marco dentro de la ventana principal. fill=BOTH indica que el marco debe expandirse tanto horizontal como verticalmente para llenar todo el espacio disponible
        Osciloscopio_Frame.columnconfigure(0, weight=1)
        Osciloscopio_Frame.rowconfigure(0, weight=1)
        Osciloscopio_Frame.rowconfigure(1, weight=1)

        resources = self.Resources() #resources es una lista de ID. Estamos llamando a la funcion de abajo 'def Resources(self):' que retorna la lista de resources
        self.vartestborrar = 1#testborrar1
    # Buttons
        # Menu desplegable
        self.var_menudesplegable =StringVar() #var_option_menu se le asigna tipo: Es una variable de control de tipo string. Es la variable que controlara el menu que crearemos abajo
        self.var_menudesplegable.set(resources[0])#valor inicial del menu desplegable
        menudesplegable = OptionMenu(Osciloscopio_Frame, self.var_menudesplegable, *resources) #Se crea menu desplegable. *resources es la lista de IDs.,)
        menudesplegable.pack(side=TOP, padx=80, pady=80)                                                                            #El * desempaqueta los elementos de la lista resources pa q pasen como argumentos individuales0
        menudesplegable.configure(**colores_menu_desplegable)                                                                          #Se crea dentro de la ventana Gen_Señal_frame
        menudesplegable["menu"].configure(**colores_menu_desplegable_opcionX)                                                                          #self.var_option_menu variable control tipo cadena caracteres asociada al menu
                                                                                                                               #y que rastreara la opcion seleccionada
                                                                                                                               #OptionMenmu es una palabra resrrvada como button, text, etc

        #Boton conexion que nos servira para validar la informacion introducida
        Conexion =Button(Osciloscopio_Frame, text='Conexion', command=self.Connection,**colores_boton) #Asociado a la ventana osciloscopio, etiqueta conexion y produce evento connection
        Conexion.pack(side=TOP, padx=50, pady=50)
        configuracion_boton(Conexion)
    

    def Connection(self):
        
        self.Recurso_elegido = self.var_menudesplegable.get() #con get capturamos la ID del usuario
    
    # Abrir conexion
        
        # Abrimos conexion con el instrumento seleccionado
        self.instrument = self.rm.open_resource(self.Recurso_elegido)

        # Enviamos comando SCPI para saber qué instrumento es
        response = self.instrument.query('*IDN?')

        # Imprimos por pantalla la respuesta
        print(f'Instrument identification:\n{response}')
        
    # Cerrar ventana principal
        self.Osciloscopio_window.destroy()
    
    # LLamamos a funcion que genera ventana principal con opciones
        self.Ventana_opciones_Osciloscopio()



    def Resources(self):
        
        self.rm = pyvisa.ResourceManager()
        resources = self.rm.list_resources()
        
        return resources
        """"
        # PRUEBA #Dejar esta prueba y en el tfg decir que es para probar si no hay nada conectado
        resources = ['Op1', 'Op2', 'Op3']
        return resources
        """
        
        
#ventana con las opciones del osciloscopio    
    def Ventana_opciones_Osciloscopio(self):
    # Meter mensaje en textbox  sobre informacion de la direccion del Generador de señal:

    # Creacion de Frame que pide escala, offset y canal   
        Osciloscopio_window = Toplevel()
        Osciloscopio_window.title('Osciloscopio: DS1074B')
        Osciloscopio_window.geometry('900x900')
        Osciloscopio_window.resizable(width=False, height=False)
        Osciloscopio_window.configure(bg=color1)
        
        self.Panel_config_Oscil= Frame(Osciloscopio_window, bg=color1, pady=40)
        self.Panel_config_Oscil.grid(row=0, column=0, sticky="nsew") #self.Panel_config_Oscil.pack(fill=BOTH, expand=True) Mas abajo se usa grid, para no mezclar con pack, nsew empaqueta en toda la ventana
        self.Panel_config_Oscil.columnconfigure(0, weight=1)  # Expandir la columna 0
        self.Panel_config_Oscil.rowconfigure(0, weight=1)     # Expandir la fila 0

        
    # Text boxes and Chekcbuttons para Parameters creation 
        #Creamos las distintas medidas y canales que se pueden manejar del osciloscopio:
        i = 0
        colocacion_filas = 1

        #Se declaran los boxtext y sus variables de offset, escala V/div y escala en tiempo del osciloscopio
        self.variable_checkbutton=[]
        self.boxtext_offset = [] 
        self.boxtext_variable_offset = []
        self.boxtext_escala_T = []
        self.boxtext_escala_V = []
        self.boxtext_variable_escala_T = []
        self.boxtext_variable_escala_V = []

        
        # Etiqueta Titulo general
        Titulo_Medidas = Label(self.Panel_config_Oscil, text=" SELECCIONE CANALES \n INTRODUZCA  ESCALA Y OFFSET ", **colores_label)
        Titulo_Medidas.grid(row=colocacion_filas, column=0, pady=5)
        colocacion_filas += 1

        #Etiqueta para indicar el textbox de escala voltios/division
        Titulo_Escala_V = Label(self.Panel_config_Oscil, text="V/div", **colores_label_pequeño)
        Titulo_Escala_V.grid(row=colocacion_filas, column=1)

        #Etiqueta para indicar el textbox de escala tiempo
        Titulo_Escala_T = Label(self.Panel_config_Oscil, text="us/div", **colores_label_pequeño)
        Titulo_Escala_T.grid(row=colocacion_filas, column=2)


        #Etiqueta para indicar el textbox de escala offset
        Titulo_Offset = Label(self.Panel_config_Oscil, text="OFFSET", **colores_label_pequeño)
        Titulo_Offset.grid(row=colocacion_filas, column=3)
        
        colocacion_filas += 1 #Bajamos una fila para imprimir lo siguiente:

 #Creamos los checkbuttons de cada canal y textbox para crear offset y escala     
        Canales = [' CANAL 1 ',' CANAL 2 ',' CANAL 3 ',' CANAL 4 ']
        popupaviso = (self.Osciloscopio_window.register(self.caracter_valido), '%P') #%P esun comando de tkinter. Es el valor del Entry si pasa la validacion.
                                                                                      #La validacion llama a la funcion caracter_valido que chequea condiciones

        #Escala Tiempo en us, no se mete en matriz porque hay una escala comun a todos los canales
        self.boxtext_escala_T.append('')
        self.boxtext_variable_escala_T.append('')
        self.boxtext_variable_escala_T = StringVar() 
        self.boxtext_variable_escala_T.set('0.0005') #La cajetilla se inicializa en 500 us 

        self.boxtext_escala_T = Entry(self.Panel_config_Oscil, 
                                          state= NORMAL, 
                                          textvariable=self.boxtext_variable_escala_T,**colores_textbox, validate='key', validatecommand=popupaviso)
        self.boxtext_escala_T.grid(row=3,column=2) 
        configuracion_boton(self.boxtext_escala_T)  
        for Canal in Canales:
            
            #Declaramos las listas que contendran las variables y textbox modificables de escala V/div, offset 
            #Escala V/div
            self.boxtext_escala_V.append('')
            self.boxtext_variable_escala_V.append('')
            self.boxtext_variable_escala_V[i] = StringVar() 
            self.boxtext_variable_escala_V[i].set('1') #La cajetilla se inicializa en 1V/div

            #Escala offset
            self.boxtext_offset.append('')
            self.boxtext_variable_offset.append('')
            self.boxtext_variable_offset[i] = StringVar() 
            self.boxtext_variable_offset[i].set('0') #Offset inicial 0V

            self.boxtext_escala_V[i] = Entry(self.Panel_config_Oscil, 
                                          state= DISABLED, 
                                          textvariable=self.boxtext_variable_escala_V[i],**colores_textbox, validate='key', validatecommand=popupaviso)
            self.boxtext_escala_V[i].grid(row=colocacion_filas,column=1) #Son los cajetines de texto donde el usuario va a meter las unidades 
            configuracion_boton(self.boxtext_escala_V[i])                                                         #siendo variables_param la variable asociada que servira para leer  el contenido del cajetin 

            self.boxtext_offset[i] = Entry(self.Panel_config_Oscil, 
                                          state= DISABLED, 
                                          textvariable=self.boxtext_variable_offset[i],**colores_textbox, validate='key', validatecommand=popupaviso)
            self.boxtext_offset[i].grid(row=colocacion_filas,column=3, padx=10) #Son los cajetines de texto donde el usuario va a meter las unidades 
            configuracion_boton(self.boxtext_offset[i])                                                          #siendo variables_param la variable asociada que servira para leer  el contenido del cajetin 
            

            self.variable_checkbutton.append('') #se inicializa vacio
            self.variable_checkbutton[i] = IntVar() #Esta variable se pondra a 1 si está seleccionada la cajetilla o 0 si no está seleccionada
            Check_Channel = Checkbutton(self.Panel_config_Oscil, text=f'{Canal}',**colores_checkbox,
                                variable=self.variable_checkbutton[i], command=self.check_function_Oscil)  
            configuracion_boton(Check_Channel)                                                        
            Check_Channel.grid(row = colocacion_filas, column=0, pady=5, padx=50)
            
            
            colocacion_filas += 1
            i += 1

# Botón "Validar para volcar al osciloscopio requisitos"
        Validar = Button(self.Panel_config_Oscil, text='Enviar', command=self.EnviarInfo_Oscil,**colores_boton_pequeño)
        Validar.grid(row = colocacion_filas, column=0, pady=20)
        configuracion_boton(Validar)
        colocacion_filas += 1


#Creamos el checkbutton y sus cajetines para las medidas que se desean recibir del osciloscopio:
        # Etiqueta Titulo medidas
        Titulo_Medidas = Label(self.Panel_config_Oscil, text="MEDIDAS EN OSCILOSCOPIO", **colores_label)
        Titulo_Medidas.grid(row=colocacion_filas, column=0, pady=25)
        colocacion_filas += 1


        Nmedidas = [' Vmax        ',' Vmin         ',' Veficaz     ',' Vpico      ','Frecuencia', 'Overshoot   ', ' Periodo     ',' Duty cycle  ']
        self.variable_checkbutton_medida = []
        self.valor_unidades = ['V','V','V','V','hz','V','s','%']
        j=0
        colocacion_filas_medida = colocacion_filas #nos quedamos con el numero de fila donde se empieza a imprimir Vmax para poder usarla en otros bucles
        self.colocacion_filas_MedRecibidas = colocacion_filas #se usaran en la funcion del boton enviar, se copian filas para recibirlas ahi y poder imprimir lecturas en textboxs
        for medida in Nmedidas:
            self.variable_checkbutton_medida.append('') #se inicializa vacio
            self.variable_checkbutton_medida[j] = IntVar()


            Check_Medida = Checkbutton(self.Panel_config_Oscil, text=f'{Nmedidas[j]}   ( {self.valor_unidades[j]} ) :',**colores_checkbox, 
            variable=self.variable_checkbutton_medida[j])  
            configuracion_boton(Check_Medida)                                                        
            Check_Medida.grid(row = colocacion_filas_medida, column=0)

            colocacion_filas_medida += 1
            j += 1
        
        
        #Se crean los textbox donde estaran los valores que se reciben del oscilosocpio segun los canales creados
        self.boxtext_medidas_recibidas  =  []
        self.boxtext_variable_medidas_recibidas = []

        #Inicializamos las listas para que no den error. Se inicializan filas.
        for medida in Nmedidas:
            self.boxtext_medidas_recibidas.append([])
            self.boxtext_variable_medidas_recibidas.append([])

        columnas_textbox_medidas = 1


        for m in range(len(Canales)):
            colocacion_filas_medidas_recibidas =  colocacion_filas
            for k in range(len(Nmedidas)):
                self.boxtext_variable_medidas_recibidas[m].append(StringVar()) #Variables tipo String (que es el formato variable del osciloscopio), a continuacion se llenaran con un '0''
                self.boxtext_variable_medidas_recibidas[m][-1].set('0')  # con [-1] accedemos al ultimo elemento de la lista, en este caso una lista que representa las filas de las columnas m.
                entry = Entry(self.Panel_config_Oscil, state=DISABLED,
                            textvariable=self.boxtext_variable_medidas_recibidas[m][-1], **colores_textbox)
                entry.grid(row=colocacion_filas_medidas_recibidas, column=columnas_textbox_medidas, padx = 10) #padx=10 para que no solapen con boton autosetup ni entre ellas
                configuracion_boton(entry)
                self.boxtext_medidas_recibidas[m].append(entry)
                colocacion_filas_medidas_recibidas += 1
            columnas_textbox_medidas += 1


        colocacion_filas += 2 #Para imprimir boton en medio de la columna de las medidas
        #AutoSetup Osciloscopio
        AutoSetup = Button(self.Panel_config_Oscil, text='AutoSetup', command=self.AutosetupBoton,**colores_boton_pequeño)
        AutoSetup.grid(row = colocacion_filas, column=columnas_textbox_medidas + 1) #Imprimimos el boton AutoSetup en ultima columna
        configuracion_boton(AutoSetup)

        colocacion_filas += 2 #Para imprimir boton en medio de la columna de las medidas
        #Graficar onda Osciloscopio en PC
        Graficar = Button(self.Panel_config_Oscil, text='Graficar', command=self.GraficarBoton,**colores_boton_pequeño)
        Graficar.grid(row = colocacion_filas, column=columnas_textbox_medidas + 1) #Imprimimos el boton AutoSetup en ultima columna
        configuracion_boton(Graficar)
    #Se comprueba que en las cajetillas de texto solo se meta puntos y numeros
    def caracter_valido(self, nuevo_valor):
        if nuevo_valor == "" or self.es_valido(nuevo_valor): #pasamos a la funcion es valido el valor introducido
            return True
        else:
            messagebox.showerror("Caracter no valido", "Caracteres admitidos:  0123456789.")
            return False

    def es_valido(self, valor):
        #Comprobamos si el nuevo numero solo tiene numeros y punto
        for char in valor:
            if char not in "0123456789.":
                return False
        return True #devolvemos falso o true a la funcion caracter_valido para que imprima popup de aviso si corresponde o ignorar
#-------------------------------------------------
# LEER DATOS BINARIOS DEL WAVEFORM :
#------------------------------------------------


    
#Boton AutoSetup ejecuta SCPI AutoSetup en Osciloscopio
    def AutosetupBoton(self):
        self.instrument.write(':AUTO')

#Evento que se produce al pulsa boton graficar
    def GraficarBoton(self):
            
            data = metadata = num_points = x_increment = x_origin = y_increment = y_origin = ''
            fig = plt.figure()
            ax1 = fig.add_subplot(1,1,1)
            ax1.set_xlabel('Time (s)')
            ax1.set_ylabel('Voltage (V)')
            self.Canales = ['CHAN1', 'CHAN2', 'CHAN3', 'CHAN4']

            def animate (i):
                
                ax1.clear()
                for m,canal in enumerate(self.Canales):
                    if(self.variable_checkbutton[m].get() == 1):
                        data = metadata = num_points = x_increment = x_origin = y_increment = y_origin = ''
                        self.instrument.write(':WAVEFORM:SOUR ' + canal)
                        data = self.instrument.query_binary_values('WAVEFORM:DATA?', datatype='B', is_big_endian=True)
                        metadata = self.instrument.query('WAVEFORM:PRE?').split(',')
                        
                        num_points = int(metadata[2])
                        x_increment = float(metadata[4])
                        x_origin = float(metadata[5])
                        y_increment = float(metadata[7])
                        y_origin = float(metadata[8])

                        x_values = np.arange(0, num_points) * x_increment + x_origin
                        y_values = (np.array(data) - y_origin) * y_increment
                        
                        ax1.plot(x_values, y_values, label=canal)
                        
                        ax1.legend()

            ani = animation.FuncAnimation(fig, animate, interval=1000)

            plt.show()

    #Envio de canal seleccionado, escala y offset
    def EnviarInfo_Oscil(self):
        i=0
        Ncanales = ['1','2','3','4']
        Nmedidas = ['VMAX','VMIN','VRMS','VPP','FREQ', 'OVER', 'PER','PDUT']
        Canales = [' CHAN1', ' CHAN2', ' CHAN3', ' CHAN4']

        self.instrument.write(':TIM:SCAL ' + str(self.boxtext_variable_escala_T.get()))#Escala us/div capturada se envia en forma de string
        for canal in Ncanales:
            if(self.variable_checkbutton[i].get() == 1):
                
                self.instrument.write(':CHAN' + Ncanales[i] + ':DISP ' + 'ON') #Abrir canal seleccionado por usuario
                self.instrument.write(':CHAN' + Ncanales[i] +':SCAL ' + str(self.boxtext_variable_escala_V[i].get()))#Escala Voltios/div capturada se envia en forma de string
                self.instrument.write(':CHAN' + Ncanales[i] +':OFFS ' + str(self.boxtext_variable_offset[i].get())) #Offset se envia
            else:
                
                self.instrument.write(':CHAN' + Ncanales[i] + ':DISP ' + 'OFF') #Cerrar canal
            i+=1

	#Recibir medidas despues de pulsar Enviar:
        #Otra manera de recorrer columnas x Filas a eleccion del programador. enumerate obtiene dimension total y va sumando +1 sin ponerlo nosotros
        m=0
        for m, canal in enumerate(Ncanales):
            k=0
            if self.variable_checkbutton[m].get() == 1:
                for k, medida in enumerate(Nmedidas):
                    if self.variable_checkbutton_medida[k].get() == 1:
                        lectura =  self.instrument.query(':MEASure:' + Nmedidas[k] + '?' + Canales[m])
                        self.boxtext_variable_medidas_recibidas[m][k].set(lectura)  # con [-1] accedemos al ultimo elemento de la lista, en este caso una lista que representa las filas de las columnas m.
                    else:
                        self.boxtext_variable_medidas_recibidas[m][k].set('0') #si volvemos a solicitar info de medida del mismo canal pero hemos deshabiltiado alguna medida, hay que ponerla a 0
            else:
                for k, medida in enumerate(Nmedidas): #si quitamos checkbox del canal le decimos que esa columna la devuelva a 0
                    self.boxtext_variable_medidas_recibidas[m][k].set('0') 

        

    def check_function_Oscil(self):
    
        cont = 0
        
        for textbox in self.boxtext_escala_V:
            if self.variable_checkbutton[cont].get() == 1:
                self.boxtext_escala_V[cont].config(state=NORMAL) #El cuadro pasa a ser editable
                self.boxtext_escala_V[cont].focus() #establece el foco en un cuadro sin que el usuario tenga que hacer clic en el
                self.boxtext_offset[cont].config(state=NORMAL)
                self.boxtext_offset[cont].focus()
            else:
                self.boxtext_escala_V[cont].config(state=DISABLED)
                self.boxtext_variable_escala_V[cont].set('1') #Pomemos un 1 si esta deshabilitado
                self.boxtext_offset[cont].config(state=DISABLED)
                self.boxtext_variable_offset[cont].set('0')
            
            cont += 1

        
    #----------------------------------------------------------------------
    #-----------------------FIN OSCILOSCOPIO-------------------------------
    #----------------------------------------------------------------------
