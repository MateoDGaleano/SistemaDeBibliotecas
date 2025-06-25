#Se importa la librería que permite usar arreglos.
import numpy as np
#Se importan las funciones que permiten verificar datos. 
from funciones_para_verificar import * 
# Se importan las clases de cada recurso de la biblioteca
from ClaseLibro import *
from ClaseAudio import *
from ClaseRecurso import *
from ClaseRevista import *
from ClaseVideo import *
# Se importa la clase usuario
from ClaseUsuario import *
#CLASE BIBLIOTECA (PRINCIPAL)
class Biblioteca:
    """
    Esta clase representa la aplicación principal y se encarga de almacenar usuarios y recursos, 
    así como permitir consultas y modificaciones de la biblioteca de la universidad “Garage-u”

    ATRIBUTOS:
    inventario_de_recursos: que es un arreglo que contiene a los recursos de la biblioteca.
    total_de_usuarios: que es un arreglo que contiene a los usuarios registrados de la biblioteca.
    numero_de_recursos: que es un contador que se encarga de cuantificar los recursos hay almacenados en el arreglo.
    numero_de_usuarios: que es un contador que se encarga de cuantificar los usuarios que hay almacenados.
    total_de_prestamos: que es un arreglo que contiene a los préstamos que se realizan en la biblioteca.
    numero_de_prestamos: que es un contador que se encargará de cuantificar los préstamos que hay en el arreglo.
    usuario_autenticado: qué permite identificar cuál de los usuarios registrados se encuentra usando la aplicación.
    CONSTANTES:
    MAX_USUARIOS: que indica cuál es el número máximo de usuarios que pueden ser almacenados por la aplicación.
    MAX_RECURSOS: que indica cuál es el número máximo de recursos que pueden ser almacenados por la aplicación.
    MAX_PRESTAMOS: que indica cuál es el npumero máximo de préstamos que pueden ser almacenados por la aplicación.
    """

    #DECLARACIÓN DE LOS ATRIBUTOS
    numero_de_recursos = int
    numero_de_usuarios = int
    numero_de_prestamos = int
    inventario_de_recursos = np.ndarray
    total_de_usuarios = np.ndarray
    total_de_prestamos = np.ndarray
    usuario_autenticado = Usuario

    #DECLARACIÓN DE LAS CONSTANTES
    MAX_USUARIOS = 200 #Esta constante indica el número máximo de usuarios que pueden ser almacenados.
    MAX_RECURSOS = 200 #Esta constante indica el número de recursos que pueden ser almacenados.
    MAX_PRESTAMOS = 200 #Esta constante indica el número máximo de usuarios que pueden ser almacenados.

    #MÉTODO CONSTRUCTOR DE LA CLASE
    def __init__ (self, numero_de_recursos = 0, numero_de_usuarios = 0, numero_de_prestamos = 0  ):
        #Cuando se crea el objeto de la clase, los valores por defecto de ambos contadores es cero.
        self.numero_de_recursos = numero_de_recursos
        self.numero_de_usuarios = numero_de_usuarios
        self.numero_de_prestamos = numero_de_prestamos
        #Se inicializan los arreglos de objetos de tipos recurso, usuario y préstamo con el valor None por defecto
        self.inventario_de_recursos = np.full((self.MAX_RECURSOS), fill_value = None, dtype = object)
        self.total_de_usuarios = np.full((self.MAX_USUARIOS), fill_value = None, dtype = object)
        self.total_de_prestamos = np.full((self.MAX_PRESTAMOS), fill_value = None, dtype = object)

        #SE CREA UN PRIMER USUARIO ADMINISTRADOR
        self.total_de_usuarios[0] = Usuario(nombre_usuario="Mateo", direccion_residencia="Medellin", telefono=300600200, email="m@gmail.com", codigo="m1811", id=101)
        self.total_de_usuarios[0].tipo_de_usuario = Usuario.PERFIL_ADMIN

        #SE CREA UN PRIMER USUARIO BIBLIOTECARIO
        self.total_de_usuarios[1] = Usuario(nombre_usuario="Daniel", direccion_residencia="Medellin", telefono=300700300, email="d@gmail.com", codigo="d123", id=102)
        self.total_de_usuarios[1].tipo_de_usuario = Usuario.PERFIL_BIBLIOTECARIO
        
        self.numero_de_usuarios = 2

        #SE INICIALIZA EL ATRIBUTO QUE PERMITE IDENTIFICAR EL USUARIO QUE SE ENCUENTRA AUTENTICADO
        self.usuario_autenticado = None #Al principio no hay usuarios autenticados


    def registrar_recurso (self):
        """
        Este método crea y agrega un recurso al arreglo de recursos
        por lo que da solución al requerimiento 1 del análisis del problema

        PARÁMETEROS:
        Ninguno

        RETORNO:
        Vacio

        Autor: Daniel Sánchez 29/05/2025
        """
        # Se verifica que el total de recursos en el arreglo no sobrepase su capacidad máxima
        if (self.numero_de_recursos < self.MAX_RECURSOS):
            """Se declara una variable entera llamada decision y se pide al usuario que ingrese qué tipo
            de recurso desea ingresar"""
            decision = int
            decision = leer_entero(1, 4, "Seleccione el tipo de recurso que desea registrar:\n1.Libro.\n2.Audio.\n3.Vídeo.\n4.Revista.")
            
            """Se crea una variable llamada no_hay_coincidencia y se inicializa en True, esto
            permite que en caso de que un recurso ya registrado tenga una signatura topográfica igual
            a la de un recurso en proceso de registro, no se permita registrar ese nuevo recurso"""
            no_hay_coincidencia = bool
            no_hay_coincidencia = True
            
            #Se verifica el valor almacenado en decision, de acuerdo a este, se crea el tipo de recurso y se piden sus datos
            if (decision == 1):
                objeto = Libro()
                objeto.pedir_datos()
            elif (decision == 2):
                objeto = Audio()
                objeto.pedir_datos()
            elif (decision == 3):
                objeto = Video()
                objeto.pedir_datos()
            elif (decision == 4):
                objeto = Revista()
                objeto.pedir_datos()

            """Una vez creado el recurso, el ciclo recorre todo el arreglo,
            y en aquellas casillas con valores diferentes a None, compara si la signatura
            topográfica del objeto almacenado coincide con la del nuevo objeto""" 
            for i in range(len(self.inventario_de_recursos)):
                if (self.inventario_de_recursos[i] != None):
                    if (self.inventario_de_recursos[i].signatura_topografica == objeto.signatura_topografica):
                        print("La signatura ingresada coincide con la de un recurso ya registrado. El recurso no será almacenado.")
                        no_hay_coincidencia = False # Si hay una coincicencia, se hace falsa la variable
            
            #En caso de que el ciclo termine sin encontrar coincidencias, la variable no_hay_coincidencia es True
            #Luego, se agrega el nuevo objeto al arreglo y se aumenta el contador de recursos en 1
            if (no_hay_coincidencia):
                self.inventario_de_recursos[self.numero_de_recursos] = objeto
                print("Recurso registrado exitosamente.")
                self.numero_de_recursos += 1
        else:
            print("No hay espacio para almacenar un nuevo recurso en este momento.")

        input("Presione Enter para continuar...")
    
    
    def registrar_usuario (self):
        """
        Este método crea y agrega un usuario al arreglo de usuarios
        Por lo que da solución al requerimiento 2 del análisis del problema

        PARÁMETEROS:
        Ninguno

        RETORNO:
        Vacio

        Autor: Daniel Sánchez 29/05/2025
        """ 
        #Se verifica que el total de usuarios en el arreglo no sobrepase la capacidad máxima
        if (self.numero_de_usuarios < self.MAX_USUARIOS):
            #Se crea un objeto auxiliar de tipo usuario
            objeto = Usuario()
            #Se piden los datos básicos del usuario
            objeto.pedir_datos()
            """Se declara una variable bandera que permita identificar si hay coincidencias entre el código
            del usuario con el código de otro usuario existente"""
            no_hay_coincidencia = bool
            no_hay_coincidencia = True
            #Se crea una variable controladora del ciclo
            i = int
            #Un ciclo recorre el arreglo total_de_usuarios para verificar que no haya otro con su mismo código o identificación
            for i in range (len(self.total_de_usuarios)):
                if (self.total_de_usuarios[i] != None):
                    if (self.total_de_usuarios[i].codigo == objeto.codigo and self.total_de_usuarios[i].id == objeto.id):
                        print("La identificación y código de usuario ingresados ya existen. No es posible realizar el registro.")
                        no_hay_coincidencia = False
                    elif (self.total_de_usuarios[i].codigo == objeto.codigo):
                        print("El código de usuario ya existe. No es posible realizar el registro.")
                        no_hay_coincidencia = False
                    elif (self.total_de_usuarios[i].id == objeto.id):
                        print("El número de identificación ingresado ya existe. No es posible realizar el registro.")
                        no_hay_coincidencia = False

            #En caso de que el ciclo termine sin encontrar coincidencias, la variable no_hay_coincidencia es True
            #Luego, se agrega el nuevo objeto al arreglo y se aumenta el contador de recursos en 1
            if (no_hay_coincidencia):
                self.total_de_usuarios[self.numero_de_usuarios] = objeto
                print("Usuario registrado exitosamente.")
                self.numero_de_usuarios += 1
        else:
            print("No hay espacio para almacenar un nuevo usuario en este momento.")

        input("Presione Enter para continuar...")


    def modificar_info_recurso(self):
        """
        Este método modifica un recurso del inventario de recursos
        Por lo que da solución al requerimiento 3 del análisis del problema.

        PARÁMETEROS:
        Ninguno

        RETORNO:
        Vacio

        Autor: Mateo Galeano 31/05/2025
        """ 
        signatura_para_busqueda = str
        coincidencia = bool
        recurso = str
        coincidencia = False
        num_del_recurso = int
        contador_i = int
        contador_i = 0
        decision = int
        continuar = int
        signatura_igual = bool
        signatura_nueva = str
        continuar = int
        seleccion = int
        print("\n*************************************\nModificar recurso\n*************************************")
        
        """Se almacena la signatura topográfica 
        que se va a usar para buscar un recurso en específico"""
        
        signatura_para_busqueda = verificar_cadena_alfanumerica("Ingrese la signatura topográfica del recurso que desea editar: ")

        #Se busca en el arreglo "inventario_de_recursos" si hay un recurso con signatura igual a "signatura_para_busqueda"
        for contador_i in range(len(self.inventario_de_recursos)):
            recurso = self.inventario_de_recursos[contador_i] #Se crea una variable "recurso" para facilitar el manejo del código
            #Se verifica si la posición del arreglo almacena el valor None, si es así, no se ejecuta el bloque de código
            if recurso != None:
                """Si la posición del arreglo tiene un valor distinto a None, se compara la signatura_topográfica con
                La ingresada para la búsqueda"""
                if recurso.signatura_topografica == signatura_para_busqueda:
                    recurso.mostrar_informacion() #Se muestra la información del recurso
                    coincidencia = True #Se asigna el valor True a la variable coincidencia
                    num_del_recurso = contador_i #Se guarda la posición del recurso encontrado en la variable "num_del_recurso"

        #Si no se encontro ningún recurso con igual signatura topográfica, mostrar un mensaje que indique que no hubo ninguna coincidencia
        if coincidencia == False:
            print("No se encontró ninguna coincidencia. Se le llevará de vuelta al menú principal.")

        #Si se encuentra una coincidencia entonces
        while coincidencia:
            #Desplegar un menú de opciones al usuario para que escoja qué atributo del recurso desea modificar
            print("\n*************************************\nSístema de bibliotecas\nMenú de opciones (Modificar recurso)\n*************************************")
            print("Seleccione el dato del recurso que desea modificar:")
            print("1.Número de inventario.")
            print("2.Título.")
            print("3.Signatura topográfica.")
            print("4.Colección.")
            print("5.Estado.")
            #Dependiendo de la clase a la que pertenezca el recurso, se muestra uno de los menús de opciones
            #La función isinstance permite verificar fácilmente a qué clase pertenece el objeto
            if (isinstance(self.inventario_de_recursos[num_del_recurso], Libro)):
                print("6.Nombre del autor.")
                print("7.ISBN.")
                print("8.Nombre de la editorial.")
                print("9.Número de edición.")
                decision = leer_entero(1, 9, "Seleccione una opción: ")
            elif (isinstance(self.inventario_de_recursos[num_del_recurso], Audio)):
                print("6.Nombre del cantante.")
                print("7.Nombre del productor.")
                print("8.Año de grabación.")
                decision = leer_entero(1, 8, "Seleccione una opción: ")
            elif (isinstance(self.inventario_de_recursos[num_del_recurso], Video)):
                print("6.Nombre del productor.")
                print("7.Nombre del director.")
                print("8.Año de grabación.")
                print("9.Género.")
                decision = leer_entero(1, 9, "Seleccione una opción: ")
            elif (isinstance(self.inventario_de_recursos[num_del_recurso], Revista)):
                print("6.ISSN.")
                print("7.Nombre de la editorial.")
                print("8.Volumen.")
                print("9.Número de edición.")
                print("10.Año de publicación.")
                decision = leer_entero(1, 10, "Seleccione una opción: ")

            #Dependiendo del valor almacenado en decision y de la clase del objeto, se procede a realizar la modificación del atributo
            if (isinstance(self.inventario_de_recursos[num_del_recurso], Libro)):
                
                match (decision):
                    #Para modificar el número de inventario del recurso
                    case 1:
                        self.inventario_de_recursos[num_del_recurso].num_inventario = leer_entero_no_acotado("Ingrese un nuevo número de inventario: ")

                    #Para modificar el titulo del recurso
                    case 2:
                        self.inventario_de_recursos[num_del_recurso].titulo = verificar_si_esta_vacio("Ingrese el nuevo titulo: ")

                    #Para modificar la signatura topográfica del recurso:
                    case 3:
                        while True:
                            #Variable booleana para verificar si la signatura que se va a ingresar es igual a alguna previamente ingresada
                            signatura_igual = False 
                            signatura_nueva = verificar_cadena_alfanumerica("Ingrese nueva signatura topográfica: ")
                            """
                            Se recorre el arreglo "inventario_de_recursos" verificando que la signatura topográfica 
                            ingresada no coincida con alguna ya asignada
                            """
                            for contador_i in range(len(self.inventario_de_recursos)):
                                recurso = self.inventario_de_recursos[contador_i] #Se crea una variable "recurso" para facilitar el manejo del código
                                #Se verifica si la posición del arreglo almacena el valor None, si es así, no se ejecuta el bloque de código
                                if recurso != None:
                                    if recurso.signatura_topografica == signatura_nueva:
                                        print("Error, esta signatura topográfica ya está en uso. Por favor, intente de nuevo.")
                                        signatura_igual = True #Se asigna el valor True a la variable, indicando que se encontro una signatura igual en el arreglo
                            #Si no se encuentra una signatura igual, asignar al recurso la nueva signatura topográfica
                            if signatura_igual == False:
                                self.inventario_de_recursos[num_del_recurso].signatura_topografica = signatura_nueva
                                break
                            
                    #Para modificar la colección del recurso
                    case 4:
                        #Esta variable nos ayuda a elegir una opción
                        seleccion = leer_entero(1, 3, "Asigne una nueva coleccion:\n1.RESERVA.\n2.GENERAL.\n3.HEMEROTECA.")
                        if seleccion == 1:
                            self.inventario_de_recursos[num_del_recurso].coleccion = "RESERVA"
                        elif seleccion == 2:
                            self.inventario_de_recursos[num_del_recurso].coleccion = "GENERAL"
                        elif seleccion == 3:
                            self.inventario_de_recursos[num_del_recurso].coleccion = "HEMEROTECA"

                    #Para modificar el estado del recurso
                    case 5:
                        #Esta variable nos ayuda a elegir una opción
                        seleccion = leer_entero(1, 5, "Asigne un nuevo estado\n1.PRESTADO.\n2.DISPONIBLE.\n3.REPARACIÓN.\n4.INACTIVO.\n5.PERDIDO.")
                        if seleccion == 1:
                            self.inventario_de_recursos[num_del_recurso].estado = "PRESTADO"
                        elif seleccion == 2:
                            self.inventario_de_recursos[num_del_recurso].estado = "DISPONIBLE"
                        elif seleccion == 3:
                            self.inventario_de_recursos[num_del_recurso].estado = "REPARACIÓN"
                        elif seleccion == 4:
                            self.inventario_de_recursos[num_del_recurso].estado = "INACTIVO"
                        elif seleccion == 5:
                            self.inventario_de_recursos[num_del_recurso].estado = "PERDIDO"
                    
                    #Para modificar el autor
                    case 6:
                        self.inventario_de_recursos[num_del_recurso].autor = verificar_si_esta_vacio("Ingrese el nuevo nombre del autor: ")
                    
                    #Para modificar el isbn
                    case 7:
                        self.inventario_de_recursos[num_del_recurso].isbn = verificar_isbn("Ingrese el nuevo número de ISBN: ")
                    
                    #Para modificar el nombre de la editorial
                    case 8:
                        self.inventario_de_recursos[num_del_recurso].editorial_libro = verificar_si_esta_vacio("Ingrese el nuevo nombre de la editorial: ")
                    
                    #Para modificar el número de la edición
                    case 9:
                        self.inventario_de_recursos[num_del_recurso].numero_de_edicion = leer_entero_no_acotado("Ingrese el nuevo número de edicición: ")           
            elif (isinstance(self.inventario_de_recursos[num_del_recurso], Audio)):
                match (decision):
                    #Para modificar el número de inventario del recurso
                    case 1:
                        self.inventario_de_recursos[num_del_recurso].num_inventario = leer_entero_no_acotado("Ingrese un nuevo número de inventario: ")

                    #Para modificar el titulo del recurso
                    case 2:
                        self.inventario_de_recursos[num_del_recurso].titulo = verificar_si_esta_vacio("Ingrese el nuevo titulo: ")

                    #Para modificar la signatura topográfica del recurso:
                    case 3:
                        while True:
                            #Variable booleana para verificar si la signatura que se va a ingresar es igual a alguna previamente ingresada
                            signatura_igual = False 
                            signatura_nueva = verificar_cadena_alfanumerica("Ingrese nueva signatura topográfica: ")
                            """
                            Se recorre el arreglo "inventario_de_recursos" verificando que la signatura topográfica 
                            ingresada no coincida con alguna ya asignada
                            """
                            for contador_i in range(len(self.inventario_de_recursos)):
                                recurso = self.inventario_de_recursos[contador_i] #Se crea una variable "recurso" para facilitar el manejo del código
                                #Se verifica si la posición del arreglo almacena el valor None, si es así, no se ejecuta el bloque de código
                                if recurso != None:
                                    if recurso.signatura_topografica == signatura_nueva:
                                        print("Error, esta signatura topográfica ya está en uso. Por favor, intente de nuevo.")
                                        signatura_igual = True #Se asigna el valor True a la variable, indicando que se encontro una signatura igual en el arreglo
                            #Si no se encuentra una signatura igual, asignar al recurso la nueva signatura topográfica
                            if signatura_igual == False:
                                self.inventario_de_recursos[num_del_recurso].signatura_topografica = signatura_nueva
                                break
                            

                    #Para modificar la colección del recurso
                    case 4:
                        #Esta variable nos ayuda a elegir una opción
                        seleccion = leer_entero(1, 3, "Asigne una nueva coleccion:\n1.RESERVA.\n2.GENERAL.\n3.HEMEROTECA.")
                        if seleccion == 1:
                            self.inventario_de_recursos[num_del_recurso].coleccion = "RESERVA"
                        elif seleccion == 2:
                            self.inventario_de_recursos[num_del_recurso].coleccion = "GENERAL"
                        elif seleccion == 3:
                            self.inventario_de_recursos[num_del_recurso].coleccion = "HEMEROTECA"

                    #Para modificar el estado del recurso
                    case 5:
                        #Esta variable nos ayuda a elegir una opción
                        seleccion = leer_entero(1, 5, "Asigne un nuevo estado\n1.PRESTADO.\n2.DISPONIBLE.\n3.REPARACIÓN.\n4.INACTIVO.\n5.PERDIDO.")
                        if seleccion == 1:
                            self.inventario_de_recursos[num_del_recurso].estado = "PRESTADO"
                        elif seleccion == 2:
                            self.inventario_de_recursos[num_del_recurso].estado = "DISPONIBLE"
                        elif seleccion == 3:
                            self.inventario_de_recursos[num_del_recurso].estado = "REPARACIÓN"
                        elif seleccion == 4:
                            self.inventario_de_recursos[num_del_recurso].estado = "INACTIVO"
                        elif seleccion == 5:
                            self.inventario_de_recursos[num_del_recurso].estado = "PERDIDO"
                    
                    #Para modificar el nombre del cantante
                    case 6:
                        self.inventario_de_recursos[num_del_recurso].nombre_cantante = verificar_si_esta_vacio("Ingrese el nuevo nombre del cantante: ")
                    
                    #Para modificar el nombre del productor
                    case 7:
                        self.inventario_de_recursos[num_del_recurso].nombre_productor_audio = verificar_si_esta_vacio("Ingrese el nuevo nombre del productor: ")
                    
                    #Para modificar el año de grabación
                    case 8:
                        self.inventario_de_recursos[num_del_recurso].anno_grabacion_audio = leer_entero_no_acotado("Ingrese el nuevo año de grabación: ")
            elif(isinstance(self.inventario_de_recursos[num_del_recurso], Video)):
                match (decision):
                    #Para modificar el número de inventario del recurso
                    case 1:
                        self.inventario_de_recursos[num_del_recurso].num_inventario = leer_entero_no_acotado("Ingrese un nuevo número de inventario: ")

                    #Para modificar el titulo del recurso
                    case 2:
                        self.inventario_de_recursos[num_del_recurso].titulo = verificar_si_esta_vacio("Ingrese el nuevo titulo: ")

                    #Para modificar la signatura topográfica del recurso:
                    case 3:
                        while True:
                            #Variable booleana para verificar si la signatura que se va a ingresar es igual a alguna previamente ingresada
                            signatura_igual = False 
                            signatura_nueva = verificar_cadena_alfanumerica("Ingrese nueva signatura topográfica: ")
                            """
                            Se recorre el arreglo "inventario_de_recursos" verificando que la signatura topográfica 
                            ingresada no coincida con alguna ya asignada
                            """
                            for contador_i in range(len(self.inventario_de_recursos)):
                                recurso = self.inventario_de_recursos[contador_i] #Se crea una variable "recurso" para facilitar el manejo del código
                                #Se verifica si la posición del arreglo almacena el valor None, si es así, no se ejecuta el bloque de código
                                if recurso != None:
                                    if recurso.signatura_topografica == signatura_nueva:
                                        print("Error, esta signatura topográfica ya está en uso. Por favor, intente de nuevo.")
                                        signatura_igual = True #Se asigna el valor True a la variable, indicando que se encontro una signatura igual en el arreglo
                            #Si no se encuentra una signatura igual, asignar al recurso la nueva signatura topográfica
                            if signatura_igual == False:
                                self.inventario_de_recursos[num_del_recurso].signatura_topografica = signatura_nueva
                                break
                            

                    #Para modificar la colección del recurso
                    case 4:
                        #Esta variable nos ayuda a elegir una opción
                        seleccion = leer_entero(1, 3, "Asigne una nueva coleccion:\n1.RESERVA.\n2.GENERAL.\n3.HEMEROTECA.")
                        if seleccion == 1:
                            self.inventario_de_recursos[num_del_recurso].coleccion = "RESERVA"
                        elif seleccion == 2:
                            self.inventario_de_recursos[num_del_recurso].coleccion = "GENERAL"
                        elif seleccion == 3:
                            self.inventario_de_recursos[num_del_recurso].coleccion = "HEMEROTECA"

                    #Para modificar el estado del recurso
                    case 5:
                        #Esta variable nos ayuda a elegir una opción
                        seleccion = leer_entero(1, 5, "Asigne un nuevo estado\n1.PRESTADO.\n2.DISPONIBLE.\n3.REPARACIÓN.\n4.INACTIVO.\n5.PERDIDO.")
                        if seleccion == 1:
                            self.inventario_de_recursos[num_del_recurso].estado = "PRESTADO"
                        elif seleccion == 2:
                            self.inventario_de_recursos[num_del_recurso].estado = "DISPONIBLE"
                        elif seleccion == 3:
                            self.inventario_de_recursos[num_del_recurso].estado = "REPARACIÓN"
                        elif seleccion == 4:
                            self.inventario_de_recursos[num_del_recurso].estado = "INACTIVO"
                        elif seleccion == 5:
                            self.inventario_de_recursos[num_del_recurso].estado = "PERDIDO"
                    
                    #Para modificar el nombre del productor
                    case 6:
                        self.inventario_de_recursos[num_del_recurso].nombre_productor_video = verificar_si_esta_vacio("Ingrese el nuevo nombre del productor: ")
                    
                    #Para modificar el nombre del director
                    case 7:
                        self.inventario_de_recursos[num_del_recurso].nombre_director = verificar_si_esta_vacio("Ingrese el nuevo nombre del director: ")
                    
                    #Para modificar el año de grabación
                    case 8:
                        self.inventario_de_recursos[num_del_recurso].anno_grabacion_video = leer_entero_no_acotado("Ingrese el nuevo año de grabación: ")
                    
                    #Para modificar el género
                    case 9:
                        #Esta variable nos ayuda a elegir una opción
                        seleccion = leer_entero(1, 4, "Asigne un nuevo género:\n1.DOCUMENTAL.\n2.COMEDIA.\n3.TERROR.\n4.ACCIÓN.")
                        if (seleccion == 1):
                            self.inventario_de_recursos[num_del_recurso].genero = "DOCUMENTAL"
                        elif (seleccion == 2):
                            self.inventario_de_recursos[num_del_recurso].genero = "COMEDIA"
                        elif (seleccion == 3):
                            self.inventario_de_recursos[num_del_recurso].genero = "TERROR"
                        elif (seleccion == 4):
                            self.inventario_de_recursos[num_del_recurso].genero = "ACCION"
            elif (isinstance(self.inventario_de_recursos[num_del_recurso], Revista)):
                match (decision):
                    #Para modificar el número de inventario del recurso
                    case 1:
                        self.inventario_de_recursos[num_del_recurso].num_inventario = leer_entero_no_acotado("Ingrese un nuevo número de inventario: ")

                    #Para modificar el titulo del recurso
                    case 2:
                        self.inventario_de_recursos[num_del_recurso].titulo = verificar_si_esta_vacio("Ingrese el nuevo titulo: ")

                    #Para modificar la signatura topográfica del recurso:
                    case 3:
                        while True:
                            #Variable booleana para verificar si la signatura que se va a ingresar es igual a alguna previamente ingresada
                            signatura_igual = False 
                            signatura_nueva = verificar_cadena_alfanumerica("Ingrese nueva signatura topográfica: ")
                            """
                            Se recorre el arreglo "inventario_de_recursos" verificando que la signatura topográfica 
                            ingresada no coincida con alguna ya asignada
                            """
                            for contador_i in range(len(self.inventario_de_recursos)):
                                recurso = self.inventario_de_recursos[contador_i] #Se crea una variable "recurso" para facilitar el manejo del código
                                #Se verifica si la posición del arreglo almacena el valor None, si es así, no se ejecuta el bloque de código
                                if recurso != None:
                                    if recurso.signatura_topografica == signatura_nueva:
                                        print("Error, esta signatura topográfica ya está en uso. Por favor, intente de nuevo.")
                                        signatura_igual = True #Se asigna el valor True a la variable, indicando que se encontro una signatura igual en el arreglo
                            #Si no se encuentra una signatura igual, asignar al recurso la nueva signatura topográfica
                            if signatura_igual == False:
                                self.inventario_de_recursos[num_del_recurso].signatura_topografica = signatura_nueva
                                break
                            

                    #Para modificar la colección del recurso
                    case 4:
                        #Esta variable nos ayuda a elegir una opción
                        seleccion = leer_entero(1, 3, "Asigne una nueva coleccion:\n1.RESERVA.\n2.GENERAL.\n3.HEMEROTECA.")
                        if seleccion == 1:
                            self.inventario_de_recursos[num_del_recurso].coleccion = "RESERVA"
                        elif seleccion == 2:
                            self.inventario_de_recursos[num_del_recurso].coleccion = "GENERAL"
                        elif seleccion == 3:
                            self.inventario_de_recursos[num_del_recurso].coleccion = "HEMEROTECA"

                    #Para modificar el estado del recurso
                    case 5:
                        #Esta variable nos ayuda a elegir una opción
                        seleccion = leer_entero(1, 5, "Asigne un nuevo estado\n1.PRESTADO.\n2.DISPONIBLE.\n3.REPARACIÓN.\n4.INACTIVO.\n5.PERDIDO.")
                        if seleccion == 1:
                            self.inventario_de_recursos[num_del_recurso].estado = "PRESTADO"
                        elif seleccion == 2:
                            self.inventario_de_recursos[num_del_recurso].estado = "DISPONIBLE"
                        elif seleccion == 3:
                            self.inventario_de_recursos[num_del_recurso].estado = "REPARACIÓN"
                        elif seleccion == 4:
                            self.inventario_de_recursos[num_del_recurso].estado = "INACTIVO"
                        elif seleccion == 5:
                            self.inventario_de_recursos[num_del_recurso].estado = "PERDIDO"
                    
                    #Para modificar el ISSN
                    case 6:
                        self.inventario_de_recursos[num_del_recurso].issn = verificar_issn("Ingrese el nuevo código ISSN: ")
                    
                    #Para modificar el nombre de la editorial
                    case 7:
                        self.inventario_de_recursos[num_del_recurso].editorial_revista = verificar_si_esta_vacio("Ingrese el nuevo nombre de la editorial: ")

                    #Para modificar el volumen
                    case 8:
                        self.inventario_de_recursos[num_del_recurso].volumen = leer_entero_no_acotado("Ingrese el nuevo número del volumen: ")
                    
                    #Para modificar el número de edición
                    case 9:
                        self.inventario_de_recursos[num_del_recurso].num_edicion = leer_entero_no_acotado("Ingrese el nuevo número de edición: ")
                    
                    #Para modificar el año de publicación
                    case 10:
                        self.inventario_de_recursos[num_del_recurso].anno_publicacion = leer_entero_no_acotado("Ingrese el nuevo año de publicación: ")

                    
            #Para indicar que el recurso fue modificado
            print("La información del recurso fue modificada con éxito.")

            #Variable para saber si el usuario desea modificar otro atributo del recurso
            continuar = leer_entero(1, 2, "¿Desea modificar otro atributo del recurso? 1.Si 2.No: ")
            #Si escoje 2.No, asignar False a la variable coincidencia para detener el ciclo
            if continuar == 2:
                coincidencia = False
        
        input("Presione Enter para continuar...")
    
    
    def buscar_recurso (self):
        """
        Este método permite consultar y mostrar la información de un recurso que es buscado por
        medio de su signatura topográfica, o para mostrar todos los recursos que coinciden si se
        busca por nombre o parte del nombre.
        Este método da solución al requerimiento 4 del análisis del problema.

        PARÁMETEROS:
        Ninguno

        RETORNO:
        Vacio

        Autor: Daniel Sánchez 29/05/2025
        """
        #Se crea una variable que servirá para identificar cómo quiere el usuario hacer la consulta
        decision = int
        decision = leer_entero(1, 2, "Seleccione cómo desea realizar la consulta:\n1.Búsqueda por nombre.\n2.Búsqueda por código.")
        #Dependiendo del valor en decision, se ejecuta una de las dos formas de búsqueda
        if (decision == 1):
            #Se declara la variable posicion y se le asigna None
            posicion = int
            posicion = None
            titulo_para_busqueda = str
            #Se pide al usuario que ingrese el título del recurso o parte de él
            titulo_para_busqueda = verificar_si_esta_vacio("Ingrese el título del recurso (o parte de él): ")
            #Se normaliza la cadena por medio de la función nomralizar_cadena. Eliminado mayúsculas, acentos y espacios
            titulo_para_busqueda = normalizar_cadena(titulo_para_busqueda)
            #El ciclo recorre el arreglo de recursos
            controlador_i = int
            print("*****RESULTADOS DE BÚSQUEDA*****")
            for controlador_i in range (len(self.inventario_de_recursos)):
                #Se verifica primero que la posición en el arreglo no esté vacía (Que tenga el valor None)
                if (self.inventario_de_recursos [controlador_i] != None):
                    #Si no lo está, se normaliza el titulo del recurso almacenado como atributo en esa posición
                    titulo_normalizado = normalizar_cadena(self.inventario_de_recursos[controlador_i].titulo)
                    #Se usa el método find() para buscar si el título o fragmento ingresado coincide con el titulo almacenado
                    if (titulo_normalizado.find(titulo_para_busqueda) != -1):
                        #Si find() retorna un valor diferente a -1, significa que encontró una coincidencia
                        #Se muestra la información de los recursos donde hubo coincidencias
                        self.inventario_de_recursos[controlador_i].mostrar_informacion()
                        #Se asigna a posición el valor en controlador_i
                        posicion = controlador_i

            #Si posicion sigue siendo None después del recorrido, entonces no hubo coincidencias
            if (posicion == None):
                print("No se encontró ningún resultado.")       
        elif (decision == 2):
            #Se declara una variable donde se almacenará la signatura topográfica que desea consultar el usuario
            signatura_para_busqueda = str
            signatura_para_busqueda = verificar_cadena_alfanumerica("Ingrese la signatura topográfica del recurso que desea consultar: ")
            #Se declara una variable bandera que se encarga de indicar si hubo o no coincidencia, se incializa en False
            coincidencia = bool
            coincidencia = False
            controlador_i = int
            print("*****RESULTADOS DE BÚSQUEDA*****")
            #El ciclo recorre el arreglo con los recursos
            for controlador_i in range (len(self.inventario_de_recursos)):
                #Se verifica que en esa posicion el arreglo no esté vacío
                if (self.inventario_de_recursos [controlador_i] != None):
                    #Se compara si la signatura topográfica del recurso almacenado coincide con la que ingresó el usuario
                    if (self.inventario_de_recursos [controlador_i].signatura_topografica == signatura_para_busqueda):
                        self.inventario_de_recursos[controlador_i].mostrar_informacion()
                        coincidencia = True
                        break
            
            if (not coincidencia):
                print("No se encontró ningún recurso con esa signatura topográfica.")
        
        input("Presione Enter para continuar...")

    def autenticar_usuario (self):
        """
            Este método permite autenticar al usuario. Retorna True si el usuario que desea autenticarse existe. False si no existe o 
            si la ID o código no coinciden.

            Este método da solución al requerimiento 13 del análisis del problema.

            PARÁMETEROS:
            Ninguno

            RETORNO:
            Booleano

            Autor: Mateo Galeano 24/06/2025
        """

        print("*********************\nAUTENTICACIÓN\n*********************")
        #Se piden los datos de autenticación
        id = leer_entero_no_acotado("Ingrese su número de identificación: ")
        user_code = verificar_cadena_alfanumerica("Ingrese su código de usuario: ")

        #Se recorre el arreglo, buscando al usuario con el nombre y código registrados
        for controlador_i in range (self.numero_de_usuarios):
            
            #Si el ID coincide, se verifica el código
            if (self.total_de_usuarios[controlador_i].id == id):
                #Si la contraseña también coincide, entonces se asigna al atributo usuario_autenticado ese usuario y retorna True
                if (self.total_de_usuarios[controlador_i].codigo == user_code):
                    self.usuario_autenticado = self.total_de_usuarios[controlador_i]
                    print("Usuario autenticado con éxito.")
                    return True
                else:
                    input("La contraseña ingresada es incorrecta. Presione enter para continuar...")
                    return False
            
        #Si no se encuentra al usuario con el nombre ingresado, entonces se retorna False
        input(f"El ID ingresado ({id}) no coincide con ningún usuario registrado. Presione Enter para continuar...")
        return False

    def mostrar_menu_usuario_estudiante_y_empleado (self):
        decision = int
        decision = 0
        while (decision != 6):
            decision = leer_entero(1, 6, "**************\nMENÚ\n**************\nSeleccione una opción:\n1.Consultar y buscar recursos.\n2.Modificar datos personales.\n3.Prestar un recurso.\n4.Devolver un recurso.\n5.Verificar historial de préstamos.\n6.Cerrar sesión y regresar al menú principal.")
            match decision:
                case 1:
                    self.buscar_recurso()
                case 2:
                    self.modificar_info_usuario()
                case 3:
                    pass
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    print("Sesión cerrada.")
                    self.usuario_autenticado = None

    def mostrar_menu_bibliotecario (self):
        decision = int
        decision = 0
        while (decision != 8):
            decision = leer_entero(1, 8, "**************\nMENÚ-BIBLIOTECARIO\n**************\nSeleccione una opción:\n1.Agregar recursos.\n2.Modificar recurso.\n3.Buscar recurso.\n4.Registrar préstamo.\n5.Registrar devolución.\n6.Consultar el historial de préstamos de un recurso.\n7.Consultar el historial de préstamos de un usuario.\n8.Cerrar sesión y salir.")
            match decision:
                case 1:
                    self.registrar_recurso()
                case 2:
                    self.modificar_info_recurso()
                case 3:
                    self.buscar_recurso()
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case 8:
                    print("Sesión cerrada.")
                    self.usuario_autenticado = None
 
    def mostrar_menu_administrador (self):
        decision = int
        decision = 0
        while (decision != 12):
            decision = leer_entero(1, 12, "**************\nMENÚ-ADMINISTRADOR\n**************\nSeleccione una opción:\n1.Registrar recurso.\n2.Modificar recurso.\n3.Buscar recurso.\n4.Registrar préstamo.\n5.Registrar devolución.\n6.Consultar el historial de préstamos de un recurso.\n7.Consultar el historial de préstamos de un usuario.\n8.Agregar usuario.\n9.Modificar usuario.\n10.Eliminar usuario.\n11.Generar reportes del sistema.\n12.Cerrar sesión y salir.")
            match decision:
                case 1:
                    self.registrar_recurso()
                case 2:
                    self.modificar_info_recurso()
                case 3:
                    self.buscar_recurso()
                case 4:
                    pass
                case 5:
                    pass
                case 6:
                    pass
                case 7:
                    pass
                case 8:
                    self.registrar_usuario()
                case 9:
                    self.modificar_info_usuario()
                case 10:
                    pass
                case 11:
                    pass
                case 12:
                    print("Sesión cerrada.")
                    self.usuario_autenticado = None

    def modificar_info_usuario(self):
        print("**************\nMODIFICAR-INFORMACIÓN-USUARIO\n**************")
        #Se crea una variable posicion para almacenar la posicion del usuario encontrado
        posicion = int
        posicion = None
        kiki = bool
        
        #Si el tipo de usuario autenticado es administrador, se pide al administrador que ingrese el id del usuario al cual quiere modificar sus datos
        if (self.usuario_autenticado.tipo_de_usuario) == Usuario.PERFIL_ADMIN:
            i = int
            id_para_busqueda = int
            id_para_busqueda = leer_entero_no_acotado("Ingrese el id del usuario: ")

            #Se busca un un usuario con un id igual al id ingresado
            for i in range(self.numero_de_usuarios):
                if id_para_busqueda == self.total_de_usuarios[i].id:
                    posicion = i
                    #Muestra la informacion del usuario
                    print(f"INFORMACIÓN DEL USUARIO\nNombre: {self.total_de_usuarios[posicion].nombre_usuario}\nDirección: {self.total_de_usuarios[posicion].direccion_residencia}\nTeléfono: {self.total_de_usuarios[posicion].telefono}\nEmail: {self.total_de_usuarios[posicion].email}\nCódigo: {self.total_de_usuarios[posicion].codigo}\nTipo de usuario: {self.total_de_usuarios[posicion].tipo_de_usuario}\nId: {self.total_de_usuarios[posicion].id}")

            #Si no se encontro ningún usuario con el id ingresado, la posición se mantendrá en None y se muestra el siguiente mensaje
            if posicion == None:
                print("No existe ningún usuario con el id ingresado.")
                input("Presione Enter para continuar...")
                return False
            
            #Si se encontro un usuario con el id ingresado, se despliega el siguiente menú
            while (posicion != None):
                desicion = int
                desicion = 0

                print("1.Nombre")
                print("2.Dirección de residencia")
                print("3.Número telefónico")
                print("4.Correo electrónico")
                print("5.Código")
                print("6.Número de identificación")
                print("7.Tipo de usuario")
                desicion = leer_entero(1, 7, "Seleccion una opción: ")
                match(desicion):
                    case 1:
                        self.total_de_usuarios[posicion].nombre_usuario = verificar_si_esta_vacio("Ingrese nuevo nombre: ")
                    case 2:
                        self.total_de_usuarios[posicion].direccion_residencia = verificar_si_esta_vacio("Ingrese la nueva dirección de su residencia: ")
                    case 3:
                        self.total_de_usuarios[posicion].telefono = leer_entero_no_acotado("Ingrese nuevo número telefónico: ")
                    case 4:
                        self.total_de_usuarios[posicion].email = verificar_email("Ingrese una nueva dirección de correo electrónico: ")
                    case 5:
                        self.total_de_usuarios[posicion].codigo = verificar_cadena_alfanumerica("Ingrese nuevo código del usuario: ")
                    
                    case 6:
                        id = int
                        id = 0
                        igual = bool
                        igual = True
                        #Verifica que no se ingrese un id igual al de otro usuario
                        while (igual):
                            id = leer_entero_no_acotado("Ingrese nuevo número de identificación: ")
                            igual = False
                            for i in range(self.numero_de_usuarios):
                                if (id == self.total_de_usuarios[i].id):
                                    print("Error. Este id pertenece a otro usuario")
                                    igual = True
                        #Si el id no es igual al de otro usuario, se le agrega el id al usuario al cual estan modificando sus datos 
                        self.total_de_usuarios[posicion].id = id
                    case 7:
                        tipo = leer_entero(1, 4, "Seleccione el nuevo tipo de usuario\n1.Estudiante\n2.Empleado\n3.Bibliotecario\n4.Administrador\n")
                        match(tipo):
                            case 1:
                                self.total_de_usuarios[posicion].tipo_de_usuario = Usuario.PERFIL_ESTUDIANTE
                            case 2:
                                self.total_de_usuarios[posicion].tipo_de_usuario = Usuario.PERFIL_EMPLEADO
                            case 3:
                                self.total_de_usuarios[posicion].tipo_de_usuario = Usuario.PERFIL_BIBLIOTECARIO
                            case 4:
                                self.total_de_usuarios[posicion].tipo_de_usuario = Usuario.PERFIL_ADMIN
                
                #Para indicar que el recurso fue modificado
                print("La información del usuario fue modificada con éxito.")

                #Variable para saber si el usuario desea modificar otro atributo del recurso
                continuar = leer_entero(1, 2, "¿Desea modificar otro atributo del recurso? 1.Si 2.No: ")
                #Si escoje 2.No, asignar False a la variable coincidencia para detener el ciclo
                if continuar == 2:
                    posicion = None
            
            input("Presione Enter para continuar...")

        #Si el usuario es de tipo estudiante o empleado, se despliega un menú para que modifique su información personal
        else:
            #Muestra la informacion del usuario
            print(f"INFORMACIÓN DEL USUARIO\nNombre: {self.usuario_autenticado.nombre_usuario}\nDirección: {self.usuario_autenticado.direccion_residencia}\nTeléfono: {self.usuario_autenticado.telefono}\nEmail: {self.usuario_autenticado.email}\nCódigo: {self.usuario_autenticado.codigo}\nTipo de usuario: {self.usuario_autenticado.tipo_de_usuario}\nId: {self.usuario_autenticado.id}")
            kiki = True
            i = int
            while (kiki):
                desicion = int
                desicion = 0

                print("1.Nombre")
                print("2.Dirección de residencia")
                print("3.Número telefónico")
                print("4.Correo electrónico")
                print("5.Código")
                print("6.Número de identificación")
                desicion = leer_entero(1, 6, "Seleccion una opción: ")
                match(desicion):
                    case 1:
                        self.usuario_autenticado.nombre_usuario = verificar_si_esta_vacio("Ingrese nuevo nombre: ")
                    case 2:
                        self.usuario_autenticado.direccion_residencia = verificar_si_esta_vacio("Ingrese la nueva dirección de su residencia: ")
                    case 3:
                        self.usuario_autenticado.telefono = leer_entero_no_acotado("Ingrese nuevo número telefónico: ")
                    case 4:
                        self.usuario_autenticado.email = verificar_email("Ingrese una nueva dirección de correo electrónico: ")
                    case 5:
                        self.usuario_autenticado.codigo = verificar_cadena_alfanumerica("Ingrese nuevo código del usuario: ")
                    case 6:
                        id = int
                        id = 0
                        igual = bool
                        igual = True
                        #Verifica que no se ingrese un id igual al de otro usuario
                        while (igual):
                            id = leer_entero_no_acotado("Ingrese nuevo número de identificación: ")
                            igual = False
                            for i in range(self.numero_de_usuarios):
                                if (id == self.total_de_usuarios[i].id):
                                    print("Error. Este id pertenece a otro usuario")
                                    igual = True
                        #Si el id no es igual al de otro usuario, se le agrega el id al usuario al cual estan modificando sus datos 
                        self.usuario_autenticado.id = id

                #Para indicar que el recurso fue modificado
                print("La información del recurso fue modificada con éxito.")

                #Variable para saber si el usuario desea modificar otro atributo del recurso
                continuar = leer_entero(1, 2, "¿Desea modificar otro atributo del recurso? 1.Si 2.No: ")
                #Si escoje 2.No, asignar False a la variable coincidencia para detener el ciclo
                if continuar == 2:
                    kiki = False
            
            input("Presione Enter para continuar...")


    def main (self):
        decision = int
        decision = 0
        while (decision != 3):
            decision = leer_entero(1, 3, "*****SISTEMA DE BIBLIOTECA-MENÚ PRINCIPAL*****\nSeleccione una opción:\n1.Registrarse.\n2.Autenticarse.\n3.Finalizar el programa.\n")
            match decision:
                case 1:
                    print("********\nREGISTRO\n********")
                    decision = leer_entero (1, 2, "Indique su perfil:\n1.ESTUDIANTE.\n2.EMPLEADO.")
                    if (decision == 1):
                        self.registrar_usuario()
                    else:
                        self.registrar_usuario()
                        self.total_de_usuarios[self.numero_de_usuarios-1].tipo_de_usuario = Usuario.PERFIL_EMPLEADO
                
                case 2:
                    if (self.autenticar_usuario()):
                        if (self.usuario_autenticado.tipo_de_usuario == Usuario.PERFIL_ADMIN):
                            self.mostrar_menu_administrador()
                        elif (self.usuario_autenticado.tipo_de_usuario == Usuario.PERFIL_BIBLIOTECARIO):
                            self.mostrar_menu_bibliotecario()
                        elif (self.usuario_autenticado.tipo_de_usuario == Usuario.PERFIL_EMPLEADO or self.usuario_autenticado.tipo_de_usuario == Usuario.PERFIL_ESTUDIANTE):
                            self.mostrar_menu_usuario_estudiante_y_empleado()
                
                case 3:
                    print("Programa Finalizado.")



    def principal (self):
        """
        Este método despliega el menú de la aplicación e invoca a los métodos respectivos de cada opción,
        que en este caso solo engloba a los primeros 4 requerimientos de la entrega No.1 del proyecto

        PARÁMETEROS:
        Ninguno

        RETORNO:
        Vacio

        Autor: Diego Candamil 1/05/2025
        """

        """
        Se declara una variable entera llamada "menu", que permite controlar el ciclo
        """
        menu = int
        menu = 0
        while (menu != 5):
            menu = leer_entero(1, 5, "**************\nMENÚ PRINCIPAL\n**************\nSeleccione una opción:\n1.Registrar un recurso.\n2.Registrar un usuario.\n3.Modificar recurso.\n4.Consultar recurso.\n5.Salir.")
            match menu:
                case 1:
                    self.registrar_recurso()
                    input("Presione Enter para regresar al menú principal...")
                    
                case 2:
                    self.registrar_usuario()
                    input("Presione Enter para regresar al menú principal...")
                case 3:
                    self.modificar_info_recurso()
                    input("Presione Enter para regresar al menú principal...")
                case 4:
                    self.buscar_recurso()
                    input("Presione Enter para regresar al menú principal...")
                case 5:
                    print("Ejecución finalizada.")
        """
        Este método despliega el menú de la aplicación e invoca a los métodos respectivos de cada opción,
        que en este caso solo engloba a los primeros 4 requerimientos de la entrega No.1 del proyecto

        PARÁMETEROS:
        Ninguno

        RETORNO:
        Vacio

        Autor: Diego Candamil 1/05/2025
        """

        """
        Se declara una variable entera llamada "menu", que permite controlar el ciclo
        """
        menu = int
        menu = 0
        while (menu != 5):
            menu = leer_entero(1, 5, "**************\nMENÚ PRINCIPAL\n**************\nSeleccione una opción:\n1.Registrar un recurso.\n2.Registrar un usuario.\n3.Modificar recurso.\n4.Consultar recurso.\n5.Salir.")
            match menu:
                case 1:
                    self.registrar_recurso()
                    input("Presione Enter para regresar al menú principal...")
                    
                case 2:
                    self.registrar_usuario()
                    input("Presione Enter para regresar al menú principal...")
                case 3:
                    self.modificar_info_recurso()
                    input("Presione Enter para regresar al menú principal...")
                case 4:
                    self.buscar_recurso()
                    input("Presione Enter para regresar al menú principal...")
                case 5:
                    print("Ejecución finalizada.")