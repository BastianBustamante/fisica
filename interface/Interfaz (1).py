# -*- coding: utf-8 -*-
import tkinter as tk
import matplotlib.animation as ani
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import matplotlib.animation as ani
import mpl_toolkits.mplot3d.axes3d as p3
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)


def sys_exit():
    tk.close()


def toggle(event):
    global tog
    if tog == True:
        t_btn.config(image=off)
        tog = False
    else:
        t_btn.config(image=on)
        tog = True

def posicion_ejemplo(root):
    fig = plt.figure()
    frame = tk.Frame(root, width=300, height=800)
    frame.place(x=300, y=170, height=406, width=502)
    canvas = FigureCanvasTkAgg(fig, master=frame)
    canvas.get_tk_widget().pack(side='top', fill='both')
    ax = p3.Axes3D(fig)

    def gen(n):
        r = 5
        for theta in np.linspace(0, 5 * np.pi, 99):
            yield np.array([r * np.cos(theta), r * np.sin(theta), theta])
            theta += 5.5 * np.pi / n

    def update(num, data, line):
        line.set_data(data[:2, :num])
        line.set_3d_properties(data[2, :num])

    N = 100
    data = np.array(list(gen(N))).T
    line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1], label='Curva Helice Circular')

    ax.set_xlim3d([-8.0, 8.0])
    ax.set_xlabel('X')

    ax.set_ylim3d([-8.0, 8.0])
    ax.set_ylabel('Y')

    ax.set_zlim3d([0.0, 16.0])
    ax.set_zlabel('Z')
    anim = ani.FuncAnimation(fig, update, N, fargs=(data, line), interval=16, repeat=False)
    ax.legend()
    canvas._tkcanvas.pack(side='top', fill='both', expand=1)
    tk.mainloop()


def posicion(root,a,b):
    if len(a.get()) == 0:
        pass
    else:
        if tog==True:
            fig = plt.figure()
            frame = tk.Frame(root, width=300, height=800)
            frame.place(x=300, y=170, height=406, width=502)
            canvas = FigureCanvasTkAgg(fig, master=frame)
            canvas.get_tk_widget().pack(side='top', fill='both')
            ax = p3.Axes3D(fig)

            def gen(n):
                r=5
                for theta in np.linspace(0, 5 * np.pi, 99):
                    yield np.array([r * np.cos(theta), r * np.sin(theta), theta])
                    theta += 5.5 * np.pi / n

            def update(num, data, line):
                line.set_data(data[:2, :num])
                line.set_3d_properties(data[2, :num])

            N = 100
            plt.rcParams['legend.fontsize'] = 12
            data = np.array(list(gen(N))).T
            line, = ax.plot(data[0, 0:1], data[1, 0:1], data[2, 0:1], label='Curva Helice Circular')
            ax.set_xlim3d([-8.0, 8.0])
            ax.set_xlabel('X')

            ax.set_ylim3d([-8.0, 8.0])
            ax.set_ylabel('Y')

            ax.set_zlim3d([0.0, 16.0])
            ax.set_zlabel('Z')
            anim = ani.FuncAnimation(fig, update, N, fargs=(data, line), interval=1700 / N, repeat=False)
            ax.legend()
            canvas._tkcanvas.pack(side='top', fill='both', expand=1)
            tk.mainloop()
        else:
            fig = plt.figure()
            frame = tk.Frame(root, width=300, height=800)
            frame.place(x=240, y=240, height=546, width=642)
            canvas = FigureCanvasTkAgg(fig, master=frame)
            canvas.get_tk_widget().pack(side='top', fill='both')
            ax = p3.Axes3D(fig)
            plt.rcParams['legend.fontsize'] = 12
            ax = fig.gca(projection='3d')
            # Prepare arrays x, y, z
            ax.set_xlim3d([-8.0, 8.0])
            ax.set_xlabel('X')

            ax.set_ylim3d([-8.0, 8.0])
            ax.set_ylabel('Y')

            ax.set_zlim3d([0.0, 16.0])
            ax.set_zlabel('Z')
            theta = np.linspace(-8 * np.pi, 8 * np.pi, 99)
            a_p = int(a.get())
            r_p = int(b.get())
            x = r_p * np.cos(theta)
            y = r_p * np.sin(theta)
            z = a_p*theta
            ax.plot(x, y, z, label='Helice circular')

            ax.legend()
            canvas._tkcanvas.pack(side='top', fill='both', expand=1)
            #plt.show()
            tk.mainloop()
def spd():
    Circular_button1.config(relief="raised")
    Circular_button2.config(relief="sunken")
    Circular_button3.config(relief="raised")
    Circular_button4.config(relief="raised")
    Circular_button5.config(relief="raised")
    Circular_button6.config(relief="raised")
    Circular_button7.config(relief="raised")
    Circular_button8.config(relief="raised")
    Circular_button9.config(relief="raised")
    Circular_button10.config(relief="raised")
    entry.config(state='disabled')
    entry1.config(state='disabled')
    entry2.config(state='normal')
    entry3.config(state='disabled')
    label3.config(text="t")
    button_calcp.config(command=velocidad)


def velocidad():
    if (len(a.get()) != 0 and len(b.get()) != 0 and len(c.get()) != 0):
        ventana_spd = tk.Tk()
        ventana_spd.wm_title("Velocidad")
        ventana_spd.geometry("376x131")
        button = tk.Button(master=ventana_spd, text="Atrás", command=ventana_spd.destroy)
        x = -int(b.get()) * np.sin(int(c.get()))
        y = int(b.get()) * np.cos(int(c.get()))
        z = 1
        solucion = ("La velocidad es " + " x: " + str('%.3f'%(x)) + " y: " + str('%.3f'%(y)) + " z: " + str('%.3f'%(z)))
        entry_respuesta = tk.Label(master=ventana_spd, text=solucion)
        entry_respuesta.pack()
        ventana_spd.resizable(0, 0)
        ventana_spd.mainloop()


def aceleracion():
    if (len(a.get()) != 0 and len(b.get()) != 0 and len(c.get()) != 0):
        ventana_acc = tk.Tk()
        ventana_acc.wm_title("Aceleracion")
        ventana_acc.geometry("376x131")
        button = tk.Button(master=ventana_acc, text="Atrás", command=ventana_acc.destroy)
        x = int(b.get()) * np.cos(int(c.get()))
        y = - int(b.get()) * np.sin(int(c.get()))
        z = 0
        solucion = ("La aceleración es " + " x: " + str('%.3f' % (x)) + " y: " + str('%.3f' % (y)) + " z: " + str(
            '%.3f' % (z)))
        entry_respuesta = tk.Label(master=ventana_acc, text=solucion)
        entry_respuesta.pack()
        ventana_acc.resizable(0, 0)
        ventana_acc.mainloop()
def aceleracionmedia():
    ventana_acc = tk.Tk()
    ventana_acc.wm_title("Aceleracion Media")
    ventana_acc.geometry("376x131")
    x = -int(b.get()) * np.sin(int(c.get()))
    y = int(b.get()) * np.cos(int(c.get()))
    z = 1
    x2 = -int(b.get()) * np.sin(int(d.get()))
    y2 = int(b.get()) * np.cos(int(d.get()))
    z2 = 1
    xa = (x2-x)/(int(d.get())-int(c.get()))
    ya = (y2-y)/(int(d.get())-int(c.get()))
    za = 0
    solucion = "la aceleracion media es " + "x: " + str('%.3f' % (xa)) + " y: " + str('%.3f' % (ya)) + " z: " + str('%.3f' % (za))
    entry_respuesta = tk.Label(master=ventana_acc, text=solucion)
    entry_respuesta.pack()
def velocidadmedia():
    ventana_acc = tk.Tk()
    ventana_acc.wm_title("Velocidad Media")
    ventana_acc.geometry("376x131")
    a_p = int(a.get())
    r_p = int(b.get())
    t = int(c.get())
    x = r_p * np.cos(t)
    y = r_p * np.sin(t)
    z = a_p*t
    t2 = int(d.get())
    x2 = r_p * np.cos(t2)
    y2 = r_p * np.sin(t2)
    z2 = a_p*t2
    xv = (x2-x)/(t2-t)
    yv = (y2-y)/(t2-t)
    zv = (z2-z)/(t2-t)
    solucion ="la velocidad media es "+"x: "+str('%.3f' % (xv))+" y: "+str('%.3f' % (yv)) + " z: "+str('%.3f' % (zv))
    entry_respuesta = tk.Label(master=ventana_acc, text=solucion)
    entry_respuesta.pack()
    ventana_acc.resizable(0, 0)
    ventana_acc.mainloop()
def spdm():
    Circular_button1.config(relief="raised")
    Circular_button3.config(relief="sunken")
    Circular_button2.config(relief="raised")
    Circular_button4.config(relief="raised")
    Circular_button5.config(relief="raised")
    Circular_button6.config(relief="raised")
    Circular_button7.config(relief="raised")
    Circular_button8.config(relief="raised")
    Circular_button9.config(relief="raised")
    Circular_button10.config(relief="raised")
    label3.config(text="ti")
    label4.config(text="tf")
    entry.config(state='disabled')
    entry1.config(state='disabled')
    entry2.config(state='normal')
    entry3.config(state='normal')
    button_calcp.config(command=velocidadmedia)


def pos(root,a,b):
    entry3.config(state='disabled')
    Circular_button1.config(relief="sunken")
    Circular_button2.config(relief="raised")
    Circular_button3.config(relief="raised")
    Circular_button4.config(relief="raised")
    Circular_button5.config(relief="raised")
    Circular_button6.config(relief="raised")
    Circular_button7.config(relief="raised")
    Circular_button8.config(relief="raised")
    Circular_button9.config(relief="raised")
    Circular_button10.config(relief="raised")
    entry.config(state='normal')
    entry1.config(state='normal')
    entry2.config(state='disabled')
    entry3.config(state='disabled')
    button_calcp.config(command=lambda:posicion(root, a, b))


def acc():
    Circular_button1.config(relief="raised")
    Circular_button2.config(relief="raised")
    Circular_button3.config(relief="raised")
    Circular_button4.config(relief="sunken")
    Circular_button5.config(relief="raised")
    Circular_button6.config(relief="raised")
    Circular_button7.config(relief="raised")
    Circular_button8.config(relief="raised")
    Circular_button9.config(relief="raised")
    Circular_button10.config(relief="raised")
    button_calcp.config(command=aceleracion)
    label3.config(text="t")
    entry.config(state='disabled')
    entry1.config(state='disabled')
    entry2.config(state='normal')
    entry3.config(state='disabled')
def accm():
    Circular_button1.config(relief="raised")
    Circular_button2.config(relief="raised")
    Circular_button3.config(relief="raised")
    Circular_button4.config(relief="raised")
    Circular_button5.config(relief="sunken")
    Circular_button6.config(relief="raised")
    Circular_button7.config(relief="raised")
    Circular_button8.config(relief="raised")
    Circular_button9.config(relief="raised")
    Circular_button10.config(relief="raised")
    button_calcp.config(command=aceleracionmedia)
    label3.config(text="ti")
    label4.config(text="tf")
    entry.config(state='disabled')
    entry1.config(state='disabled')
    entry2.config(state='normal')
    entry3.config(state='normal')


def curv():
    Circular_button1.config(relief="raised")
    Circular_button2.config(relief="raised")
    Circular_button3.config(relief="raised")
    Circular_button4.config(relief="raised")
    Circular_button5.config(relief="raised")
    Circular_button6.config(relief="sunken")
    Circular_button7.config(relief="raised")
    Circular_button8.config(relief="raised")
    Circular_button9.config(relief="raised")
    Circular_button10.config(relief="raised")


def rcurv():
    Circular_button1.config(relief="raised")
    Circular_button2.config(relief="raised")
    Circular_button3.config(relief="raised")
    Circular_button4.config(relief="raised")
    Circular_button5.config(relief="raised")
    Circular_button6.config(relief="raised")
    Circular_button7.config(relief="sunken")
    Circular_button8.config(relief="raised")
    Circular_button9.config(relief="raised")
    Circular_button10.config(relief="raised")


def tors():
    Circular_button1.config(relief="raised")
    Circular_button2.config(relief="raised")
    Circular_button3.config(relief="raised")
    Circular_button4.config(relief="raised")
    Circular_button5.config(relief="raised")
    Circular_button6.config(relief="raised")
    Circular_button7.config(relief="raised")
    Circular_button8.config(relief="sunken")
    Circular_button9.config(relief="raised")
    Circular_button10.config(relief="raised")


def rtors():
    Circular_button1.config(relief="raised")
    Circular_button2.config(relief="raised")
    Circular_button3.config(relief="raised")
    Circular_button4.config(relief="raised")
    Circular_button5.config(relief="raised")
    Circular_button6.config(relief="raised")
    Circular_button7.config(relief="raised")
    Circular_button8.config(relief="raised")
    Circular_button9.config(relief="sunken")
    Circular_button10.config(relief="raised")


def larc():
    Circular_button1.config(relief="raised")
    Circular_button2.config(relief="raised")
    Circular_button3.config(relief="raised")
    Circular_button4.config(relief="raised")
    Circular_button5.config(relief="raised")
    Circular_button6.config(relief="raised")
    Circular_button7.config(relief="raised")
    Circular_button8.config(relief="raised")
    Circular_button9.config(relief="raised")
    Circular_button10.config(relief="sunken")


if __name__ == "__main__":
    tog = True
    root = tk.Tk()
    root.wm_title("Física Interactiva")
    frame = tk.Frame(root)
    frame.pack(padx=20, pady=20)
    root.geometry("900x900")
    root.resizable(0, 0)
    dato = tk.StringVar()
    a = tk.StringVar()
    b = tk.StringVar()
    c = tk.StringVar()
    d =tk.StringVar()
    Circular_button1 = tk.Button(master=root, text="Posición", command=lambda:pos(root,a,b))
    Circular_button1.pack()
    Circular_button1.config(relief="sunken")
    Circular_button1.place(x=20, y=170, height=40, width=200)
    Circular_button2 = tk.Button(master=root, text="Velocidad", command=spd)
    Circular_button2.pack()
    Circular_button2.place(x=20, y=220, height=40, width=200)
    Circular_button3 = tk.Button(master=root, text="Velocidad Media", command=spdm)
    Circular_button3.pack()
    Circular_button3.place(x=20, y=270, height=40, width=200)
    Circular_button4 = tk.Button(master=root, text="Aceleración", command=acc)
    Circular_button4.pack()
    Circular_button4.place(x=20, y=320, height=40, width=200)
    Circular_button5 = tk.Button(master=root, text="Aceleración Media", command=accm)
    Circular_button5.pack()
    Circular_button5.place(x=20, y=370, height=40, width=200)
    Circular_button6 = tk.Button(master=root, text="Curvatura", command=curv)
    Circular_button6.pack()
    Circular_button6.place(x=20, y=420, height=40, width=200)
    Circular_button7 = tk.Button(master=root, text="Radio de Curvatura", command=rcurv)
    Circular_button7.pack()
    Circular_button7.place(x=20, y=470, height=40, width=200)
    Circular_button8 = tk.Button(master=root, text="Torsión", command=tors)
    Circular_button8.pack()
    Circular_button8.place(x=20, y=520, height=40, width=200)
    Circular_button9 = tk.Button(master=root, text="Radio de Torsión", command=rtors)
    Circular_button9.pack()
    Circular_button9.place(x=20, y=570, height=40, width=200)
    Circular_button10 = tk.Button(master=root, text="Longitud de Arco", command=larc)
    Circular_button10.pack()
    Circular_button10.place(x=20, y=620, height=40, width=200)
    Circular_button = tk.Button(master=root, text="Atrás", command=root.destroy)
    Circular_button.pack()
    Circular_button.place(x=20, y=10, height=40, width=200)
    titulo_label = tk.Label(master=root, text="Helice Circular", font=("letter case", 50))
    titulo_label.place(x=290, y=70, height=371, width=111)
    titulo_label.pack()
    label2 = tk.Label(master=root, text="R", font=("letter case", 12))
    label2.place(x=440, y=660, height=21, width=21)
    label3 = tk.Label(master=root, text="Ti", font=("letter case", 12))
    label3.place(x=560, y=660, height=21, width=21)

    label4 = tk.Label(master=root, text="Tf", font=("letter case", 12))
    label4.place(x=680, y=660, height=21, width=21)

    label1 = tk.Label(master=root, text="A", font=("letter case", 12))
    label1.place(x=320, y=660, height=21, width=21)
    entry = tk.Entry(master=root, textvariable=a)
    entry.place(x=340, y=660, height=30, width=75)
    entry1 = tk.Entry(master=root, textvariable=b)
    entry1.place(x=460, y=660, height=30, width=75)
    entry2 = tk.Entry(master=root, textvariable=c)
    entry2.place(x=580, y=660, height=30, width=75)
    entry3 = tk.Entry(master=root, textvariable=d)
    entry3.place(x=700, y=660, height=30, width=75)
    entry2.config(state='disable')
    entry3.config(state='disable')
    button_calcp = tk.Button(master=root, text="Calcular",command=lambda:posicion(root,a,b))
    button_calcp.place(y=600, x=450, height=40, width=200)
    on = tk.PhotoImage(file="on.gif")
    off = tk.PhotoImage(file="off.gif")
    t_btn = tk.Label(width=12, image=on)
    t_btn.bind('<Button-1>', toggle)
    t_btn.place(x=840, y=10, height=15, width=27)
    labelk = tk.Label(master=root, text="Animación")
    labelk.place(x=820, y=30)
    posicion_ejemplo(root)
    root.mainloop()