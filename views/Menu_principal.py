import tkinter as tk
from tkinter.font import BOLD
import util.generic as utl
from views.Busqueda_y_filtrado import BusquedaYFiltrado
from views.Historial_de_eventos_asistidos import HistorialDeEventosAsistidos
from views.Indice_de_eventos import IndiceDeEventos

class MenuPrincipal:
    
    def click_boton_1(self):
        self.ventana.destroy()
        IndiceDeEventos()

    def click_boton_2(self):
        self.ventana.destroy()
        HistorialDeEventosAsistidos()
    
    def click_boton_3(self):
        self.ventana.destroy()
        BusquedaYFiltrado()

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de sesion")
        self.ventana.geometry("800x500")
        self.ventana.config(bg = "#fcfcfc")
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana,800,500)
        
        imagen_fondo = utl.leer_imagen("./assets/imagen_fondo.png",(800,500))

        label_fondo = tk.Label(self.ventana, image=imagen_fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        frame_botones = tk.Frame(self.ventana)
        frame_botones.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        imagen_boton1 = utl.leer_imagen("./assets/HISTORIAL.png",(200,200))

        imagen_boton2 = utl.leer_imagen("./assets/NUEVOS EVENTOS.png",(200,200))

        imagen_boton3 = utl.leer_imagen("./assets/BUSCADOR.png",(200,200))

        label_boton1 = tk.Label(frame_botones, image=imagen_boton1)
        label_boton1.grid(row = 0, column= 0)
        boton1 = tk.Button(frame_botones, text="Indice de eventos", command= self.click_boton_1,bd = 0)
        boton1.grid(row=1, column=0, padx=10)

        label_boton2 = tk.Label(frame_botones, image=imagen_boton2)
        label_boton2.grid(row = 0, column= 1)
        boton2 = tk.Button(frame_botones, text="Historial de eventos", command= self.click_boton_2, bd = 0)
        boton2.grid(row=1, column=1, padx=10)

        label_boton3 = tk.Label(frame_botones, image=imagen_boton3)
        label_boton3.grid(row = 0, column= 2)
        boton3 = tk.Button(frame_botones, text = "Busqueda y filtrado", command= self.click_boton_3, bd = 0)
        boton3.grid(row=1, column=2, padx=10)

        self.ventana.mainloop()

        
