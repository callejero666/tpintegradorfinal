import tkinter as tk
from tkinter import ttk
import util.generic as utl
from tkintermapview import TkinterMapView
import json

class BusquedaYFiltrado:
     
    def actualizar_posicion_en_mapa(self, event):
        selected_item = self.tv.focus()
        if selected_item:
            coordenadas = self.tv.item(selected_item, "values")[-1]
            latitud, longitud = map(float, coordenadas.split(", "))
            self.mapa.set_position(latitud, longitud)

    def filtrar_lista_con_ubicaciones(self,event):
        texto_busqueda = self.filtro_ubicacion.get()
        
        self.tv.delete(*self.tv.get_children())

        with open("./datos/nuevoseventos.json") as archivo:
            datos = json.load(archivo)

        for contador, linea in enumerate(datos):
            if texto_busqueda!="Ninguno":
                if linea['Provincia'] == texto_busqueda:
                    self.tv.insert(parent="", index=contador, iid=contador, text="",
                            values=(linea['Fecha'], linea['Hora'], linea['Artista'],
                                    linea['Genero'], linea['Provincia'], linea['Lugar'],
                                    linea['Direccion'], linea['Ubicacion'], linea['Coordenadas']))
            else:
                self.tv.insert(parent="", index=contador, iid=contador, text="",
                            values=(linea['Fecha'], linea['Hora'], linea['Artista'],
                                    linea['Genero'], linea['Provincia'], linea['Lugar'],
                                    linea['Direccion'], linea['Ubicacion'], linea['Coordenadas']))
    
    def filtrar_lista_con_horas(self,event):
        texto_busqueda = self.filtro_hora.get()
        
        self.tv.delete(*self.tv.get_children())

        with open("./datos/nuevoseventos.json") as archivo:
            datos = json.load(archivo)

        for contador, linea in enumerate(datos):
            if texto_busqueda!="Ninguno":
                if linea['Hora'] == texto_busqueda:
                    self.tv.insert(parent="", index=contador, iid=contador, text="",
                            values=(linea['Fecha'], linea['Hora'], linea['Artista'],
                                    linea['Genero'], linea['Provincia'], linea['Lugar'],
                                    linea['Direccion'], linea['Ubicacion'], linea['Coordenadas']))
            else:
                self.tv.insert(parent="", index=contador, iid=contador, text="",
                            values=(linea['Fecha'], linea['Hora'], linea['Artista'],
                                    linea['Genero'], linea['Provincia'], linea['Lugar'],
                                    linea['Direccion'], linea['Ubicacion'], linea['Coordenadas']))



    def buscar_eventos(self, event):
        texto_busqueda = self.buscador.get()

        self.tv.delete(*self.tv.get_children())

        with open("./datos/nuevoseventos.json") as archivo:
            datos = json.load(archivo)

        for contador, linea in enumerate(datos):
            if texto_busqueda.lower() in json.dumps(linea).lower():
                self.tv.insert(parent="", index=contador, iid=contador, text="",
                          values=(linea['Fecha'], linea['Hora'], linea['Artista'],
                                  linea['Genero'], linea['Provincia'], linea['Lugar'],
                                  linea['Direccion'], linea['Ubicacion'], linea['Coordenadas']))

    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de sesion")
        self.ventana.geometry("1100x700")
        self.ventana.config(bg = "#fcfcfc")
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana,1100,700)
            
        imagen_fondo = utl.leer_imagen("./assets/imagen_fondo.png",(1100,700))

        label_fondo = tk.Label(self.ventana, image=imagen_fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        frame_titulo = tk.Frame(self.ventana, borderwidth=1)
        frame_titulo.pack(side=tk.TOP, pady=10)

        title = tk.Label(frame_titulo, text = "Busqueda y filtrado de eventos", font=("Times", 25), fg="#666a88", bg="#fcfcfc", pady=50, justify="left")
        title.pack(fill=tk.X)

        frame_bucador_y_filtros = tk.Frame(self.ventana, borderwidth=2)
        frame_bucador_y_filtros.pack(side=tk.TOP, pady=10)

        label_buscador = tk.Label(frame_bucador_y_filtros, text="Buscador:")
        label_buscador.pack(side=tk.LEFT, padx=5)

        self.buscador = ttk.Entry(frame_bucador_y_filtros, width=30)
        self.buscador.pack(side=tk.LEFT, padx=5)
        self.buscador.bind("<KeyRelease>", self.buscar_eventos)

        filtro_x_ubicacion = ttk.Label(frame_bucador_y_filtros, text = "Filtrar x ubicacion")
        filtro_x_ubicacion.pack(side = tk.LEFT, padx = 5)
        self.filtro_ubicacion = ttk.Combobox(frame_bucador_y_filtros, state="readonly", values = ["Ninguno",
                                                                                                  "Bs As",
                                                                                                  "Catamarca",
                                                                                                  "Chaco",
                                                                                                  "Chubut",
                                                                                                  "Cordoba",
                                                                                                  "Corrientes",
                                                                                                  "Entre Rios",
                                                                                                  "Formosa",
                                                                                                  "Jujuy",
                                                                                                  "La Pampa",
                                                                                                  "La Rioja",
                                                                                                  "Mendoza",
                                                                                                  "Neuquen",
                                                                                                  "Rio Negro",
                                                                                                  "Salta",
                                                                                                  "San Juan",
                                                                                                  "San Luis",
                                                                                                  "Santa Cruz",
                                                                                                  "Santa Fe",
                                                                                                  "Santiago Del Estero",
                                                                                                  "Tierra Del Fuego",
                                                                                                  "Tucuman"
                                                                                                  ])
        self.filtro_ubicacion.current(0)
        self.filtro_ubicacion.pack(side=tk.LEFT, padx = 5)
        self.filtro_ubicacion.bind("<<ComboboxSelected>>", self.filtrar_lista_con_ubicaciones)

        filtro_x_hora = ttk.Label(frame_bucador_y_filtros, text = "Filtrar por hora")
        filtro_x_hora.pack(side = tk.LEFT, padx = 5)
        self.filtro_hora = ttk.Combobox(frame_bucador_y_filtros, state= "readonly", values =["Ninguno",
                                                                                                  "00:00",
                                                                                                  "01:00",
                                                                                                  "02:00",
                                                                                                  "03:00",
                                                                                                  "04:00",
                                                                                                  "05:00",
                                                                                                  "06:00",
                                                                                                  "07:00",
                                                                                                  "08:00",
                                                                                                  "09:00",
                                                                                                  "10:00",
                                                                                                  "11:00",
                                                                                                  "12:00",
                                                                                                  "13:00",
                                                                                                  "14:00",
                                                                                                  "15:00",
                                                                                                  "16:00",
                                                                                                  "17:00",
                                                                                                  "18:00",
                                                                                                  "19:00",
                                                                                                  "20:00",
                                                                                                  "21:00",
                                                                                                  "22:00",
                                                                                                  "23:00"
                                                                                                  ])
        self.filtro_hora.current(0)
        self.filtro_hora.bind("<<ComboboxSelected>>", self.filtrar_lista_con_horas)
        self.filtro_hora.pack(side = tk.LEFT, padx = 5)

        
        frame_treeview = tk.Frame(self.ventana, borderwidth=2)
        frame_treeview.pack(side=tk.TOP, pady=10)
        
        columnas_tabla = ("Fecha", "Hora", "Artista", "Genero", "Provincia", "Lugar", "Direccion", "Ubicacion", "Coordenadas")
        self.tv = ttk.Treeview(frame_treeview, columns=columnas_tabla, show='headings')
        vsb = ttk.Scrollbar(frame_treeview, orient="vertical", command=self.tv.yview)
        hsb = ttk.Scrollbar(frame_treeview, orient="horizontal", command=self.tv.xview)
        self.tv.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

        vsb.pack(side=tk.RIGHT, fill=tk.Y)
        hsb.pack(side=tk.BOTTOM, fill=tk.X)
        self.tv.pack(fill=tk.BOTH, expand=True)

        frame_treeview.columnconfigure(0, weight=1)
        frame_treeview.rowconfigure(0, weight=1)

        for col in columnas_tabla:
            self.tv.heading(col, text=col)
            self.tv.column(col, stretch=tk.YES, width=80)

        self.tv.pack(fill=tk.BOTH, expand=True)
        
        with open("./datos/nuevoseventos.json") as archivo:
            datos = json.load(archivo)
        contador = 0
        for linea in datos:
            self.tv.insert(parent="", index=contador,   iid=contador, text = "", values=(linea['Fecha'],
                                                                                 linea['Hora'],
                                                                                 linea['Artista'],
                                                                                 linea['Genero'],
                                                                                 linea['Provincia'],
                                                                                 linea['Lugar'],
                                                                                 linea['Direccion'],
                                                                                 linea['Ubicacion'],
                                                                                 linea['Coordenadas']))
            contador+=1
            
        self.tv.bind("<<TreeviewSelect>>", self.actualizar_posicion_en_mapa)

        frame_mapa = tk.Frame(self.ventana)
        frame_mapa.pack(side = tk.BOTTOM,fill=tk.X, expand=True, pady=10)
        
        self.mapa = TkinterMapView(frame_mapa, width=200, height=300, corner_radius=0)
        self.mapa.set_position(-24.77616437851034, -65.41079411004006)
        self.mapa.set_zoom(16)
        self.mapa.pack(fill=tk.BOTH, expand = True)


    
        
   

        self.ventana.mainloop()    

    







