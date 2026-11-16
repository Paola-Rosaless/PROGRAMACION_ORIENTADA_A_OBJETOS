from coches import cochesBD, coches
from tkinter import *
from tkinter import messagebox 

class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestion de coches")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0,0) #si se puede modificar la ventana
        self.main_view()
        

       #VISTAS 
    def borrarpantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def menu_acciones_view(self):
        self.tipo="coches"
        self.borrarpantalla()
        Label(self.ventana,text=f"...::: Menu de {self.tipo} :::... \n")
        Button(self.ventana,text="1.- Agregar",command=self.insertar_view).pack(pady=5)
        Button(self.ventana,text="2.- Borrar",command=self.eliminar_view).pack(pady=5)
        Button(self.ventana,text="3.- Modificar",command=self.modificar_view).pack(pady=5)
        Button(self.ventana,text="4.- Mostrar",command=self.consultar_view).pack(pady=5)
        Button(self.ventana,text="5.- Regresar",command=self.main_view).pack(pady=5)

    def main_view(self):
        self.borrarpantalla()
        Label(self.ventana,text="...:: M E N U   P R I N C I P A L ::...").pack(pady=10)
        Button(self.ventana, text="1.- Coches ",command=self.menu_acciones_view).pack(pady=5)
        Button(self.ventana, text="2.- Salir ",command=self.ventana.quit).pack(pady=5)

    def insertar_view(self):
        self.borrarpantalla()
        Label(self.ventana,text="..Ingresa los datos del coche..").pack(pady=10)

        #MARCA
        Label(self.ventana,text="marca: ").pack(pady=5)
        self.marca=Entry(self.ventana)
        self.marca.focus() #hace que entre en la barra 
        self.marca.pack(pady=5)

        #COLOR
        Label(self.ventana,text="Color: ").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)        

        #MODELO
        Label(self.ventana,text="Modelo: ").pack(pady=5)
        self.modelo=Entry(self.ventana) 
        self.modelo.pack(pady=5)        

        #VELOCIDAD
        Label(self.ventana,text="Velocidad: ").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)        

        #POTENCIA
        Label(self.ventana,text="Potencia: ").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)        

        #ASIENTOS
        Label(self.ventana,text="Asientos: ").pack(pady=5)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)     

        #REGRESAR Y GUARDAR
        Button(self.ventana,text="Guardar",command=self.insertar_controller).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones_view).pack(pady=10)

    def eliminar_view(self):
        self.borrarpantalla()
        Label(self.ventana,text="..Ingresa el ID del coche a eliminar..").pack(pady=10)
        Label(self.ventana,text="ID: ").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus() #hace que entre en la barra 
        self.id.pack(pady=5)

        #RESULTADO DE LA BUSQUEDA
        self.resultado_busqueda=Label(self.ventana,text="")
        self.resultado_busqueda.pack(pady=5)

        #BUSCAR, ELIMINAR Y REGRESAR
        Button(self.ventana,text="Buscar",command=self.buscar_controller).pack(pady=10)
        self.btn_eliminar=Button(self.ventana,text="Eliminar",state="disabled",command=self.eliminar_controller)
        self.btn_eliminar.pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones_view).pack(pady=10)
       
    def modificar_view(self):
        self.borrarpantalla()
        Label(self.ventana,text="..Ingresa el ID del coche a modificar..").pack(pady=10)

        Label(self.ventana,text="ID: ").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus() #hace que entre en la barra 
        self.id.pack(pady=5)

        #MARCA
        Label(self.ventana,text="Nueva Marca: ").pack(pady=5)
        self.marca=Entry(self.ventana)
        self.marca.pack(pady=5)

        #COLOR
        Label(self.ventana,text="Nuevo Color: ").pack(pady=5)
        self.color=Entry(self.ventana)
        self.color.pack(pady=5)        

        #MODELO
        Label(self.ventana,text="Nuevo Modelo: ").pack(pady=5)
        self.modelo=Entry(self.ventana) 
        self.modelo.pack(pady=5)        

        #VELOCIDAD
        Label(self.ventana,text="Nueva Velocidad: ").pack(pady=5)
        self.velocidad=Entry(self.ventana)
        self.velocidad.pack(pady=5)        

        #POTENCIA
        Label(self.ventana,text="Nueva Potencia: ").pack(pady=5)
        self.potencia=Entry(self.ventana)
        self.potencia.pack(pady=5)        

        #ASIENTOS
        Label(self.ventana,text="Nuevos Asientos: ").pack(pady=5)
        self.asientos=Entry(self.ventana)
        self.asientos.pack(pady=5)     

        #REGRESAR Y GUARDAR
        Button(self.ventana,text="Guardar",command=self.modificar_controller).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones_view).pack(pady=10)

    def consultar_view(self):
        self.borrarpantalla()
        Label(self.ventana,text="..Consultar los coches..").pack(pady=10)
        filas=""
        filas=self.consultar_controller(filas)
        #Label(self.ventana,text=f"{filas}").pack(pady=5)
        Label(self.ventana,text=f"{'No.':<4} {'ID':<4} {'Marca':<14} {'Color':<12} {'Modelo':<14} {'Velocidad':<9} {'Potencia':<9} {'Asientos':<8}\n{'-'*81}",font=("Courier New",9)).pack(pady=5)
        Label(self.ventana,text=f"{filas}",font=("Courier New",9)).pack(pady=5)

        Button(self.ventana,text="Regresar", command=self.menu_acciones_view).pack(pady=5)



#CONTROLADOR 

    def insertar_controller(self):
        coche1 = coches.Coches(self.marca.get(), self.color.get(), self.modelo.get(), self.velocidad.get(), self.potencia.get(), self.asientos.get())                    
        coche1 = cochesBD.cochesBD(self.marca.get(), self.color.get(), self.modelo.get(), self.velocidad.get(), self.potencia.get(), self.asientos.get())
        respuesta = coche1.insertar()
        self.respuesta_sql(respuesta)
        del coche1
        self.insertar_view()

  
    def buscar_controller(self):
        id = self.id.get()
        registros = cochesBD.cochesBD.buscar(id)
        if len(registros) > 0:
            coche = registros[0]
            self.resultado_busqueda.config(text=f"ID: {coche[0]}  Marca: {coche[1]}  Color: {coche[2]}  Modelo: {coche[3]}  Velocidad: {coche[4]}  Potencia: {coche[5]}  Asientos: {coche[6]}")
            self.btn_eliminar.config(state="normal")
        else:
            self.resultado_busqueda.config(text="... ¡No se encontro un coche con ese ID ...!")
            self.btn_eliminar.config(state="disabled")

    def eliminar_controller(self):
        id = self.id.get()
        confirmacion = messagebox.askyesno(title="... Confirmar eliminacion ...", message=f"¿Deseas eliminar el coche con ID {id}?")
        if not confirmacion:
            return
        respuesta = cochesBD.cochesBD.eliminar(id)
        self.respuesta_sql(respuesta)
        self.eliminar_view()

    def consultar_controller(self,filas):
        registros = cochesBD.cochesBD.consultar()
        if len(registros) > 0:
            numero_coches = 1
            for fila in registros:
                filas += f"{numero_coches:<4} {str(fila[0])[:4]:<4} {str(fila[1])[:14]:<14} {str(fila[2])[:12]:<12} {str(fila[3])[:14]:<14} {str(fila[4])[:9]:<9} {str(fila[5])[:9]:<9} {str(fila[6])[:8]:<8}\n{'-'*81}\n"
                numero_coches += 1
        else:
            filas = "... ¡No existen datos que mostrar por el momento ...!"
        return filas

    def modificar_controller(self):
        id = self.id.get()
        coche1 = coches.Coches(self.marca.get(), 
                               self.color.get(), 
                               self.modelo.get(), 
                               self.velocidad.get(), 
                               self.potencia.get(),
                               self.asientos.get())            

        coche1 = cochesBD.cochesBD(self.marca.get(),
                                   self.color.get(), 
                                   self.modelo.get(), 
                                   self.velocidad.get(), 
                                   self.potencia.get(), 
                                   self.asientos.get())        
        
        respuesta = coche1.actualizar(id)
        self.respuesta_sql(respuesta)
        del coche1
        self.modificar_view()

    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title="...Exitoso...", message="..accion realizada con exito" )
        else:
            messagebox.showerror(title="..verifica por favor..", message="esta accion no pudo realizarse con exito")

        
if __name__ == "__main__":
    ventana=Tk()
    app = App(ventana)
    ventana.mainloop()

    

