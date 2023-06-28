from tkinter import *
from enero_batery import *
# from febrero_batery import *
# from marzo_batery import *
# from abril_batery import *
# from mayo_batery import *
# from junio_batery import *
# from julio_batery import *
# from agosto_batery import *
# from septiembre_batery import *
# from octubre_batery import *

#Estableciendo la ventana root 
root = Tk()

#Creación del frame principal 
frame = Frame(root)
frame.pack()

#Variable de control para el mes de operacion 
mesDeOperacion = StringVar(frame)
#Setenado un valor por defecto al mes de operacion
mesDeOperacion.set("")

#Varible de control para el uso de baterias
bancoDeBateria = StringVar(frame)
#Setenado un valor por defecto a la variable
bancoDeBateria.set("no")


#Funcion invocada por el boton calcular
def calcular():
    cu = float(variableCu.get())
    c =  float(variableC.get())
    d = float(variableD.get())
    mes= str(mesDeOperacion.get())
    bateria = str(bancoDeBateria.get())

    #Inicializando los valores de PPV
    Valoresppv = str(variableppv.get())
    valoresppv_divi = Valoresppv.split(',')
    dicppv = {}

    #Inicializando los valores de PLoad
    valoresPLoad = str(variablepLoad.get())
    valorespload_divi = valoresPLoad.split(',')
    dicpload = {}

    #Diccionario de valores Prem
    dicPrem = {}
    #Procesamiento de los diccionarios que contienen los valores de PPV, PLoad, Prem 
    for i in range(24):
        dicppv[i+1] = float(valoresppv_divi[i])
        dicpload[i+1] = float(valorespload_divi[i])
        dicPrem[i+1] = float(float(valoresppv_divi[i]) - float(valorespload_divi[i]))
    
    #Escogiendo el algoritmo del mes en que se trabajara
    if(mes=="Enero"):
        algoritmoEnero(cu,c,d,dicppv,dicpload,dicPrem,bateria)
    elif(mes=="Febrero"):
        pass
    elif(mes=="Marzo"):
        pass
    elif(mes=="Abril"):
        pass
    elif(mes=="Mayo"):
        pass
    elif(mes=="Junio"):
        pass
    elif(mes=="Julio"):
        pass
    elif(mes=="Agosto"):
        pass
    elif(mes=="Septiembre"):
        pass
    elif(mes=="Octubre"):
        pass
    print("PDF GENERADO")
    print("Excel generado")

#Funcion seteo de mes
def escogerMes(mes):
    mesDeOperacion.set(mes)
    print(mesDeOperacion.get())

def SeleccionBateria(bateria):
    bancoDeBateria.set(bateria)
    print(bancoDeBateria.get())
#Creacion de menu de configuracion de operacion
barraMenu = Menu(root)

#Menu de los meses de operacion 
menu_desplegable1 = Menu(barraMenu, tearoff=0)
menu_desplegable1.add_command(label="Enero", command=lambda:escogerMes("Enero"))
menu_desplegable1.add_command(label="Febrero", command=lambda:escogerMes("Febrero"))
menu_desplegable1.add_command(label="Marzo", command=lambda:escogerMes("Marzo"))
menu_desplegable1.add_command(label="Abril", command=lambda:escogerMes("Abril"))
menu_desplegable1.add_command(label="Mayo", command=lambda:escogerMes("Mayo"))
menu_desplegable1.add_command(label="Junio", command=lambda:escogerMes("Junio"))
menu_desplegable1.add_command(label="Julio", command=lambda:escogerMes("Julio"))
menu_desplegable1.add_command(label="Agosto", command=lambda:escogerMes("Agosto"))
menu_desplegable1.add_command(label="Septiembre", command=lambda:escogerMes("Septiembre"))
menu_desplegable1.add_command(label="Octubre", command=lambda:escogerMes("Octubre"))
barraMenu.add_cascade(label="Mes de operacion", menu=menu_desplegable1)

#Menu para escoger trabajar o no con bateria
menu_desplegable2 = Menu(barraMenu, tearoff=0)
menu_desplegable2.add_command(label="Si", command=lambda:SeleccionBateria("si"))
menu_desplegable2.add_command(label="No", command=lambda:SeleccionBateria("no"))
barraMenu.add_cascade(label="Banco de bateria", menu=menu_desplegable2)


root.config(menu=barraMenu)

#Ruta de accesos logo manglar
LogoManglar = PhotoImage(file="recursos/LogoManglar.png")
LogoManglar_redimensionado = LogoManglar.subsample(3,4)
#Label del logo 
label_logo_manglar= Label(frame,image = LogoManglar_redimensionado)
label_logo_manglar.grid(row=1, column=0, pady=10,columnspan=4)


#Etiqueta de la varible Cu
labelCu = Label(frame, text="Cu:")
labelCu.grid(row=2, column=0, padx=10)
#Input de la varible Cu 
Cu = DoubleVar()
variableCu = Entry(frame, textvariable=Cu)
variableCu.grid(row=3, column=0, padx=10, pady=2)
variableCu.config(background="black", fg="#03f943", justify="right")

#Etiqueta de la varible C
labelC = Label(frame, text="C:")
labelC.grid(row=2, column=1, padx=10)
#Input de la Varible C
C = DoubleVar()
variableC= Entry(frame, textvariable=C)
variableC.grid(row=3, column=1, padx=10, pady=2)
variableC.config(background="black", fg="#03f943", justify="right")

#Etiqueta de la varible D
labelD = Label(frame, text="D:")
labelD.grid(row=2, column=2, padx=10)
#Input de la Varible D
D = DoubleVar()
variableD= Entry(frame, textvariable=D)
variableD.grid(row=3, column=2, padx=10, pady=2)
variableD.config(background="black", fg="#03f943", justify="right")

#Etiqueta de la varible ppv
labelppv = Label(frame, text="ppv:")
labelppv.grid(row=2, column=3, padx=10)
#Input de la Varible ppv
ppv = StringVar()
variableppv= Entry(frame, textvariable=ppv)
variableppv.grid(row=3, column=3, padx=10, pady=2)
variableppv.config(background="black", fg="#03f943", justify="right")

#Etiqueta de la varible pLoad
labelpLoad = Label(frame, text="PLoad:")
labelpLoad.grid(row=2, column=4, padx=10)
#Input de la Varible pLoad
pLoad = StringVar()
variablepLoad= Entry(frame, textvariable=pLoad)
variablepLoad.grid(row=3, column=4, padx=10, pady=2)
variablepLoad.config(background="black", fg="#03f943", justify="right")


#Boton para realizar el calculo 
calculo = Button(frame, text="calcular", width=20, command=lambda:calcular())
calculo.grid(row=4, column=2,padx=2, pady=15)



root.mainloop()


