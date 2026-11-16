from estudiantes import estudiantes
from tkinter import *
from tkinter import messagebox

class App:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Gestion de coches")
        self.ventana.geometry("600x600")
        self.ventana.resizable(0,0) #se puede redimensionar la ventana
        self.main_view()
        

       #VISTAS 
    def borrarpantalla(self):
        for widget in self.ventana.winfo_children():
            widget.destroy()

    def menu_acciones_view(self):
        self.tipo="estudiantes"
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
        Button(self.ventana, text="1.- Estudiantes ",command=self.menu_acciones_view).pack(pady=5)
        Button(self.ventana, text="2.- Salir ",command=self.ventana.quit).pack(pady=5)

    def insertar_view(self):
        self.borrarpantalla()
        Label(self.ventana,text="..Ingresa los datos del estudiante..").pack(pady=10)

        #NOMBRE
        Label(self.ventana,text="Nombre: ").pack(pady=5)
        self.nombre=Entry(self.ventana)
        self.nombre.focus() #hace que entre en la barra
        self.nombre.pack(pady=5)

        #NOTA
        Label(self.ventana,text="Calificacion: ").pack(pady=5)
        self.nota=Entry(self.ventana)
        self.nota.pack(pady=5)

        Button(self.ventana,text="Guardar",command=self.insertar_controller).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones_view).pack(pady=10)     

    def eliminar_view(self):
        self.borrarpantalla()
        Label(self.ventana,text="..Ingresa el ID del estudiante a eliminar..").pack(pady=10)

        #ID
        Label(self.ventana,text="ID: ").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus() 
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
        Label(self.ventana,text="..Ingresa el ID del estudiante a modificar..").pack(pady=10)

        Label(self.ventana,text="ID: ").pack(pady=5)
        self.id=Entry(self.ventana)
        self.id.focus() #hace que entre en la barra 
        self.id.pack(pady=5)

    
        Label(self.ventana,text="Nuevo Nombre: ").pack(pady=5)
        self.nombre=Entry(self.ventana)
        self.nombre.pack(pady=5)

        Label(self.ventana,text="Nueva Nota: ").pack(pady=5)
        self.nota=Entry(self.ventana)
        self.nota.pack(pady=5)        


        #REGRESAR Y GUARDAR
        Button(self.ventana,text="Guardar",command=self.modificar_controller).pack(pady=10)
        Button(self.ventana,text="Regresar",command=self.menu_acciones_view).pack(pady=10)

    def consultar_view(self):
        self.borrarpantalla()
        Label(self.ventana,text="..Consultar los Estudiantes..").pack(pady=10)
        filas=""
        filas=self.consultar_controller(filas)
        Label(self.ventana,text=f"{'No.':<20} {'ID':<20} {'Nombre':<20} {'Nota':<20} \n {'-'*65}").pack(pady=5)
        Label(self.ventana,text=f"{filas}").pack(pady=5)
        Button(self.ventana,text="Regresar", command=self.menu_acciones_view).pack(pady=5)


#---------------------CONTROLADORES-----------------------------

    def insertar_controller(self):
        estudiante1 = estudiantes.Estudiantes(self.nombre.get(), self.nota.get())
        respuesta = estudiante1.insertar()
        self.respuesta_sql (respuesta)
        del estudiante1
        self.insertar_view()


    def buscar_controller(self):
        id = self.id.get()
        registros = estudiantes.Estudiantes.buscar(id)
        if len(registros) > 0:
            estudiante = registros[0]
            self.resultado_busqueda.config(text=f"ID: {estudiante[0]}  Nombre: {estudiante[1]}  Nota: {estudiante[2]}")
            self.btn_eliminar.config(state="normal")
        else:
            self.resultado_busqueda.config(text="... ¡No se encontro un estudiante con ese ID ...!")
            self.btn_eliminar.config(state="disabled")


    def eliminar_controller(self):
        id = self.id.get()
        confirmacion = messagebox.askyesno(title="... Confirmar eliminacion ...", message=f"¿Deseas eliminar el estudiante con ID {id}?")
        if not confirmacion:
            return
        respuesta = estudiantes.Estudiantes.eliminar(id)
        self.respuesta_sql(respuesta)
        self.eliminar_view()


    
    def respuesta_sql(self, respuesta):
        if respuesta:
            messagebox.showinfo(title="...Exitoso...", message="..accion realizada con exito" )
        else:
            messagebox.showerror(title="..verifica por favor..", message="esta accion no pudo realizarse con exito")
        
    def consultar_controller(self,filas):
        registros = estudiantes.Estudiantes.consultar()
        if len(registros) > 0:
            numero_estudiantes = 1
            for fila in registros:
               # filas += f"Estudiante #{numero_estudiantes}\n Id: {fila[0]}\t Nombre: {fila[1]}\t Nota: {fila[2]}\n"

                filas += f"{numero_estudiantes:<20} {fila[0]:<20}\t {fila[1]:<20}\t {fila[2]:<20} \n {'-'*65}\n"
                numero_estudiantes += 1
        else:
            filas = "... ¡No existen datos que mostrar por el momento ...!"
        return filas

    def modificar_controller(self):
        id = self.id.get()
        estudiante1 = estudiantes.Estudiantes(self.nombre.get(), 
                                              self.nota.get())               
        
        respuesta = estudiante1.actualizar(id)
        self.respuesta_sql(respuesta)
        del estudiante1
        self.modificar_view()

if __name__ == "__main__":
    ventana=Tk()
    app = App(ventana)
    ventana.mainloop()

'''
class App:
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        print("\033c")

    def esperarTecla(self):
        input("Oprima tecla ")

    def menu_acciones(self, tipo):
        print(f"\n\t\t\t...::: Menu de {tipo} :::... \n")
        opcion = input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Salir \n\t\t Elige una opcion: ").strip()
        return opcion

    def respuesta_sql(self, respuesta):
        if respuesta:
            input("\n\t Accion Realizada con Exito! \n")
        else:
            input("\n\t Opcion invalida! Oprima cualquier tecla para continuar...  \n")

    def datos_estudiante(self, tipo):
        self.borrarPantalla()
        print(f"\n\t ...Ingresar los datos del {tipo}...")
        estudiantitos = {}
        estudiantitos['nombre'] = input("Nombre: ").upper().strip()
        estudiantitos['nota'] = input("Calificacion: ").strip()
        return estudiantitos

    def menu_estudiantes(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            opcion = self.menu_acciones("Estudiantes")
            match opcion:
                case '1':
                    estudiantitos = self.datos_estudiante("Estudiante")      
                    estudiante1 = estudiantes.Estudiantes(estudiantitos['nombre'], estudiantitos['nota'])
                    respuesta = estudiante1.insertar()
                    self.respuesta_sql(respuesta)
                    del estudiante1

                case "2":
                    self.borrarPantalla()
                    id = input("Ingresa el ID del estudiante a eliminar: ").strip()
                    # Método estático: se llama directamente desde la clase sin instanciar
                    respuesta = estudiantes.Estudiantes.eliminar(id)
                    self.respuesta_sql(respuesta)

                case "3":
                    id = input("Ingresa el ID del estudiante a actualizar: ").strip()
                    estudiantitos = self.datos_estudiante("Estudiante")      
                    estudiante1 = estudiantes.Estudiantes(estudiantitos['nombre'], estudiantitos['nota'])
                    respuesta = estudiante1.actualizar(id)
                    self.respuesta_sql(respuesta)
                    del estudiante1

                case "4":
                    self.borrarPantalla()
                    # Método estático: se llama directamente desde la clase
                    registros = estudiantes.Estudiantes.consultar()
                    if len(registros) > 0:
                        numero_estudiantes = 1
                        for fila in registros:
                            print(f"Estudiante #{numero_estudiantes}\n\t ID: {fila[0]}\n\t nombre: {fila[1]}\n\t calificacion: {fila[2]}\n")
                            numero_estudiantes += 1
                        self.esperarTecla()
                    else:
                        print("\n\n\t ¡No existen datos que mostrar por el momento ...!")
                        self.esperarTecla()

                case "5":
                    opcion = False
                case _:
                    input("\n\t ... Opcion invalida, vuelve a intentarlo por favor ...") 

    def main(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            opcion = input("\n\t\t\t...:: M E N U   P R I N C I P A L ::...\n\n\t 1.- Estudiantes \n\t 2.- Salir \n \t\t Elige una opcion: ").strip().lower()
            match opcion:
                case "1":
                    self.borrarPantalla()
                    self.menu_estudiantes()
                case "2":
                    self.borrarPantalla()
                    input("Saliendo del sistema... ")
                    opcion = False
                case _:
                    input("\n\t ... Opcion invalida, vuelve a intentarlo por favor ... ")

'''
