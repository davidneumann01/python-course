class Agenda:

    def __init__(self):
        self.contactos = {} # definimos un diccionario para almacenar los datos
        self.comentario = {}

    
    def menu(self):
        opcion = 0
        try: 
            while opcion != 5:
                print("1- Carga de un contacto en la agenda")
                print("2- Listado completo de la agenda")
                print("3- Consulta ingresando el nombre de la persona")
                print("4- Modificacion del telefono y email")
                print("5- Finalizar programa")
                opcion=int(input("Ingrese su opcion:"))
                if opcion == 1:
                    self.cargar()
                elif opcion == 2:
                    self.listado()
                elif opcion == 3:
                    self.consulta()
                elif opcion == 4:
                    self.modificacion()
        except ValueError: # al ingresar un valor que no sea int
            self.menu()


    def cargar(self):
        nombre=input("Ingrese el nombre de la persona: ")
        telefono=input("Ingrese el numero de telefono: ")
        email=input("Ingrese el email: ")
        datos_extra=input("Ingresa informacion extra(opcional): ")
        self.contactos[nombre] = (telefono,email)
        self.comentario[nombre] = (datos_extra)
        print("______________________________________________")

    
    def listado(self):
        print("______________________________________________")
        nombre=input("Listado completo de la agenda")
        for nombre in self.contactos:
            print(nombre, self.contactos[nombre][0],self.contactos[nombre][1])
        print("______________________________________________")

    
    def consulta(self):
        print("______________________________________________")
        nombre=input("Ingrese el nombre de la persona a consultar: ")
        if nombre in self.contactos:
            print(f"{nombre} su telefono es {self.contactos[nombre][0]} y su email es {self.contactos[nombre][1]}")
            print("_________________Extra_____________________")
            print(f"{self.comentario[nombre]}")
        else:
            print("No existe un contacto con ese nombre")
        print("______________________________________________")

    
    def modificacion(self):
        print("______________________________________________")
        nombre=input("Ingrese el nombre de la persona a modificar el telefono y email: ")
        if nombre in self.contactos:
            telefono=input("Ingrese el nuevo telefono: ")
            email=input("Ingrese el nuevo email: ")
            self.contactos[nombre] = (telefono,email)
        else:
            print("No existe un contacto con ese nombre")
        print("______________________________________________")

# bloque principal

agenda=Agenda()
agenda.menu()
