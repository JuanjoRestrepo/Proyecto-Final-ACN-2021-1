import tkinter
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import *
from tkinter import messagebox


###funcion prueba

def test():
    global L
    global N
    global dt
    global tfinal

    L=int(Lo.get())
    N=int(No.get())
    dt=float(dto.get())
    tfinal=int(tfinalo.get())

    # print(Li)
    # print(Ni)
    # print(dti)
    # print(tfinali)



###aqui empieza la parte grafica de tkinter#####################
window=Tk()
#titulo de la ventana
window.title('Proyecto Final')

#etiqueta de la longitud de cuerda con su entry box
Lo=tk.IntVar()
lbl0=Label(window, text="Longitud de la Cuerda: ", fg='black')
lbl0.place(x=60, y=50)
txtfld0=Entry(window,bg='white',fg='black', bd=5,textvariable=Lo)
txtfld0.place(x=320, y=45)


##etiqueta del numero de nodos con su entry box
No=tk.IntVar()
lbl1=Label(window, text="Ingrese Numero de Nodos/Particiones: ", fg='black')
lbl1.place(x=60, y=90)
txtfld1=Entry(window,bg='white',fg='black', bd=5,textvariable=No)
txtfld1.place(x=320, y=85)

##etiqueta de entrada del dt con su entry box
dto=tk.StringVar()
lbl2=Label(window, text="Ingrese un Delta de T: ", fg='black')
lbl2.place(x=60, y=130)
txtfld2=Entry(window,bg='white',fg='black', bd=5,textvariable=dto)
txtfld2.place(x=320, y=125)

##etiqueta del tiempo a simular con su entry box
tfinalo=tk.IntVar()
lbl2=Label(window, text="Ingrese Tiempo a Simular: ", fg='black')
lbl2.place(x=60, y=170)
txtfld2=Entry(window,bg='white',fg='black', bd=5,textvariable=tfinalo)
txtfld2.place(x=320, y=165)

#boton para ejecutar la funcion
btn=Button(window, text="Ejecutar", fg='black',command=test).pack()
#btn.place(x=250, y=250)

window.geometry("600x350")
window.mainloop()


###aqui empieza el programa

#datos
############L = float(input('longitud de la cuerda: '))##1.##entrada1
##L=float(Lo.get())

global L
#global N
global dt
global tfinal

L=int(Lo.get())
N=int(No.get())
dt=float(dto.get())
tfinal=int(tfinalo.get())
c = 0.8##entrada->porsilas

#discretizacion
##N = int(No.get())##10
############N=0
############while N<=1:
    ############N = int(input('Ingrese Numero de Nodos/Particiones: '))##10
    
x = np.linspace(0, L, N)
dx = L/(N-1)

#condicion inicial
t = 0.
uinc = 0.5
u = np.ones(N)*uinc
v = np.zeros(N)

#condiciones de frontera
u0 = 0
uL = 0
u[0] = u0
u[-1] = uL

#criterio de estabilidad
dtestable = dx/c

#solucion con el tiempo
#dt=float(input('Ingrese un Delta de T: '))
##dt = float(dto.get)##0.01##entrada

##tfinal = float(tfinalo.get())##20.##entrada
udt = u.copy()
u_dt = u.copy()

usolucion = [u]
vsolucion = [v]
tsolucion = [t]

while t < tfinal:
    #condicion inicial
    if t == 0.:
        for i in range(N):
            if i == 0:
                udt[i] = u0
            elif i == N-1:
                udt[i] = uL
            else:
                udt[i] = ( (c**2*dt**2/(2*dx**2))*u[i-1]
                           + (1 - c**2*dt**2/dx**2)*u[i]
                           + (c**2*dt**2/(2*dx**2))*u[i+1] )

    #en otro tiempo t
    else:
        for i in range(N):
            if i == 0:
                udt[i] = u0
            elif i == N-1:
                udt[i] = uL
            else:
                udt[i] = ( (c**2*dt**2/dx**2)*u[i-1]
                           + (2 - 2*c**2*dt**2/dx**2)*u[i]
                           + (c**2*dt**2/dx**2)*u[i+1]
                           - u_dt[i])
    u_dt = u.copy()
    u = udt.copy()
    v = (udt - u_dt)/(2*dt)
    t = t + dt
    usolucion.append(u)
    vsolucion.append(v)
    tsolucion.append(t)

usolucion = np.round(np.array(usolucion),3)
vsolucion = np.round(np.array(vsolucion),3)
tsolucion = np.round(np.array(tsolucion),3)

import matplotlib.animation as animation
fig = plt.figure()
ax = plt.gca()

def actualizar(i):
    ax.clear()
    plt.plot(x,usolucion[i], 'ro')
    plt.title(str(tsolucion[i]))
    plt.xlim(0,L)
    plt.ylim(-1,1)

ani = animation.FuncAnimation(fig,actualizar, range(len(tsolucion)))
plt.show()
#print("Exito papi\n;v")
