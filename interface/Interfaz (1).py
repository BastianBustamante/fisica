# -*- coding: utf-8 -*-
import tkinter as tk
import matplotlib.animation as ani
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import matplotlib.pyplot as plt
import tkinter
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from tkinter import *
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)

def toggle(event):
    global tog
    if tog == True:
        t_btn.config(image=off)
        tog = False
    else:
        t_btn.config(image=on)
        tog = True


def quit():
    raiz.destroy()

def gen(n):
    t = 0
    r = 5
    while t < 8 * np.pi:
        yield np.array([r * np.cos(t), r * np.sin(t), t])
        t += 5.5 * np.pi / n

def update(num, data, line):
    line.set_data(data[:2, :num])
    line.set_3d_properties(data[2, :num])


if __name__ == "__main__":

    tog = False
    fig = plt.figure()
    raiz = tkinter.Tk()
    raiz.title("Fisica interactiva")
    raiz.geometry("900x900")
    frame = Frame(raiz,width=300,height=800)
    frame.place(x=240,y=100)
    canvas=FigureCanvasTkAgg(fig,master=frame)
    canvas.get_tk_widget().pack(side='top',fill='both')
    Label(raiz, text="Helice Circular", font=("letter case", 50)).place(x=250, y=5)

    atras = Button(raiz, text="Atras", width=15, height=2,command=raiz.destroy).place(x=20, y=5)

    posicion = tkinter.Button(raiz, text="Posicion", width=15,height=2).place(x=20, y=70)
    velocidad = Button(raiz, text="Velocidad", width=15, height=2).place(x=20, y=130)
    velocidadm = Button(raiz, text="Velocidad Media", width=15, height=2).place(x=20, y=190)
    aceleracion = Button(raiz, text="Aceleracion", width=15, height=2).place(x=20, y=250)
    aceleracionm = Button(raiz, text="Aceleracion Media", width=15, height=2).place(x=20, y=310)
    curvatura = Button(raiz, text="Curvatura", width=15, height=2).place(x=20, y=370)
    radiocurvatura = Button(raiz, text="Radio de Curvatura", width=15, height=2).place(x=20, y=430)
    torsion = Button(raiz, text="Torsion", width=15, height=2).place(x=20, y=490)
    radiotorsion = Button(raiz, text="Radio de Torsion", width=15, height=2).place(x=20, y=550)
    longitudarco = Button(raiz, text="Longitud de Arco", width=15, height=2).place(x=20, y=610)

    #boton de animacion
    on = tk.PhotoImage(file="on.gif")
    off = tk.PhotoImage(file="off.gif")

    t_btn = tk.Label(width=12, image = off)
    t_btn.bind('<Button-1>', toggle)
    t_btn.pack
    t_btn.place(x=840, y = 10, height = 15, width = 27)
    labelk = tk.Label(master = raiz , text = "Animación")
    labelk.place(x=820, y = 30)


    input1 = Label(raiz, text="A", width=7, height=3).place(x=280, y=660)
    cuadroTexto1 = Entry(raiz)
    cuadroTexto1.place(x=250, y=650)

    input2 = Label(raiz, text="B", width=7, height=3).place(x=440, y=660)
    cuadroTexto2 = Entry(raiz)
    cuadroTexto2.place(x=410, y=650)

    input3 = Label(raiz, text="C", width=7, height=3).place(x=600, y=660)
    cuadroTexto3 = Entry(raiz)
    cuadroTexto3.place(x=570, y=650)

    input4 = Label(raiz, text="D", width=7, height=3).place(x=740, y=660)
    cuadroTexto4 = Entry(raiz)
    cuadroTexto4.place(x=720, y=650)

    ax = p3.Axes3D(fig)

    N = 100
    data = np.array(list(gen(N))).T
    line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1], label='Curva Helice Circular')
    ax.legend()

    # Setting the axes properties

    ax.set_xlim3d([-8.0, 8.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([-8.0, 8.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([0.0, 16.0])
    ax.set_zlabel('Z')
    ani = animation.FuncAnimation(fig, update, N, fargs=(data, line), interval=16, repeat=False)
    #plt.show()
    raiz.mainloop()