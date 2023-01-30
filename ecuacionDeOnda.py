
import numpy as np
import matplotlib.pyplot as plt

#datos
L = 1.
c = 1.5

#discretizacion
N = 5
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
dt = 0.1
tfinal = 20.
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
print("Exito papi\n;v")
