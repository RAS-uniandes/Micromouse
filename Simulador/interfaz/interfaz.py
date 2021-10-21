#27/2/2021
#https://realpython.com/pysimplegui-python/#getting-started-with-pysimplegui
#https://pysimplegui.readthedocs.io/en/latest/#pysimplegui-users-manual
import PySimpleGUI as sg
import os



def layout():
    lay = opciones()
    opcion = sg.Frame('Opciones',lay)
    lay2 = [[]]
    imagen = sg.Output(size=(40,34),key="img",font=('consolas',10))
    #imagen = []
    return [[opcion,sg.VSeperator(),imagen]]


#Codigo obtenido de https://realpython.com/pysimplegui-python/
def opciones():
    x = [[sg.Text("Mapa"),sg.In(size=(25, 1), enable_events=True, key="leyo"),sg.FolderBrowse(),],
     [sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-")],]
    return x

def cargarImagen(ruta):
    if ruta!="":
        archivo = open(ruta, "r")
        frm = ""
        lector = archivo.readline()
        while lector!="":
            frm = frm + lector.replace("-",chr(8213))
            lector = archivo.readline()

        ventana["img"].update([])
        print(frm)


ventana = sg.Window(title="Simulador", layout=layout(), margins=(50, 50), location=(0, 0),
                    resizable=True)
# Loop de ventos
while True:
    event,values = ventana.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "leyo":
        carpeta = values["leyo"]
        try:
            file_list = os.listdir(carpeta)
        except:
            file_list = []
        nomArchivos = [
            i
            for i in file_list
                if os.path.isfile(os.path.join(carpeta, i)) and i.lower().endswith((".txt"))
        ]
        ventana["-FILE LIST-"].update(nomArchivos)
    elif event == "-FILE LIST-":
        try:
            filename = os.path.join(
                values["leyo"], values["-FILE LIST-"][0]
            )
            cargarImagen(filename)
        except:
            pass


