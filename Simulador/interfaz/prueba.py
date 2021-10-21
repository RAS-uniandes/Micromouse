import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

ALTO = 710
ANCHO = 330
def cargar():
   archivo = filedialog.askopenfilename()
   cargarImagen(archivo)

def cargarImagen(ruta):
    if ruta!="":
        archivo = open(ruta, "r")
        frm = ""
        lector = archivo.readline()
        while lector!="":
            frm = frm + lector.replace("-",chr(8213))
            lector = archivo.readline()
        txt.config(state="normal")
        txt.delete("1.0","end")
        txt.insert("end",frm)
        txt.config(state = "disabled")
        print(frm)

top = tk.Tk()
#------------------------------------------------------
#Crear frame y canvas
canvas = tk.Canvas(top, height=ALTO, width=ANCHO)
canvas.pack()
frame1 = tk.Frame(top, bd=5, bg="#ACC5C0")
frame1.place(relwidth=1,relheight=1)
#frame2 = tk.Frame(top, bd=5, bg="blue")
#frame2.place(relwidth=0.5,relheight=1,relx=0.5)
#------------------------------------------------------
#Menu cargar archivo
menu = tk.Menu(top)
menuArchivo = tk.Menu(menu, tearoff=0)
menuArchivo.add_command(label="Cargar", command=cargar)
menu.add_separator()
menuArchivo.add_command(label="Salir",command=top.quit)
menu.add_cascade(label="Archivo",menu=menuArchivo)
top.config(menu=menu)
#------------------------------------------------------
#Caja de texto para mostrar el laberinto
txt = tk.Text(frame1,font="consolas",state="disabled")
txt.tag_configure("whole", spacing1=0)
txt.place(relwidth=1,relheight=0.9,rely=0.1)
top.mainloop()