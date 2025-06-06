# CODIFICACIÓN DE LA CLASE VIDEO-AUTOR: DANIEL SÁNCHEZ 28/05/2025
from ClaseRecurso import * #SE IMPORTA LA CLASE PADRE RECURSO
class Video (Recurso):
    """
    Esta clase representa una vídeo y se encarga de crear el objeto, almacenar la información de éste ingresada
    por el usuario y mostrar dicha información.
    Además, la clase es hija de la clase Recurso, por lo que hereda los atributos y métodos especificados en dicha
    clase.

    ATRIBUTOS (PROPIOS DE ESTA CLASE):
    nombre_productor_video: que almacena el nombre del productor.
    nombre_director: que almacena el nombre del director.
    anno_grabacion_video: que almacena el año de grabación.
    genero: que almacena el género del vídeo.

    """
    
    #DECLARACIÓN DE LOS ATRIBUTOS
    nombre_productor_video = str
    nombre_director = str
    anno_grabacion_video = int
    genero = str
    
    #MÉTODO CONSTRUCTOR DE LA CLASE
    def __init__(self, nombre_productor_video = None, nombre_director = None, anno_grabacion_video = None, genero = None, num_inventario = None, titulo = None, signatura_topografica = None, coleccion = None):
        #Por medio del método de python super(), se accede al constructor de la clase Recurso
        super().__init__(num_inventario, titulo, signatura_topografica, coleccion) 
        self.nombre_productor_video = nombre_productor_video
        self.nombre_director = nombre_director
        self.anno_grabacion_video = anno_grabacion_video
        self.genero = genero
    
    #MÉTODO PARA PEDIR LOS DATOS DEL VÍDEO AL USUARIO
    def pedir_datos(self):
        #Por medio del método de python super(), se accede al método pedir_datos() de Recurso
        super().pedir_datos()
        #Posteriormente, se pide la información de los atributos propios de Video
        self.nombre_director = verificar_si_esta_vacio("Ingrese el nombre del director: ")
        self.nombre_productor_video = verificar_si_esta_vacio("Ingrese el nombre del productor: ")
        self.anno_grabacion_video = leer_entero_no_acotado("Ingrese el año de grabación: ")
        #Se crea una variable llamada decision, de tipo entero
        decision = int
        # Se utiliza la función leer_entero para validar que el dato sea ingresado correctamente
        # Se almacena el valor retornado en decision
        decision = leer_entero(1, 4, "Seleccione el género del vídeo:\n1.DOCUMENTAL.\n2.COMEDIA.\n3.TERROR.\n4.ACCIÓN.")
        """Tras ingresar una decisión válida, se verifica el valor almacenado en decision 
        y se asigna el género elegido al atributo genero"""
        if (decision == 1):
            self.genero = "DOCUMENTAL"
        elif (decision == 2):
            self.genero = "COMEDIA"
        elif (decision == 3):
            self.genero = "TERROR"
        elif (decision == 4):
            self.genero = "ACCION"
        
    #MÉTODO PARA MOSTRAR LA INFORMACIÓN DEL VÍDEO
    def mostrar_informacion(self):
        super().mostrar_informacion() #Se accede al método mostrar_informacion de la clase Recurso
        print(f"Director: {self.nombre_director}")
        print(f"Productor: {self.nombre_productor_video}")
        print(f"Género: {self.genero}")
        print(f"Año de grabación: {self.anno_grabacion_video}")