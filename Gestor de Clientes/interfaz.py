from tkinter import *
from tkinter import ttk     # widgets extendidos
import database as db
from tkinter.messagebox import askokcancel, WARNING
import helpers

# CenterWidgetMixin = centra la ventana
class CenterWidgetMixin:
    def center(self):
        self.update()
        w = self.winfo_width()
        h = self.winfo_height()
        ws = self.winfo_screenwidth()
        hs = self.winfo_screenheight()
        x = int(ws/2 - w/2)
        y = int(hs/2 - h/2)
        self.geometry(f"{w}x{h}+{x}+{y}")


# TopLevel = manejo de subventanas / subventana de CREAR CLIENTE
class CreateClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Crear cliente')
        self.build()
        self.center()

        # impide volver a la ventana principal sin interactuar con la nueva
        self.transient(parent)
        self.grab_set()     


    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        Label(frame, text='Nombre (2 a 30 chars)').grid(row=0, column=0)
        Label(frame, text='Apellido (2 a 30 chars)').grid(row=0, column=1)
        Label(frame, text='DNI (8 int)').grid(row=0, column=2)

        nombre = Entry(frame)
        nombre.grid(row=1, column=0)
        nombre.bind('<KeyRelease>', lambda event: self.validate(event, 0))

        apellido = Entry(frame)
        apellido.grid(row=1, column=1)
        apellido.bind('<KeyRelease>', lambda event: self.validate(event, 1))

        dni = Entry(frame)
        dni.grid(row=1, column=2)
        dni.bind('<KeyRelease>', lambda event: self.validate(event, 2))
        
        frame = Frame(self)
        frame.pack(pady=10)

        crear = Button(frame, text='Crear', command=self.create)
        crear.configure(state=DISABLED)
        crear.grid(row=0, column=0)
        Button(frame, text='Cancelar', command=self.close).grid(row=0, column=1)


        self.validaciones = [0, 0, 0]
        self.crear = crear
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni


    def create(self):
        self.master.tabla.insert(
            parent='', index='end', iid=self.dni.get(), 
            values=(self.nombre.get(), self.apellido.get(), self.dni.get()))
        db.Clientes.crear(self.dni.get(), self.nombre.get(), self.apellido.get())
        self.close()


    def close(self):
        self.destroy()
        self.update()
        # metodos internos para cerrar una ventana


    def validate(self, event, index):
        # recuperar el texto ingresado
        valor = event.widget.get()

        # FORMA CORTA
        valido = helpers.dni_valido(valor, db.Clientes.lista) if index == 2 \
            else (len (valor) >= 2 and len(valor) <= 30)
        event.widget.configure({'bg':"lightgreen" if valido else 'Red'})
  
        # estado del botón 'crear'
        self.validaciones[index] = valido
        self.crear.config(state=NORMAL if self.validaciones ==[1, 1, 1] else DISABLED)

                

class EditClientWindow(Toplevel, CenterWidgetMixin):
    def __init__(self, parent):
        super().__init__(parent)
        self.title('Editar cliente')
        self.build()
        self.center()

        # impide volver a la ventana principal sin interactuar con la nueva
        self.transient(parent)
        self.grab_set()     


    def build(self):
        frame = Frame(self)
        frame.pack(padx=20, pady=10)

        Label(frame, text='Nombre (2 a 30 chars)').grid(row=0, column=0)
        Label(frame, text='Apellido (2 a 30 chars)').grid(row=0, column=1)
        Label(frame, text='DNI (no editable)').grid(row=0, column=2)

        nombre = Entry(frame)
        nombre.grid(row=1, column=0)
        nombre.bind('<KeyRelease>', lambda event: self.validate(event, 0))

        apellido = Entry(frame)
        apellido.grid(row=1, column=1)
        apellido.bind('<KeyRelease>', lambda event: self.validate(event, 1))

        dni = Entry(frame)
        dni.grid(row=1, column=2)
        

        cliente = self.master.tabla.focus()
        campos = self.master.tabla.item(cliente, 'values')
        nombre.insert(0, campos[0])
        apellido.insert(0, campos[1])
        dni.insert(0, campos[2])
        dni.config(state=DISABLED)

        frame = Frame(self)
        frame.pack(pady=10)

        actualizar = Button(frame, text='Modificar', command=self.edit_client)
        actualizar.grid(row=0, column=0)
        Button(frame, text='Cancelar', command=self.close).grid(row=0, column=1)

        self.validaciones = [1, 1]
        self.actualizar = actualizar
        self.nombre = nombre
        self.apellido = apellido
        self.dni = dni
    

    def edit_client(self):
        cliente = self.master.tabla.focus()
        self.master.tabla.item(cliente, values=
            (self.nombre.get(), self.apellido.get(), self.dni.get()))
        db.Clientes.modificar(self.dni.get(), self.nombre.get(), self.apellido.get())
        self.close()

    def close(self):
        self.destroy()
        self.update()
        # metodos internos para cerrar una ventana


    def validate(self, event, index):
        # recuperar el texto ingresado
        valor = event.widget.get()

        # FORMA CORTA
        valido = (valor.isalpha() and len (valor) >= 2 and len(valor) <= 30)
        event.widget.configure({'bg':"lightgreen" if valido else 'Red'})

        # estado del botón 'crear'
        self.validaciones[index] = valido
        self.actualizar.config(state=NORMAL if self.validaciones ==[1, 1] else DISABLED)       



class MainWindow(Tk, CenterWidgetMixin):

    def __init__(self):
        super().__init__()
        self.title("Gestor de clientes")
        self.build()
        self.center()

    def build(self):
        frame = Frame(self)
        frame.pack()

        # crear una tabla de excel
        tabla = ttk.Treeview(frame)
        tabla['columns'] = ('Nombre', 'Apellido', 'DNI')

        # eliminar la primera columna automática
        tabla.column('#0', width=0, stretch=NO)
        tabla.column('Nombre', anchor=CENTER)
        tabla.column('Apellido', anchor=CENTER)
        tabla.column('DNI', anchor=CENTER)

        # asignar nombre a las columnas
        tabla.heading("Nombre", text= 'Nombre', anchor=CENTER)
        tabla.heading("Apellido", text= 'Apellido', anchor=CENTER)
        tabla.heading("DNI", text= 'DNI', anchor=CENTER)
        
        # crear una barra de scroll
        scrollbar = Scrollbar(frame)
        scrollbar.pack(side=RIGHT, fill=Y)

        # asignar la barra a la tabla
        tabla['yscrollcommand'] = scrollbar.set

        # cargar los valores a la tabla
        for cliente in db.Clientes.lista:
            tabla.insert(
                parent='', index='end', iid=cliente.dni, 
                values=(cliente.nombre, cliente.apellido, cliente.dni) )

        tabla.pack()

        frame = Frame(self)
        frame.pack(pady=20)

        Button(frame, text="Crear", command=self.create).grid(row=0, column=0)
        Button(frame, text="Modificar", command=self.edit).grid(row=0, column=1)
        Button(frame, text="Borrar", command=self.delete).grid(row=0, column=2)

        self.tabla = tabla


    def delete(self):
        cliente = self.tabla.focus()
        if cliente:
            campos = self.tabla.item(cliente, 'values')
            # guarda dni, nombre y apellido de la persona clickeada (focus)
            
            confirmar = askokcancel(
                title='Confirmar borrado',
                message=f'Borrar a {campos[0]} {campos[1]}?',
                icon = WARNING)
            if confirmar:
                self.tabla.delete(cliente)
                db.Clientes.borrar(campos[2])



    def create(self):
        CreateClientWindow(self)



    def edit(self):
        if self.tabla.focus():
            EditClientWindow(self)



if __name__ == "__main__":
    app = MainWindow()
    app.mainloop()