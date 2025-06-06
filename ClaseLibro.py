# CODIFICACIÓN DE LA CLASE LIBRO-AUTOR: DANIEL SÁNCHEZ 28/05/2025
from ClaseRecurso import * #SE IMPORTA LA CLASE PADRE RECURSO
class Libro (Recurso):
    """
    Esta clase representa un libro  y se encarga de crear el objeto, almacenar la información de éste ingresada
    por el usuario y mostrar dicha información.
    Además, la clase es hija de la clase Recurso, por lo que hereda los atributos y métodos especificados en dicha
    clase.

    ATRIBUTOS (PROPIOS DE ESTA CLASE):
    autor: que almacena el nombre del autor.
    isbn: que almacena el código ISBN del libro.
    editorial_libro: que almacena el nombre de la editorial.
    numero_de_edicion: que almacena el número de la edición.

    """
    
    
    #DECLARACIÓN DE LOS ATRIBUTOS
    autor = str
    isbn = int
    editorial_libro = str
    numero_de_edicion = int
    
    #MÉTODO CONSTRUCTOR DE LA CLASE
    def __init__(self, autor = None, isbn = None, editorial_libro = None, numero_de_edicion = None, num_inventario = None, titulo = None, signatura_topografica = None, coleccion = None):
        #Por medio del método de python super(), se accede al constructor de la clase Recurso
        super().__init__(num_inventario, titulo, signatura_topografica, coleccion) 
        self.autor = autor
        self.isbn = isbn
        self.editorial_libro = editorial_libro
        self.numero_de_edicion = numero_de_edicion
    
    #MÉTODO PARA PEDIR LOS DATOS DEL LIBRO AL USUARIO
    def pedir_datos(self):
        #Por medio del método de python super(), se accede al método pedir_datos() de Recurso
        super().pedir_datos()
        #Posteriormente, se pide la información de los atributos propios de Libro
        self.autor = verificar_si_esta_vacio("Ingrese el nombre del autor: ")
        self.editorial_libro = verificar_si_esta_vacio("Ingrese el nombre de la editorial: ")
        self.numero_de_edicion = leer_entero_no_acotado("Ingrese el número de edición: ")
        self.isbn = verificar_isbn("Ingrese el código ISBN del libro: ")
        
    #MÉTODO PARA MOSTRAR LA INFORMACIÓN DEL LIBRO
    def mostrar_informacion(self):
        super().mostrar_informacion() #Se accede al método mostrar_informacion de la clase Recurso
        print(f"Autor: {self.autor}")
        print(f"Editorial: {self.editorial_libro}")
        print(f"Número de edición: {self.numero_de_edicion}")
        print(f"Código ISBN: {self.isbn}")
