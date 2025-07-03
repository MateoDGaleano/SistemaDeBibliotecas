# CODIFICACIÓN DE LA CLASE RECURSO-AUTOR: DANIEL SÁNCHEZ 28/05/2025
from funciones_para_verificar import * #SE IMPORTA EL ARCHIVO CON LAS FUNCIONES PARA VERIFICAR ENTRADAS
class Recurso: #CLASE PADRE RECURSO
    """
    Esta clase representa un recurso cualquiera de la biblioteca 
    y se encarga de crear el objeto, almacenar la información de éste ingresada
    por el usuario y mostrar dicha información.
    Además, la clase es una clase Padre, por lo que hereda sus atributos y métodos a
    cada tipo de recurso: Libro, Revista, Audio y Vídeo.

    ATRIBUTOS:
    num_inventario: que almacena el número de inventario del recurso.
    titulo: que almacena el nombre del recurso.
    signatura_topografica: que almacena el código que permite identificar al recurso.
    coleccion: que almacena la colección a la que pertenece (GENERAL, RESERVA, HEMEROTECA).
    estado: que almacena el estado (DISPONIBLE, PRESTADO, PERDIDO, INACTIVO, REPARACION).

    """
    #DECLARACIÓN DE LOS ATRIBUTOS
    num_inventario = int
    titulo = str
    signatura_topografica = str
    coleccion = str
    estado = str
    
    # MÉTODO CONSTRUCTOR DE LA CLASE
    def __init__ (self, num_inventario, titulo, signatura_topografica, coleccion):
        self.num_inventario = num_inventario
        self.titulo = titulo
        self.signatura_topografica = signatura_topografica
        self.coleccion = coleccion
        self.estado = "DISPONIBLE" #Por defecto, el atributo estado se inicializa como disponible

    
    #MÉTODO PARA MOSTRAR LA INFORMACIÓN DEL RECURSO
    def mostrar_informacion(self):
        print("*"*24)
        print("INFORMACIÓN DEL RECURSO:")
        print("*"*24)
        print(f"Número de inventario: {self.num_inventario}")
        print(f"Título: {self.titulo}")
        print(f"Colección: {self.coleccion}")
        print(f"Estado: {self.estado}")
        print(f"Signatura topográfica: {self.signatura_topografica}")

        
    #MÉTODO PARA PEDIR LA INFORMACIÓN DEL RECURSO
    def pedir_datos(self):
        self.num_inventario = leer_entero_no_acotado("Ingrese un número de inventario: ")
        self.titulo = verificar_si_esta_vacio("Ingrese el título del recurso: ")
        self.signatura_topografica = verificar_cadena_alfanumerica("Ingrese la signatura topográfica del recurso: ")
        # Creamos una variable llamada decision para que el usuario seleccione una de las 3 colecciones
        decision = int
        # Se utiliza la función leer_entero para validar que el dato sea ingresado correctamente
        # Se almacena el valor retornado en decision
        decision = leer_entero(1, 3, "Seleccione la colección a la que pertenece el recurso:\n1.GENERAL.\n2.RESERVA.\n3.HEMEROTECA.")
        #Tras ingresar una decisión válida, se verifica el valor almacenado en decision y se asigna al atributo
        #la colección adecuada
        if (decision == 1):
            self.coleccion = "GENERAL"
        elif(decision == 2):
            self.coleccion = "RESERVA"
        elif(decision == 3):
            self.coleccion = "HEMEROTECA"
        
        



