# CODIFICACIÓN DE LA CLASE AUDIO-AUTOR: DANIEL SÁNCHEZ - 28/05/2025
from ClaseRecurso import * #SE IMPORTA LA CLASE PADRE RECURSO
class Audio (Recurso):
    """
    Esta clase representa a un audio  y se encarga de crear el objeto, almacenar la información de éste ingresada
    por el usuario y mostrar dicha información.
    Además, la clase es hija de la clase Recurso, por lo que hereda los atributos y métodos especificados en dicha
    clase.

    ATRIBUTOS (PROPIOS DE ESTA CLASE):
    nombre_cantante: que almacena el nombre del cantante.
    nombre_productor_audio: que almacena el nombre del productor.
    anno_grabacion_audio: que almacena el año de grabación del audio.

    """
    
    #DECLARACIÓN DE LOS ATRIBUTOS
    nombre_cantante = str
    nombre_productor_audio = str
    anno_grabacion_audio = int
    
    #MÉTODO CONSTRUCTOR DE LA CLASE
    def __init__ (self, nombre_cantante = None, nombre_productor_audio = None, anno_grabacion_audio = None, num_inventario = None, titulo = None, signatura_topografica = None, coleccion = None):
        #Por medio del método de python super(), se accede al constructor de la clase Recurso
        super().__init__(num_inventario, titulo, signatura_topografica, coleccion) 
        self.nombre_cantante = nombre_cantante
        self.nombre_productor_audio = nombre_productor_audio
        self.anno_grabacion_audio = anno_grabacion_audio
    
    #MÉTODO PARA PEDIR LOS DATOS AL USUARIO
    def pedir_datos (self):
        #Por medio del método de python super(), se accede al método pedir_datos() de Recurso
        super().pedir_datos()
        #Luego, se piden los datos propios del audio
        self.nombre_cantante = verificar_si_esta_vacio("Ingrese el nombre del cantante: ")
        self.nombre_productor_audio = verificar_si_esta_vacio("Ingrese el nombre del productor: ")
        self.anno_grabacion_audio = leer_entero_no_acotado("Ingrese el año de grabación: ")

    #MÉTODO PARA MOSTRAR LA INFORMACION DEL AUDIO
    def mostrar_informacion(self):
        super().mostrar_informacion() #Se accede al método mostrar_informacion de la clase Recurso
        print(f"Cantante: {self.nombre_cantante}")
        print(f"Productor: {self.nombre_productor_audio}")
        print(f"Año de grabación: {self.anno_grabacion_audio}")
    




    