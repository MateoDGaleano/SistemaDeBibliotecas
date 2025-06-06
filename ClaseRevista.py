# CODIFICACIÓN DE LA CLASE REVISTA-AUTOR: DANIEL SÁNCHEZ 28/05/2025
from ClaseRecurso import * #SE IMPORTA LA CLASE PADRE RECURSO
class Revista (Recurso):
    """
    Esta clase representa una revista y se encarga de crear el objeto, almacenar la información de éste ingresada
    por el usuario y mostrar dicha información.
    Además, la clase es hija de la clase Recurso, por lo que hereda los atributos y métodos especificados en dicha
    clase.

    ATRIBUTOS (PROPIOS DE ESTA CLASE):
    issn: que almacena el código ISSN.
    editorial_revista: que almacena el nombre de la editorial.
    volumen: que almacena el número del volumen.
    num_edicion: que almacena el número de la edición.
    anno_publicacion: que almacena el año de publicación.

    """
    
    #ATRIBUTOS PROPIOS DE LA REVISTA
    issn = int
    editorial_revista = str
    volumen = int
    num_edicion = int
    anno_publicacion = int

    #MÉTODO CONSTRUCTOR DE LA CLASE
    def __init__ (self, issn = None, editorial_revista = None, volumen = None, num_edicion = None, anno_publicacion = None, num_inventario = None, titulo = None, signatura_topografica = None, coleccion = None):
        #Por medio del método de python super(), se accede al constructor de la clase Recurso y
        #se asignan los valores de los parametros del constructor de la revista al los de recurso
        super().__init__(num_inventario, titulo, signatura_topografica, coleccion) 
        self.issn = issn
        self.editorial_revista = editorial_revista
        self.volumen = volumen
        self.num_edicion = num_edicion
        self.anno_publicacion = anno_publicacion
    
    #MÉTODO PARA PEDIR LOS DATOS AL USUARIO
    def pedir_datos (self):
        #Por medio del método de python super(), se accede al método pedir_datos() de Recurso
        super().pedir_datos()
        #Posteriormente, se piden los datos propios de la revista al usuario
        self.issn = verificar_issn("Ingrese el código ISSN: ")
        self.anno_publicacion = leer_entero_no_acotado("Ingrese el año de publicación: ")
        self.editorial_revista = verificar_si_esta_vacio("Ingrese el nombre de la editorial: ")
        self.volumen = leer_entero_no_acotado("Ingrese el número del volumen: ")
        self.num_edicion = leer_entero_no_acotado("Ingrese el número de la edición: ")
    
    #MÉTODO PARA MOSTRAR LA INFORMACIÓN DE LA REVISTA
    def mostrar_informacion(self):
        super().mostrar_informacion() #Se accede al método mostrar_informacion de la clase Recurso
        print(f"Código ISSN: {self.issn}")
        print(f"Editorial: {self.editorial_revista}")
        print(f"Volumen: {self.volumen}")
        print(f"Edición: {self.num_edicion}")
        print(f"Año de publicación: {self.anno_publicacion}")

          
