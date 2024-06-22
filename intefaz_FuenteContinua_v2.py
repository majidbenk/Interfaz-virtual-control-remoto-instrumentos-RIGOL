from tkinter import *
from tkinter import messagebox
import pyvisa
import time
from config_boton import configuracion_boton
from diccionario_boton import colores_boton
from diccionario_boton import colores_menu_desplegable
from diccionario_boton import colores_menu_desplegable_opcionX
from diccionario_boton import colores_checkbox
from diccionario_boton import colores_label_mediano
from diccionario_boton import color_texto
from diccionario_boton import colores_textbox_mediano
from diccionario_boton import colores_label_canales
from interfaz_osciloscopio_v4 import Osciloscopio
import matplotlib.pyplot as plt
#revisar bibliotecas
color1 = '#020f12'
color2 = '#05d7ff'
color3 = '#65e7ff'
color4 = 'BLACK'
highlightcolor=color2



#-------------------------------------------------
# CREACION VENTANA E INTERFAZ VISUAL :
#------------------------------------------------


    

class FuenteContinua:
    #def_init__ es un constructor que se llama automáticamente cuando se crea una instancia de la clase.
    def __init__(self) -> None:
        self.FuenteConitnua_window = Toplevel() #crea ventana
        self.FuenteConitnua_window.title('BUSCAR FUENTE CONTINUA RIGOL DP832A')
        self.FuenteConitnua_window.geometry('750x500')
        self.FuenteConitnua_window.resizable(width=False, height=False)
        FuenteContinua_Frame = Frame(self.FuenteConitnua_window , bg=color1, pady=40)
        FuenteContinua_Frame.pack(fill=BOTH, expand=True) #Empaqueta el marco dentro de la ventana principal. fill=BOTH indica que el marco debe expandirse tanto horizontal como verticalmente para llenar todo el espacio disponible
        FuenteContinua_Frame.columnconfigure(0, weight=1)
        FuenteContinua_Frame.rowconfigure(0, weight=1)
        FuenteContinua_Frame.rowconfigure(1, weight=1)

        resources = self.Resources() #resources es una lista de ID. Estamos llamando a la funcion de abajo 'def Resources(self):' que retorna la lista de resources
        
    # Buttons
        # Menu desplegable
        self.var_menudesplegable =StringVar() #var_option_menu se le asigna tipo: Es una variable de control de tipo string. Es la variable que controlara el menu que crearemos abajo
        self.var_menudesplegable.set(resources[0])#valor inicial del menu desplegable
        menudesplegable = OptionMenu(FuenteContinua_Frame, self.var_menudesplegable, *resources) #Se crea menu desplegable. *resources es la lista de IDs.,)
        menudesplegable.pack(side=TOP, padx=80, pady=80)                                                                            #El * desempaqueta los elementos de la lista resources pa q pasen como argumentos individuales0
        menudesplegable.configure(**colores_menu_desplegable)                                                                          #Se crea dentro de la ventana Gen_Señal_frame
        menudesplegable["menu"].configure(**colores_menu_desplegable_opcionX)                                                                          #self.var_option_menu variable control tipo cadena caracteres asociada al menu
                                                                                                                               #y que rastreara la opcion seleccionada
                                                                                                                               #OptionMenmu es una palabra resrrvada como button, text, etc

        #Boton conexion que nos servira para validar la informacion introducida
        Conexion =Button(FuenteContinua_Frame, text='Conexion', command=self.Connection,**colores_boton) #Asociado a la ventana osciloscopio, etiqueta conexion y produce evento connection
        Conexion.pack(side=TOP, padx=50, pady=50)
        configuracion_boton(Conexion)
    

    def Connection(self):
        
        self.Recurso_elegido = self.var_menudesplegable.get() #con get capturamos la ID del usuario
    
    # Abrir conexion
        
        # Abrimos conexion con el instrumento seleccionado
        self.instrument = self.rm.open_resource(self.Recurso_elegido)

        # Enviamos comando SCPI para saber qué instrumento es
        response = self.instrument.query('*IDN?')

        # Imprimos por pantalla la respuesta (INFORMACION ORIENTADA A PROGRAMADOR)
        print(f'Instrument identification:\n{response}')
        
    # Cerrar ventana principal
        self.FuenteConitnua_window.destroy()
    
    # LLamamos a funcion que genera ventana principal con opciones
        self.Ventana_opciones_FuenteContinua()

    #testborrar2     
    def osciloscopio (self): 
        self.osciloscopio_var = Osciloscopio()
        self.vartest = self.osciloscopio_var.vartestborrar

    def Resources(self):
        
        self.rm = pyvisa.ResourceManager()
        resources = self.rm.list_resources()
        
        return resources
        """
        # PRUEBA #Dejar esta prueba y en el tfg decir que es para probar si no hay nada conectado
        resources = ['Op1', 'Op2', 'Op3']
        return resources

        """
    def Ventana_Aplicacion_transistor (self):
        App_Transistor_window = Toplevel()
        App_Transistor_window.title('PARAMETROS TRANSISTOR')
        App_Transistor_window.geometry('600x400')
        App_Transistor_window.resizable(width=False, height=False)
        App_Transistor_window.configure(bg=color1)
        
        self.Panel_config_Transistor= Frame(App_Transistor_window, bg=color1, pady=40)
        self.Panel_config_Transistor.grid(row=0, column=0, sticky="nsew") #self.Panel_config_FuentCont.pack(fill=BOTH, expand=True) Mas abajo se usa grid, para no mezclar con pack, nsew empaqueta en toda la ventana
        self.Panel_config_Transistor.columnconfigure(0, weight=1)  # Expandir la columna 0
        self.Panel_config_Transistor.rowconfigure(0, weight=1)     # Expandir la fila 0

        colocacion_filas = 0 #Variable para controlar filas de etiquetas, cajetines..

        #CAPTURAR MAXIMO VGS
        Titulo_VGS = Label(self.Panel_config_Transistor, text=f'Introduzca VGS MAX: ', **color_texto)
        Titulo_VGS.grid(row=colocacion_filas, column=1, pady=5) 

        self.boxtext_variable_VGS = StringVar() 
        self.boxtext_variable_VGS.set('0') #La cajetilla se inicializa en 0
        self.boxtext_VGS = Entry(self.Panel_config_Transistor, 
                                              state = NORMAL, 
                                              textvariable=self.boxtext_variable_VGS,**colores_textbox_mediano) #AÑADIR VALIDATE
        self.boxtext_VGS.grid(row=colocacion_filas,column=2, padx=5)
        configuracion_boton(self.boxtext_VGS)
        colocacion_filas += 1

        #CAPTURAR MAXIMO VDS
        Titulo_VDS = Label(self.Panel_config_Transistor, text=f'Introduzca VDS MAX: ', **color_texto)
        Titulo_VDS.grid(row=colocacion_filas, column=1, pady=5) 

        self.boxtext_variable_VDS =  StringVar() 
        self.boxtext_variable_VDS.set('0') #La cajetilla se inicializa en 0
        self.boxtext_VDS = Entry(self.Panel_config_Transistor, 
                                              state = NORMAL, 
                                              textvariable=self.boxtext_variable_VDS,**colores_textbox_mediano) #AÑADIR VALIDATE
        self.boxtext_VDS.grid(row=colocacion_filas,column=2, padx=5)
        configuracion_boton(self.boxtext_VDS)

        colocacion_filas += 1 

        #Boton que al ser pulsado llama a la funcion Transistor_graficar
        Graficar_Transistor = Button(self.Panel_config_Transistor,text='GRAFICAR Id-Vds',
                                    command=self.graficar_transistor, **colores_boton) 
        Graficar_Transistor.grid(row=colocacion_filas, column=1, padx=10, pady=10)
        configuracion_boton(Graficar_Transistor)

        #test borrar y funciona
        #self.osciloscopio()
        #print('test',self.vartest) #testborrar3
    """   
    def graficar_transistor(self):
        Puntos_VDS_inicial = float(self.boxtext_variable_VDS.get())/15 #Dividimos VDSmax entre 15 los puntos de VDS para aumentar precision
        Puntos_VGS_inicial = float(self.boxtext_variable_VGS.get())/5 #Dividimos VGSmax entre 5 para trazar distintas curvas
        Puntos_VDS_inicial_aux = Puntos_VDS_inicial
        Puntos_VGS_inicial_aux = Puntos_VGS_inicial +  Puntos_VGS_inicial #Empezamos en un punto alto,dos veces el minimo puesto que para VGS bajas IDS es cercana a 0
        Puntos_IDS = []
        Puntos_VDS = []
        Puntos_VGS = 3.5 #test con 3.5Volt en VGS esto hay que meterlo en un bucle Puntos_vgs[j] y la intensidad que se lee Puntos_IDS[i][j] de manera que haya una ID para cad VGS
        i=0
        Canal = ['1','2','3']
        plotVDS = []
        plotIDS =[]
        corriente = 0.4
        self.instrument.write(':OUTP CH' + str(Canal[0]) + ',' + 'ON') #Encendemos canal 1 
        self.instrument.write(':OUTP CH' + str(Canal[1]) + ',' + 'ON')  #Encendemos canal 2
#Barrido de medidas de escritura y lectura para obtener IDS, VGS, VDS de un transistor
        #Limpiamos primero posibles datos anteriores escritos en fuente tension
        self.instrument.write(':INST:NSEL ' + str(Canal[0])) #SELECCIONAMOS CANAL AL QUE IRA LA INFORMACION
        self.instrument.write(':VOLT ' + '0') #SE PONE VOLTAJE A 0 V

        self.instrument.write(':INST:NSEL ' + str(Canal[1])) #SELECCIONAMOS CANAL AL QUE IRA LA INFORMACION
        self.instrument.write(':VOLT ' + '0') #SE PONE VOLTAJE A 0 V

        time.sleep(1) #SE ENCIENDE INSTRUMENTO Y DELAY 1 SEGUNDO ANTES DE EMPEZAR A CAPTURAR MEDIDAS
        for i in range(15):

            time.sleep(1) #delay 1 segundos entre cada medida que se envia y se recibe

            #VOLTAJE SALIDA VDS
            Puntos_VDS.append(Puntos_VDS_inicial_aux)
            self.instrument.write(':INST:NSEL ' + str(Canal[0])) #SELECCIONAMOS CANAL AL QUE IRA LA INFORMACION. Canal[0] es canal 1 en el RIGOL DP832A
            self.instrument.write(':VOLT ' + str(Puntos_VDS[i])) #SACAR VOLTAJE EN CANAL  
            self.instrument.write(':CURR ' + str(corriente)) #SACAR CORRIENTE EN CANAL

            #VOLTAJE SALIDA VGS
            self.instrument.write(':INST:NSEL ' + str(Canal[1])) #SELECCIONAMOS CANAL AL QUE IRA LA INFORMACION
            self.instrument.write(':VOLT ' + str(Puntos_VGS)) #SACAR VOLTAJE EN CANAL 
            self.instrument.write(':CURR ' + str(corriente)) #SACAR CORRIENTE EN CANAL

            #LEEMOS IDS
            ids_value = self.instrument.query(':MEAS:CURR? CH' + Canal[0])
            try:
                Puntos_IDS.append(float(ids_value))
            except ValueError:
                Puntos_IDS.append(0.0)  # En caso de error en la lectura, añadimos 0.0

            Puntos_VDS_inicial_aux += Puntos_VDS_inicial #Se va aumentando la VDS que se envia a la fuente de tension
            Puntos_VGS_inicial_aux += Puntos_VGS_inicial #Se va aumentando la VGS 

            i += 1


        plt.figure(figsize=(10, 6))
        plt.scatter(Puntos_VDS, Puntos_IDS, color='b', marker='o', label='Puntos')
        plt.plot(Puntos_VDS, Puntos_IDS, color='b')
        plt.title('GRAFICA IDS - VDS')
        plt.xlabel('IDS')
        plt.ylabel('VDS')
        plt.legend('VGS')
        plt.grid(True)
        plt.show()


        print('test',self.boxtext_variable_VGS.get()) #testborrar4
        print('test',Puntos_VDS_inicial) #testborrar5
        print('Puntos_VDS:', Puntos_VDS)
        print('Puntos_VGS:', Puntos_VGS)
        print('Puntos IDS',Puntos_IDS)
        #escribir en ventana aviso DE QUE CANALES SE ESTAN UTILZIAN Y QUE ES RESPONSABILIDAD DE USUARIO SU VGS Y VDS LIMITE Y QUE EN NEUSTRO CASO HABRIA QUE PONER UN DISIPADOR SI 
        #QUEREMOS TRABAJAR A MAS DE 4V AUNQUE EL FABRICANTE DIGA QUE VGS Y VDS SEAN 20V
    """

    def graficar_transistor(self):
        Puntos_VDS_inicial = float(self.boxtext_variable_VDS.get()) / 15  # Dividimos VDSmax entre 15 los puntos de VDS para aumentar precisión
        VGS_max = float(self.boxtext_variable_VGS.get())  # Valor máximo de VGS
        VGS_inicial = 2.5  # El valor inicial de VGS es 2V, POR DEBAJO DE ESTE VALOR IDS=0 en casi cualquier transistor
        num_curvas = 6  # Número de curvas a trazar
        Puntos_VGS = [VGS_inicial + i * (VGS_max - VGS_inicial) / (num_curvas - 1) for i in range(num_curvas)]  # Generar 5 puntos de VGS entre 2V y VGS_max del usuario
        Canal = ['1', '2', '3']
        corriente = 0.4

        self.instrument.write(':OUTP CH' + str(Canal[0]) + ',' + 'ON')  # Encendemos canal 1
        self.instrument.write(':OUTP CH' + str(Canal[1]) + ',' + 'ON')  # Encendemos canal 2

        time.sleep(1)  # Delay 1 segundo antes de empezar a capturar medidas

        plt.figure(figsize=(10, 6))

        for VGS in Puntos_VGS:

            # Limpiamos posibles datos anteriores escritos en la fuente de tensión
            self.instrument.write(':INST:NSEL ' + str(Canal[0]))  # Seleccionamos canal al que irá la información
            self.instrument.write(':VOLT ' + '0')  # Se pone voltaje a 0 V

            self.instrument.write(':INST:NSEL ' + str(Canal[1]))  # Seleccionamos canal al que irá la información
            self.instrument.write(':VOLT ' + '0')  # Se pone voltaje a 0 V
            Puntos_VDS_inicial_aux = Puntos_VDS_inicial
            Puntos_IDS = []
            Puntos_VDS = []

            for i in range(15):
                time.sleep(0.8)  # Delay 0.8 segundos entre cada medida que se envía y se recibe

                # Voltaje salida VDS
                Puntos_VDS.append(Puntos_VDS_inicial_aux)
                self.instrument.write(':INST:NSEL ' + str(Canal[0]))  # Seleccionamos canal al que irá la información
                self.instrument.write(':VOLT ' + str(Puntos_VDS[i]))  # Sacar voltaje en canal
                self.instrument.write(':CURR ' + str(corriente))  # Sacar corriente en canal

                # Voltaje salida VGS
                self.instrument.write(':INST:NSEL ' + str(Canal[1]))  # Seleccionamos canal al que irá la información
                self.instrument.write(':VOLT ' + str(VGS))  # Sacar voltaje en canal
                self.instrument.write(':CURR ' + str(corriente))  # Sacar corriente en canal

                # Leemos IDS
                ids_value = self.instrument.query(':MEAS:CURR? CH' + Canal[0])
                try:
                    Puntos_IDS.append(float(ids_value))
                except ValueError:
                    Puntos_IDS.append(0.0)  # En caso de error en la lectura, añadimos 0.0

                Puntos_VDS_inicial_aux += Puntos_VDS_inicial  # Se va aumentando la VDS que se envía a la fuente de tensión


            # Graficar cada curva para un VGS
            plt.plot(Puntos_VDS, Puntos_IDS, marker='o', label=f'VGS = {VGS:.2f} V')

                #Apagamos canales al acabar disparos
        self.instrument.write(':OUTP CH' + str(Canal[0]) + ',' + 'OFF')  
        self.instrument.write(':OUTP CH' + str(Canal[1]) + ',' + 'OFF') 
        plt.title('Curvas IDS - VDS para diferentes VGS')
        plt.xlabel('VDS (V)')
        plt.ylabel('IDS (A)')
        plt.legend()
        plt.grid(True)
        plt.show()

    #NOTA AL PROGRAMADOR. EN ESTE CASO SE UTILIZA UN TRANSISTOR BS170, VGSmax= 4V SI NO SE USA UN DISISPADOR. 


#Creacion de los btones, etiquetas y cajetines
    def Ventana_opciones_FuenteContinua(self):
        messagebox.showinfo("ADVERTENCIA", "SU INSTRUMENDO TIENE VALORES MAXIMOS DE PROTECCION:\n \n CH1: 33V - 3.3 A \n CH2: 33V - 3.3 A \n CH3: 5.5V - 3.3 A")
    # Meter mensaje en textbox  sobre informacion de la direccion del Generador de señal:
    
    # Creacion de Frame que pide escala, offset y canal   
        FuenteConitnua_window = Toplevel()
        FuenteConitnua_window.title('fUENTE CONTINUA RIGOL DP832A: CONFIGURACION OPCIONES')
        FuenteConitnua_window.geometry('1300x750')
        FuenteConitnua_window.resizable(width=False, height=False)
        FuenteConitnua_window.configure(bg=color1)
        
        self.Panel_config_FuentCont= Frame(FuenteConitnua_window, bg=color1, pady=40)
        self.Panel_config_FuentCont.grid(row=0, column=0, sticky="nsew") #self.Panel_config_FuentCont.pack(fill=BOTH, expand=True) Mas abajo se usa grid, para no mezclar con pack, nsew empaqueta en toda la ventana
        self.Panel_config_FuentCont.columnconfigure(0, weight=1)  # Expandir la columna 0
        self.Panel_config_FuentCont.rowconfigure(0, weight=1)     # Expandir la fila 0

        colocacion_filas = 0 #Variable para controlar filas de los botones, etiquetas, cajetines..

        # Etiqueta que identifica cada canal
        Titulo_Canal = Label(self.Panel_config_FuentCont, text=" CANAL1 - 30v/3A ", **colores_label_mediano)
        Titulo_Canal.grid(row=colocacion_filas, column=1, pady=5)

        Titulo_Canal2 = Label(self.Panel_config_FuentCont, text=" CANAL2 - 30v/3A ", **colores_label_mediano)
        Titulo_Canal2.grid(row=colocacion_filas, column=3, pady=5)

        Titulo_Canal3 = Label(self.Panel_config_FuentCont, text=" CANAL3 - 5v/3A ", **colores_label_mediano)
        Titulo_Canal3.grid(row=colocacion_filas, column=5, pady=5, padx=50)

        colocacion_filas += 1 #Siguiente elemento que se añada a pantalla ira una linea de codigo mas abajo

        #Creamos Checkbutton para encender y apagar canales en el RIGOL DP832A (Fuente Continua marca RIGOL)
        j=0
        Canales = ['CANAL1','CANAL2','CANAL3']
        self.variable_ON_OFF = [] #Variable del checkbutton que capturar estado logico '1' o '0'
        colocacion_column_checkbx = 1
        for Canal in Canales:
            self.variable_ON_OFF.append('') #se inicializa vacio para evitar errores al recorrer el bucle
            self.variable_ON_OFF[j] = IntVar()
            Check_ON_OFF = Checkbutton(self.Panel_config_FuentCont, text=f' ON/OFF {Canales[j]}',**colores_checkbox,
                                    variable=self.variable_ON_OFF[j], command=self.Encender_Apagar_Canales)  
            configuracion_boton(Check_ON_OFF)                                                        
            Check_ON_OFF.grid(row = colocacion_filas, column=colocacion_column_checkbx, pady=40)
            j += 1
            colocacion_column_checkbx += 2
        colocacion_filas += 1

        #Creamos etiqueta de las medidas a introducir
        j=0
        colocacion_column_checkbx = 0
        colocacion_filas_V_I = colocacion_filas
        chs=['CH1','CH2','CH3']
        for Canal in Canales:
            #Tension e intensidad deseadas por usuario:
            colocacion_filas_V_I = colocacion_filas #reiniciamos a la 1a fila
            Titulo_Voltaje = Label(self.Panel_config_FuentCont, text=f' Voltaje    {chs[j]}:', **color_texto)
            Titulo_Voltaje.grid(row=colocacion_filas_V_I, column=1 + colocacion_column_checkbx, pady=5,padx=70) #Aumento columna respecto posicion inicial columna 1 
            colocacion_filas_V_I += 1 #ponemos etiqueta intensidad debajo del voltaje
            
            Titulo_Intensidad = Label(self.Panel_config_FuentCont, text=f'Intensidad {chs[j]}:', **color_texto)
            Titulo_Intensidad.grid(row=colocacion_filas_V_I, column=1 + colocacion_column_checkbx, pady=5) 
            colocacion_filas_V_I += 1 #ponemos etiqueta intensidad debajo del voltaje
            #Proteccion de V e I deseadas por el usuario

            Titulo_Voltaje_PROT = Label(self.Panel_config_FuentCont, text=f'Voltaje   PROTECCION   {chs[j]}:', **color_texto)
            Titulo_Voltaje_PROT.grid(row=colocacion_filas_V_I, column=1 + colocacion_column_checkbx, pady=5)
            colocacion_filas_V_I += 1 
            
            Titulo_Intensidad_PROT = Label(self.Panel_config_FuentCont, text=f'Intensidad PROTECCION {chs[j]}:', **color_texto)
            Titulo_Intensidad_PROT.grid(row=colocacion_filas_V_I, column=1 + colocacion_column_checkbx, pady=5) 
            colocacion_column_checkbx += 2
            j += 1
        
        
        #Creamos boxtext para que el usuario meta valores de V salida, I salida  y proteccion V salida e I salida
        colocacion_column_text = 2
        i=0
        #Boxtext donde se introduciran V e I del RIGOL DP832A
        self.boxtext_Vset = []
        self.boxtext_variable_Vset= []
        self.boxtext_Iset = []
        self.boxtext_variable_Iset= []
        #Boxtext donde se introduciran las V e I de PROTECCION del RIGOL DP832A
        self.boxtext_VsetPROT = []
        self.boxtext_variable_VsetPROT= []
        self.boxtext_IsetPROT = []
        self.boxtext_variable_IsetPROT= []
        #El orden logico de impresion de los textbox es recorriendo columna entera de cada canal:
        popupaviso = (self.FuenteConitnua_window.register(self.caracter_valido), '%P') #%P esun comando de tkinter. Es el valor del Entry si pasa la validacion. La validacion llama a la funcion caracter_valido que chequea condiciones
        for Canal in Canales:
            colocacion_filas_text = colocacion_filas
            self.boxtext_Vset.append('')
            self.boxtext_variable_Vset.append('')
            self.boxtext_variable_Vset[i] = StringVar() 
            self.boxtext_variable_Vset[i].set('0') #La cajetilla se inicializa en 1V/div
            
            self.boxtext_Vset[i] = Entry(self.Panel_config_FuentCont, 
                                              state=DISABLED, 
                                              textvariable=self.boxtext_variable_Vset[i],**colores_textbox_mediano, validate='key', validatecommand=popupaviso)
            self.boxtext_Vset[i].grid(row=colocacion_filas_text,column=colocacion_column_text, padx=25)
            configuracion_boton(self.boxtext_Vset[i])
            colocacion_filas_text += 1
            
            self.boxtext_Iset.append('')
            self.boxtext_variable_Iset.append('')
            self.boxtext_variable_Iset[i] = StringVar() 
            self.boxtext_variable_Iset[i].set('0') #La cajetilla se inicializa en 1V/div
            
            self.boxtext_Iset[i] = Entry(self.Panel_config_FuentCont, 
                                              state=DISABLED, 
                                              textvariable=self.boxtext_variable_Iset[i],**colores_textbox_mediano, validate='key', validatecommand=popupaviso)
            self.boxtext_Iset[i].grid(row=colocacion_filas_text,column=colocacion_column_text, padx=25)
            configuracion_boton(self.boxtext_Iset[i])
            colocacion_filas_text+= 1
            
            #Se procede igual para la V e I de proteccion que debemos enviar al RIGOL DP832A
            #Por defecto daremos el valor maximo del fabricante 33.0V y 3.3A
            
            self.boxtext_VsetPROT.append('')
            self.boxtext_variable_VsetPROT.append('')
            self.boxtext_variable_VsetPROT[i] = StringVar() 
            self.boxtext_variable_VsetPROT[i].set('33') #La cajetilla se inicializa en 1V/div
            
            self.boxtext_VsetPROT[i] = Entry(self.Panel_config_FuentCont, 
                                              state=DISABLED, 
                                              textvariable=self.boxtext_variable_VsetPROT[i],**colores_textbox_mediano, validate='key', validatecommand=popupaviso)
            self.boxtext_VsetPROT[i].grid(row=colocacion_filas_text,column=colocacion_column_text, padx=25)
            configuracion_boton(self.boxtext_VsetPROT[i])
            colocacion_filas_text += 1
            
            self.boxtext_IsetPROT.append('')
            self.boxtext_variable_IsetPROT.append('')
            self.boxtext_variable_IsetPROT[i] = StringVar() 
            self.boxtext_variable_IsetPROT[i].set('3.3') #La cajetilla se inicializa en 1V/div
            
            self.boxtext_IsetPROT[i] = Entry(self.Panel_config_FuentCont, 
                                              state=DISABLED, 
                                              textvariable=self.boxtext_variable_IsetPROT[i],**colores_textbox_mediano, validate='key', validatecommand=popupaviso)
            self.boxtext_IsetPROT[i].grid(row=colocacion_filas_text,column=colocacion_column_text, padx=25)
            configuracion_boton(self.boxtext_IsetPROT[i])

            colocacion_column_text += 2
            i += 1

        self.boxtext_variable_VsetPROT[2].set('5.5') #El ultimo canal tiene una configuracion especial, lo marcamos fuera del bucle y se sobre escribe la informacion erronea 
                                                     #5.5V de proteccion en el CANAL 3 del instrumento RIGOL DP832A

        colocacion_filas = colocacion_filas_text + 1 #La nueva fila estara donde paro el bucle de impresion + 1 fila
        
        #Boton que envia informacion al RIGOL DP832A y llama al command que contiene los SCPI necesarios
        EnviarInfo = Button(self.Panel_config_FuentCont,text='RECIBIR DATOS',
                                    command=self.Enviar_Info, **colores_boton) 
        EnviarInfo.grid(row=colocacion_filas, column=3, padx=50, pady=50)
        configuracion_boton(EnviarInfo)
        
        #Boton para utilizar aplicacion de transistor. Se abre ventana que pide VGS, VDS y grafica ID
        Transistor_app = Button(self.Panel_config_FuentCont,text='TRANSISTOR',
                                    command=self.Ventana_Aplicacion_transistor, **colores_boton) 
        Transistor_app.grid(row=colocacion_filas, column=5, padx=50, pady=50)
        configuracion_boton(Transistor_app)

        colocacion_filas += 1
        self.colocar_filar_respuesta = colocacion_filas #La copiamos como variable global de la clase para tene rreferencia de fila cuando demos al usuario la respuesta del RIGOL DP832 A

#Se comprueba que en las cajetillas de texto solo se meta puntos y numeros

    def caracter_valido(self, nuevo_valor):
        if nuevo_valor == "" or self.es_valido(nuevo_valor): #pasamos a la funcion es valido el valor introducido
            return True
        else:
            messagebox.showerror("Introduzca caracter valido", "Caracteres admitidos:  0123456789.")
            return False

    def es_valido(self, valor):
        #Comprobamos si el nuevo numero solo tiene numeros y punto
        for char in valor:
            if char not in "0123456789.":
                return False
        return True #devolvemos falso o true a la funcion caracter_valido para que imprima popup de aviso si corresponde o ignorar
#-------------------------------------------------
# LECTURA Y ESCRITURA A TRAVES DE COMANDOS SCPI :
#------------------------------------------------
    def Encender_Apagar_Canales (self):
        
        Canales = ['1','2','3']
        j=0
        for Canal in Canales:
            if (self.variable_ON_OFF[j].get() == 1):
                self.boxtext_Vset[j].config(state=NORMAL) #El cuadro pasa a ser editable
                self.boxtext_Vset[j].focus() #establece el foco en un cuadro sin que el usuario tenga que hacer clic en el
                self.boxtext_Iset[j].config(state=NORMAL)
                self.boxtext_Iset[j].focus()
                self.boxtext_VsetPROT[j].config(state=NORMAL) #El cuadro pasa a ser editable
                self.boxtext_VsetPROT[j].focus() #establece el foco en un cuadro sin que el usuario tenga que hacer clic en el
                self.boxtext_IsetPROT[j].config(state=NORMAL)
                self.boxtext_IsetPROT[j].focus()
                
                self.instrument.write(':OUTP CH' + str(Canal) + ',' + 'ON') #ON si checkbox true-> SCPI
            else:
                self.instrument.write(':OUTP CH' + str(Canal) + ',' + 'OFF') #OFF si checkbox null -> SCPI
                
            j += 1
            
    def Enviar_Info(self):

        #Variables para recoger la V e I que este consumiendo la carga. Sera de tipo lista porque son 3 canales y habra que inicializar la lista fuera y dentro del bucle.
        medir_corriente = []
        medir_pow = []
        medir_volt = []
        
        
        Canales = ['1','2','3']
        j=0

        for Canal in Canales:
            medir_corriente.append('')
            medir_pow.append('')
            medir_volt.append('')
            if (self.variable_ON_OFF[j].get() == 1):  
                #Escritura enviada a RIGOL DP832A
                #VOLTAJE SALIDA
                self.instrument.write(':INST:NSEL ' + str(Canal)) #SELECCIONAMOS CANAL AL QUE IRA LA INFORMACION
                self.instrument.write(':VOLT ' + str(self.boxtext_variable_Vset[j].get())) #SACAR VOLTAJE EN CANAL  
                
                #CORRIENTE SALIDA
                self.instrument.write(':INST:NSEL ' + str(Canal)) #SELECCIONAMOS CANAL AL QUE IRA LA INFORMACION
                self.instrument.write(':CURR ' + str(self.boxtext_variable_Iset[j].get())) #SACAR CORRIENTE EN CANAL

                #VOLTAJE PROTECCION
                self.instrument.write(':INST:NSEL ' + str(Canal)) #SELECCIONAMOS CANAL AL QUE IRA LA INFORMACION
                self.instrument.write(':VOLT:PROT ' + str(self.boxtext_variable_VsetPROT[j].get())) #VOLTAJE PROTECCION EN CANAL

                #CORRIENTE PROTECCION
                self.instrument.write(':INST:NSEL ' + str(Canal)) #SELECCIONAMOS CANAL AL QUE IRA LA INFORMACION
                self.instrument.write(':CURR:PROT ' + str(self.boxtext_variable_IsetPROT[j].get())) #CORRIENTE PROTECCION EN CANAL

                #Lecturas que recibimos de las cargas
                #MEDIR VOLTAJE
                medir_volt[j] = self.instrument.query(':MEAS:VOLT? CH' + str(Canal))
            
                #MEDIR CORRIENTE
                medir_corriente[j] = self.instrument.query(':MEAS:CURR? CH' + str(Canal))

                #MEDIR POTENCIA
                medir_pow[j] = self.instrument.query(':MEAS:POWE? CH' + str(Canal))
                
            else:
                medir_volt[j] = 0
                medir_corriente[j] = 0
                medir_pow[j] = 0
            
            j += 1

        #El RIGOL DP832A envia la respuesta como entero que contiene el caracter \n. Necesitamos suprimir dicho caracter para trabajar solo con numeros. 
        #Se procede a hacerlo con las tres lecturas.
        medir_volt_limpio = []
        for medvolt in medir_volt:
            medvolt_str = str(medvolt)
            medir_volt_limpio.append(medvolt_str.strip('\n')) #Suprimimos el \n

        medir_corriente_limpio = []
        for corriente in medir_corriente:
            corriente_str = str(corriente)
            medir_corriente_limpio.append(corriente_str.strip('\n')) 

        medir_pow_limpio = []
        for medpow in medir_pow:
            medpow_str = str(medpow)
            medir_pow_limpio.append(medpow_str.strip('\n'))

        #Ahora se proporciona la informacion recibida del RIGOL DP832A al usuario
        j=0
        colocacion_columnas = 1
        for Canal in Canales:
            colocacion_filas = self.colocar_filar_respuesta
            if (self.variable_ON_OFF[j].get() == 1):
                Valores_consumo = Label(self.Panel_config_FuentCont, text=f'Vconsumida carga: {medir_volt_limpio[j]} V \n Iconsumida carga: {medir_corriente_limpio[j]} A \n Potencia consumida: {medir_pow_limpio[j]} W', **colores_label_canales)
                Valores_consumo.grid(row=colocacion_filas, column=colocacion_columnas, pady=5)
                
            colocacion_columnas += 2
            j += 1
            
        
        print('volts: ',medir_volt)
        print('Is: ',medir_corriente)
           
           









    #----------------------------------------------------------------------
    #-------------------FIN  CODIGO FUENTE CONTINUA -----------------------
    #----------------------------------------------------------------------
