import tkinter as tk
from tkinter import ttk
import util.generic as utl
import json
from tkinter import messagebox

class HistorialDeEventosAsistidos:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Inicio de sesion")
        self.ventana.geometry("1000x00")
        self.ventana.config(bg="#fcfcfc")
        self.ventana.resizable(width=0, height=0)
        utl.centrar_ventana(self.ventana, 800, 600)

        imagen_fondo = utl.leer_imagen("./assets/imagen_fondo.png", (800, 600))

        frame_indice_de_eventos = tk.Frame(self.ventana)
        frame_indice_de_eventos.pack(fill=tk.BOTH, expand=True)

        label_fondo = tk.Label(self.ventana, image=imagen_fondo)
        label_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        frame_indice_de_eventos = tk.Frame(self.ventana, borderwidth=2)
        frame_indice_de_eventos.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

        title = tk.Label(frame_indice_de_eventos, text="Historial de eventos asistidos", font=("Times", 30),
                         fg="#666a88", bg="#fcfcfc", pady=50, justify="left")
        title.pack(fill=tk.X)
        columnas_tabla = ("Id", "Nombre", "Artista", "Genero", "Id_ubicacion", "Hora inicio", "Hora fin", "Descripcion", "Imagen")
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

        with open("./datos/historial.json") as archivo:
            datos = json.load(archivo)
        contador = 0
        for linea in datos:
            tv.insert(parent="", index=contador, iid=contador, text="",
                      values=(linea['id'], linea['nombre'], linea['artista'], linea['genero'],
                              linea['id_ubicacion'], linea['hora_inicio'], linea['hora_fin'],
                              linea['descripcion'], linea['imagen']))
            contador += 1

        btn_atras = tk.Button(
            self.ventana, text="Atrás", font=("Times", 16),  # command=MenuPrincipal()
        )
        btn_atras.pack(side=tk.LEFT, padx=150, pady=70)

        btn_resena = tk.Button(
            self.ventana, text="Reseña", font=("Times", 16), command=self.abrir_ventana_resena
        )
        btn_resena.pack(side=tk.RIGHT, padx=150, pady=70)

        self.ventana.mainloop()

    def abrir_ventana_resena(self):
        VentanaResena()

class VentanaResena(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.title("Registro de Usuarios y Comentarios")
        self.geometry("600x400")

        frame_registro = tk.Frame(self)
        frame_registro.pack(pady=10)

        label_usuario = tk.Label(frame_registro, text="Usuario:")
        label_usuario.grid(row=0, column=0, padx=5, pady=5)
        self.entry_usuario = tk.Entry(frame_registro)
        self.entry_usuario.grid(row=0, column=1, padx=5, pady=5)

        label_comentario = tk.Label(frame_registro, text="Comentario:")
        label_comentario.grid(row=1, column=0, padx=5, pady=5)
        self.entry_comentario = tk.Entry(frame_registro)
        self.entry_comentario.grid(row=1, column=1, padx=5, pady=5)

        boton_guardar = tk.Button(frame_registro, text="Guardar", command=self.guardar_datos)
        boton_guardar.grid(row=2, columnspan=2, padx=5, pady=5)

        frame_mostrar = tk.Frame(self)
        frame_mostrar.pack(pady=10)

        self.tree = ttk.Treeview(frame_mostrar, columns=("Usuario", "Comentario"), show="headings")
        self.tree.heading("Usuario", text="Usuario")
        self.tree.heading("Comentario", text="Comentario")
        self.tree.pack()

        boton_eliminar = tk.Button(frame_mostrar, text="Eliminar", command=self.eliminar_comentario)
        boton_eliminar.pack()

        self.mostrar_datos()

    def guardar_datos(self):
        usuario = self.entry_usuario.get()
        comentario = self.entry_comentario.get()

        if usuario and comentario:
            datos = {"Usuario": usuario, "Comentario": comentario}
            try:
                with open("./datos/resena.json", "r") as file:
                    data = json.load(file)
            except FileNotFoundError:
                data = []

            # Check if data already exists in the file
            if datos in data:
                messagebox.showwarning("Advertencia", "La información ya está registrada en el archivo JSON.")
            else:
                data.append(datos)
                with open("./datos/resena.json", "w") as file:
                    json.dump(data, file, indent=4)  # Add indentation (4 spaces) for each entry
                self.mostrar_datos()
                # Clear entry fields after successful saving
                self.entry_usuario.delete(0, tk.END)
                self.entry_comentario.delete(0, tk.END)

    def eliminar_comentario(self):
        seleccion = self.tree.selection()
        if seleccion:
            with open("./datos/resena.json", "r") as file:
                data = json.load(file)

            for item in seleccion:
                index = int(self.tree.item(item, "text"))
                del data[index]

            with open("./datos/resena.json", "w") as file:
                json.dump(data, file, indent=4)  # Add indentation (4 spaces) for each entry

            self.mostrar_datos()

    def mostrar_datos(self):
        try:
            with open("./datos/resena.json", "r") as file:
                data = json.load(file)
                self.tree.delete(*self.tree.get_children())
                for index, item in enumerate(data):
                    self.tree.insert("", "end", iid=index, text=index, values=(item["Usuario"], item["Comentario"]))
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    app = HistorialDeEventosAsistidos()


