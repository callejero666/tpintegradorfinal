import tkinter as tk
from tkinter import ttk
import util.generic as utl
import json
class IndiceDeEventos:
    
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de sesion")
        self.ventana.geometry("800x600")
        self.ventana.config(bg = "#fcfcfc")
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana,800,600)
            
        imagen_fondo = utl.leer_imagen("./assets/imagen_fondo.png",(800,600))

        frame_indice_de_eventos = tk.Frame(self.ventana)
        frame_indice_de_eventos.pack(fill=tk.BOTH, expand=True)

        label_fondo = tk.Label(self.ventana, image=imagen_fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        frame_indice_de_eventos = tk.Frame(self.ventana, borderwidth=2)
        frame_indice_de_eventos.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        title = tk.Label(frame_indice_de_eventos, text = "Indice de eventos", font=("Times", 30), fg="#666a88", bg="#fcfcfc", pady=50, justify="left")
        title.pack(fill=tk.X)
        columnas_tabla = ("Fecha", "Hora", "Artista", "Genero", "Provincia", "Lugar", "Direccion", "Ubicacion", "Coordenadas")
        tv = ttk.Treeview(frame_indice_de_eventos, columns=columnas_tabla, show='headings')
        vsb = ttk.Scrollbar(frame_indice_de_eventos, orient="vertical", command=tv.yview)
        hsb = ttk.Scrollbar(frame_indice_de_eventos, orient="horizontal", command=tv.xview)
        tv.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        hsb.pack(side=tk.BOTTOM, fill=tk.X)
        tv.pack(fill=tk.BOTH, expand=True)

        frame_indice_de_eventos.columnconfigure(0, weight=1)
        frame_indice_de_eventos.rowconfigure(0, weight=1)

        for col in columnas_tabla:
            tv.heading(col, text=col)
            tv.column(col, stretch=tk.YES, width=80)

        tv.pack(fill=tk.BOTH, expand=True)
        
        with open("./datos/nuevoseventos.json") as archivo:
            datos = json.load(archivo)
        contador = 0
        for linea in datos:
            tv.insert(parent="", index=contador,   iid=contador, text = "", values=(linea['Fecha'],
                                                                                 linea['Hora'],
                                                                                 linea['Artista'],
                                                                                 linea['Genero'],
                                                                                 linea['Provincia'],
                                                                                 linea['Lugar'],
                                                                                 linea['Direccion'],
                                                                                 linea['Ubicacion'],
                                                                                 linea['Coordenadas']))
            contador+=1
            
        # Crear Botones para volver al menu

        btn_atras = tk.Button(
            self.ventana, text="Atrás", font=("Times", 16)#, command=self.ventana.quit
        )
        btn_atras.pack(side=tk.LEFT, padx=350, pady=70)     


        self.ventana.mainloop()