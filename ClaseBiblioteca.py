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
# Se importa la clase usuario, préstamo y multa
from ClaseUsuario import *
from ClasePrestamo import *
from ClaseMulta import *
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
    prestamos_activos: que es un arreglo que contiene a los préstamos que se realizan en la biblioteca y se encuentran vigentes.
    numero_de_prestamos_activos: que es un contador que se encargará de cuantificar los préstamos que hay en el arreglo.
    usuario_autenticado: que permite identificar cuál de los usuarios registrados se encuentra usando la aplicación.
    prestamos_inactivos: que es un arreglo que contiene a los préstamos que ya han finalizado.
    numero_de_prestamos_inactivos: que es un contador que se encargará de cuantificar los préstamos que han finalizado.

    CONSTANTES:
    MAX_USUARIOS: que indica cuál es el número máximo de usuarios que pueden ser almacenados por la aplicación.
    MAX_RECURSOS: que indica cuál es el número máximo de recursos que pueden ser almacenados por la aplicación.
    MAX_PRESTAMOS: que indica cuál es el número máximo de préstamos que pueden ser almacenados por la aplicación.
    MAX_PRESTAMOS_INACTIVOS: que indica el número máximo de préstamos que pueden ser almacenados por la aplicación.
    ARCHIVO_RECURSOS: contiene la ruta del archivo en donde se guardan los recursos.
    ARCHIVO_USUARIOS: contiene la ruta del archivo en donde se guardan los usuarios. 
    ARCHIVO_PRESTAMOS_ACTIVOS: contiene la ruta del archivo en donde se guardan los préstamos activos. 
    ARCHIVO_PRESTAMOS_INACTIVOS: contiene la ruta del archivo en donde se guardan los préstamos inactivos.

    """

    #DECLARACIÓN DE LOS ATRIBUTOS
    numero_de_recursos = int
    numero_de_usuarios = int
    numero_de_prestamos_activos = int
    numero_de_prestamos_inactivos = int
    inventario_de_recursos = np.ndarray
    total_de_usuarios = np.ndarray
    prestamos_activos = np.ndarray
    prestamos_inactivos = np.ndarray
    usuario_autenticado = Usuario

    #DECLARACIÓN DE LAS CONSTANTES
    MAX_USUARIOS = 200 
    MAX_RECURSOS = 200 
    MAX_PRESTAMOS = 200 
    MAX_PRESTAMOS_INACTIVOS = 400
    ARCHIVO_RECURSOS = "archivo_recursos.npy"
    ARCHIVO_USUARIOS = "archivo_usuarios.npy"
    ARCHIVO_PRESTAMOS_ACTIVOS = "archivo_prestamos_activos.npy"
    ARCHIVO_PRESTAMOS_INACTIVOS = "archivo_prestamos_inactivos.npy"


    #MÉTODO CONSTRUCTOR DE LA CLASE (ANTIGUO)
    """def __init__ (self, numero_de_recursos = 0, numero_de_usuarios = 2, numero_de_prestamos_activos = 0, numero_de_prestamos_inactivos = 0 ):
        #Cuando se crea el objeto de la clase, los valores por defecto de todos los contadores es cero.
        self.numero_de_recursos = numero_de_recursos
        self.numero_de_usuarios = numero_de_usuarios
        self.numero_de_prestamos_activos = numero_de_prestamos_activos
        self.numero_de_prestamos_inactivos = numero_de_prestamos_inactivos
        #Se inicializan los arreglos de objetos de tipos recurso, usuario y préstamo con el valor None por defecto
        self.inventario_de_recursos = np.full((self.MAX_RECURSOS), fill_value = None, dtype = object)
        self.total_de_usuarios = np.full((self.MAX_USUARIOS), fill_value = None, dtype = object)
        self.prestamos_activos = np.full((self.MAX_PRESTAMOS), fill_value = None, dtype = object)
        self.prestamos_inactivos = np.full((self.MAX_PRESTAMOS_INACTIVOS), fill_value = None, dtype = object)

        #SE CREA UN PRIMER USUARIO ADMINISTRADOR
        self.total_de_usuarios[0] = Usuario(nombre_usuario="Mateo", direccion_residencia="Medellin", telefono=300600200, email="m@gmail.com", codigo="m1811", id=101)
        self.total_de_usuarios[0].tipo_de_usuario = Usuario.PERFIL_ADMIN

        #SE CREA UN PRIMER USUARIO BIBLIOTECARIO
        self.total_de_usuarios[1] = Usuario(nombre_usuario="Daniel", direccion_residencia="Medellin", telefono=300700300, email="d@gmail.com", codigo="d123", id=102)
        self.total_de_usuarios[1].tipo_de_usuario = Usuario.PERFIL_BIBLIOTECARIO
        
        self.numero_de_usuarios = numero_de_usuarios

        #SE INICIALIZA EL ATRIBUTO QUE PERMITE IDENTIFICAR EL USUARIO QUE SE ENCUENTRA AUTENTICADO
        self.usuario_autenticado = None #Al principio no hay usuarios autenticados
    """

    #NUEVO MÉTODO CONSTRUCTOR DE LA CLASE
    def __init__ (self):
        # Se cargan los datos de cada arreglo y cada contador

        #DATOS DEL ARREGLO DE RECURSOS Y SU CONTADOR
        self.inventario_de_recursos, self.numero_de_recursos = self.cargar_datos(self.ARCHIVO_RECURSOS, self.MAX_RECURSOS)

        #DATOS DEL ARREGLO DE USUARIOS Y SU CONTADOR
        self.total_de_usuarios, self.numero_de_usuarios = self.cargar_datos(self.ARCHIVO_USUARIOS, self.MAX_USUARIOS)

        #DATOS DEL ARREGLO DE PRÉSTAMOS ACTIVOS Y SU CONTADOR
        self.prestamos_activos, self.numero_de_prestamos_activos = self.cargar_datos(self.ARCHIVO_PRESTAMOS_ACTIVOS, self.MAX_PRESTAMOS)

        #DATOS DEL ARREGLO DE PRÉSTAMOS INACTIVOS Y SU CONTADOR
        self.prestamos_inactivos, self.numero_de_prestamos_inactivos = self.cargar_datos(self.ARCHIVO_PRESTAMOS_INACTIVOS, self.MAX_PRESTAMOS_INACTIVOS)
        
        
        
        # Si la APP se ejecuta por primera vez (o ha habido un error), se crean dos usuarios por defecto de tipo administrador y bibliotecario
        if (self.numero_de_usuarios == 0):
            self.total_de_usuarios[0] = Usuario(nombre_usuario="Mateo", direccion_residencia="Medellin", telefono=300600200, email="m@gmail.com", codigo="m1811", id=101)
            self.total_de_usuarios[0].tipo_de_usuario = Usuario.PERFIL_ADMIN
            self.total_de_usuarios[1] = Usuario(nombre_usuario="Daniel", direccion_residencia="Medellin", telefono=300700300, email="d@gmail.com", codigo="d123", id=102)
            self.total_de_usuarios[1].tipo_de_usuario = Usuario.PERFIL_BIBLIOTECARIO
            self.numero_de_usuarios = 2
            #LOS DOS PRIMEROS USUARIOS SE GUARDAN
            if (self.guardar_datos(self.total_de_usuarios, self.ARCHIVO_USUARIOS)):
                print("Se ha guardado con éxito un primer bibliotecario y administrador.")
            else:
                print("Ha habido un error al guardar al primer bibliotecario y administrador.")
        
        #Al inciar, no hay usuario autenticado
        self.usuario_autenticado = None

        #Se deben reconectar las direcciones de memoria para los atributos de recurso_prestado y titular_del_prestamo para cada préstamo

        for i in range(self.numero_de_prestamos_activos):
            for j in range(self.numero_de_usuarios):
                if (self.prestamos_activos[i].titular_del_prestamo.id == self.total_de_usuarios[j].id):
                    self.prestamos_activos[i].titular_del_prestamo = self.total_de_usuarios[j]

        #Se hace la misma reconexión, para los recursos
        for i in range(self.numero_de_prestamos_activos):
            for j in range(self.numero_de_recursos):
                if (self.prestamos_activos[i].recurso_prestado.signatura_topografica == self.inventario_de_recursos[j].signatura_topografica):
                    self.prestamos_activos[i].recurso_prestado = self.inventario_de_recursos[j]

        #Se hace la reconexión para las multas
        for i in range (self.numero_de_usuarios):
            for j in range(self.total_de_usuarios[i].numero_de_multas):
                for k in range(self.numero_de_recursos):
                    if (self.total_de_usuarios[i].multas_vigentes[j].recurso_con_multa.signatura_topografica == self.inventario_de_recursos[k].signatura_topografica):
                        self.total_de_usuarios[i].multas_vigentes[j].recurso_con_multa = self.inventario_de_recursos[k]

        #Se hace la reconexión para los prestamos inactivos
        for i in range(self.numero_de_prestamos_inactivos):
            for j in range(self.numero_de_usuarios):
                if (self.prestamos_inactivos[i].titular_del_prestamo.id == self.total_de_usuarios[j].id):
                    self.prestamos_inactivos[i].titular_del_prestamo = self.total_de_usuarios[j]

    def guardar_datos (self, arreglo_de_datos, archivo):
        """ 
        Este método almacena los datos de un arreglo en un archivo

        PARÁMETROS:
        arreglo_de_datos = arreglo Numpy con los datos a alamcenar.
        archivo = URL relativa del archivo en el que se almacenarán los datos.

        RETORNO:
        True si almacena los datos correctamente en el archivo.
        False si no logra almacenar los datos en el archivo.
        """
        try:
            np.save(archivo, arreglo_de_datos)
            return True
        except (FileNotFoundError, EOFError):
            print(f"Error: No se pudieron almacenar los datos en el archivo {archivo}.")
            return False



    def cargar_datos (self, archivo, num_max_datos):
        """ 
        Este método carga los datos de un archivo, en un arreglo específico.

        PARAMETROS:
            archivo = URL relativa del archivo a abrir.
            num_max_datos = indica el tamaño máximo de datos que almacena el arreglo.

        RETORNO:
            arreglo_de_datos = arreglo con los datos cargados.
            num_datos = cantidad de datos cargados en el arreglo.
        
        """
        try:
            arreglo_de_datos = np.load(archivo, allow_pickle=True)
            i = 0
            while (arreglo_de_datos[i] != None):
                i += 1
            return arreglo_de_datos, i

        except (FileNotFoundError, EOFError):
            print(f"Error: No pudo cargarse el archivo {archivo}. Se generará un arreglo vacío.")
            arreglo_de_datos = np.full((num_max_datos), fill_value= None, dtype= object)
            return arreglo_de_datos, 0


    def registrar_recurso (self):
        """
        Este método crea y agrega un recurso al arreglo de recursos
        por lo que da solución al requerimiento 1 del análisis del problema

        PARÁMETEROS:
        Ninguno

        RETORNO:
        True si el registro se hace exitosamente.
        False si no se hace el registro.

        Autor: Daniel Sánchez 29/05/2025
        """
        
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
            return True

        return False
    
    
    def registrar_usuario (self):
        """
        Este método crea y agrega un usuario al arreglo de usuarios
        Por lo que da solución al requerimiento 2 del análisis del problema

        PARÁMETEROS:
        Ninguno

        RETORNO:
        True si el registro pudo realizarse
        False si el registro no pudo realizarse

        Autor: Mateo Daniel Galeano Quiñones 29/05/2025
        """ 
        
    
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
            return True
        
        return False
    

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
        el_recurso_esta_prestado = bool
        el_recurso_esta_prestado = False
        signatura_para_busqueda = str
        coincidencia = bool
        recurso = Recurso
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
            print("No se encontró ninguna coincidencia. Se le llevará de vuelta al menú.")
        else:
            #Si la coincidencia no es False, entonces se procede a verificar si ese recurso encontrado está prestado
           if (self.inventario_de_recursos[num_del_recurso].estado == "PRESTADO"):
               el_recurso_esta_prestado = True

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
                        if (not el_recurso_esta_prestado):
                            #Esta variable nos ayuda a elegir una opción
                            seleccion = leer_entero(1, 4, "Asigne un nuevo estado:\n1.DISPONIBLE.\n2.REPARACIÓN.\n3.INACTIVO.\n4.PERDIDO.")
    
                            if seleccion == 1:
                                self.inventario_de_recursos[num_del_recurso].estado = "DISPONIBLE"
                            elif seleccion == 2:
                                self.inventario_de_recursos[num_del_recurso].estado = "REPARACIÓN"
                            elif seleccion == 3:
                                self.inventario_de_recursos[num_del_recurso].estado = "INACTIVO"
                            elif seleccion == 4:
                                self.inventario_de_recursos[num_del_recurso].estado = "PERDIDO"
                        else:
                            print("El recurso se encuentra actualmente prestado, registre la devolución para poder editar su estado.")
                    
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
                        if (not el_recurso_esta_prestado):
                            #Esta variable nos ayuda a elegir una opción
                            seleccion = leer_entero(1, 4, "Asigne un nuevo estado:\n1.DISPONIBLE.\n2.REPARACIÓN.\n3.INACTIVO.\n4.PERDIDO.")
                        
                        
                            if seleccion == 1:
                                self.inventario_de_recursos[num_del_recurso].estado = "DISPONIBLE"
                            elif seleccion == 2:
                                self.inventario_de_recursos[num_del_recurso].estado = "REPARACIÓN"
                            elif seleccion == 3:
                                self.inventario_de_recursos[num_del_recurso].estado = "INACTIVO"
                            elif seleccion == 4:
                                self.inventario_de_recursos[num_del_recurso].estado = "PERDIDO"
                        else:
                            print("El recurso se encuentra actualmente prestado. Registre la devolución para poder editar su estado.")
                    
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
                        if (not el_recurso_esta_prestado):
                            #Esta variable nos ayuda a elegir una opción
                            seleccion = leer_entero(1, 4, "Asigne un nuevo estado:\n1.DISPONIBLE.\n2.REPARACIÓN.\n3.INACTIVO.\n4.PERDIDO.")
                            
                            if seleccion == 1:
                                self.inventario_de_recursos[num_del_recurso].estado = "DISPONIBLE"
                            elif seleccion == 2:
                                self.inventario_de_recursos[num_del_recurso].estado = "REPARACIÓN"
                            elif seleccion == 3:
                                self.inventario_de_recursos[num_del_recurso].estado = "INACTIVO"
                            elif seleccion == 4:
                                self.inventario_de_recursos[num_del_recurso].estado = "PERDIDO"
                        else:
                            print("El recurso se encuentra actualmente prestado. Registre la devolución para poder editar su estado.")
                    
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
                        if (not el_recurso_esta_prestado):
                            #Esta variable permite almacenar la elección del usuario
                            seleccion = leer_entero(1, 4, "Asigne un nuevo estado:\n1.DISPONIBLE.\n2.REPARACIÓN.\n3.INACTIVO.\n4.PERDIDO.")
                      
                            if seleccion == 1:
                                self.inventario_de_recursos[num_del_recurso].estado = "DISPONIBLE"
                            elif seleccion == 2:
                                self.inventario_de_recursos[num_del_recurso].estado = "REPARACIÓN"
                            elif seleccion == 3:
                                self.inventario_de_recursos[num_del_recurso].estado = "INACTIVO"
                            elif seleccion == 4:
                                self.inventario_de_recursos[num_del_recurso].estado = "PERDIDO"
                        else:
                            print("El recurso se encuentra actualmente prestado. Registre la devolución para poder editar su estado.")
                    
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
        while (decision != 4):
            decision = leer_entero(1, 4, "**************\nMENÚ\n**************\nSeleccione una opción:\n1.Consultar y buscar recursos.\n2.Modificar datos personales.\n3.Verificar historial de préstamos.\n4.Cerrar sesión y regresar al menú principal.")
            match decision:
                case 1:
                    self.buscar_recurso()
                    input("Presione Enter para continuar...")
                case 2:
                    if (self.modificar_usuario(self.usuario_autenticado, False)):
                        print("La información fue modificada con éxito.")
                        ##PUNTO DE GUARDADO
                        if (self.guardar_datos(self.prestamos_activos, self.ARCHIVO_PRESTAMOS_ACTIVOS)):
                            if (self.guardar_datos(self.prestamos_inactivos, self.ARCHIVO_PRESTAMOS_INACTIVOS)):
                                if (self.guardar_datos(self.total_de_usuarios, self.ARCHIVO_USUARIOS)):
                                    if (self.guardar_datos(self.inventario_de_recursos, self.ARCHIVO_RECURSOS)):
                                        print("Datos guardados con éxito.")
                                    else:
                                        print("Error: los datos no pudieron guardarse.")
                                else:
                                    print("Error: los datos no pudieron guardarse.")
                            else:
                                print("Error: los datos no pudieron guardarse.")
                        else:
                            print("Error: los datos no pudieron guardarse.")
                            
                        input("Presione Enter para continuar...")
                    else:
                        input("La información no pudo modificarse.\nPresione Enter para continuar...")
                case 3:
                    self.mostrar_historial_usuario(self.usuario_autenticado)
                    input("Presione Enter para continuar...")
                case 4:
                    print("Sesión cerrada.")
                    self.usuario_autenticado = None

    def mostrar_menu_bibliotecario (self):
        decision = int
        decision = 0
        while (decision != 8):
            decision = leer_entero(1, 8, "**************\nMENÚ-BIBLIOTECARIO\n**************\nSeleccione una opción:\n1.Registrar recurso.\n2.Modificar recurso.\n3.Buscar recurso.\n4.Registrar préstamo.\n5.Registrar devolución.\n6.Consultar el historial de préstamos de un recurso.\n7.Consultar el historial de préstamos de un usuario.\n8.Cerrar sesión y salir.")
            match decision:
                case 1:
                    if (self.numero_de_recursos < self.MAX_RECURSOS):
                        print("********\nREGISTRO\n********")
                        if(self.registrar_recurso()):
                    
                            ##PUNTO DE GUARDADO
                            if (self.guardar_datos (self.inventario_de_recursos, self.ARCHIVO_RECURSOS)):
                                print("Datos guardados exitosamente.")
                            else:
                                print("Error: los datos no pudieron guardarse.")

                            input ("Presione Enter para continuar...")
                        else:
                            input("Presione Enter para continuar...")
                    else:
                        input("No hay espacio disponible para registrar más recursos.\nPresione Enter para continuar...")
                case 2:
                    self.modificar_info_recurso()
                    ##PUNTO DE GUARDADO
                    if (self.guardar_datos(self.prestamos_activos, self.ARCHIVO_PRESTAMOS_ACTIVOS)):
                        if (self.guardar_datos(self.prestamos_inactivos, self.ARCHIVO_PRESTAMOS_INACTIVOS)):
                            if (self.guardar_datos(self.total_de_usuarios, self.ARCHIVO_USUARIOS)):
                                if (self.guardar_datos(self.inventario_de_recursos, self.ARCHIVO_RECURSOS)):
                                    print("Datos guardados con éxito.")
                                else:
                                    print("Error: los datos no pudieron guardarse.")
                            else:
                                print("Error: los datos no pudieron guardarse.")
                        else:
                            print("Error: los datos no pudieron guardarse.")
                    else:
                        print("Error: los datos no pudieron guardarse.")
                    
                    input("Presione Enter para continuar...")
                case 3:
                    self.buscar_recurso()
                    input("Presione Enter para continuar...")
                case 4:
                    if (self.numero_de_prestamos_activos < self.MAX_PRESTAMOS):
                        id_para_busqueda = int
                        signatura_para_busqueda = str
                        pos_usuario = int
                        pos_recurso = int
                        id_para_busqueda = leer_entero_no_acotado("Ingrese la ID del usuario que desea realizar el préstamo: ")
                        signatura_para_busqueda = verificar_cadena_alfanumerica("Ingrese la signatura topográfica del recurso que desea prestar: ")
                        pos_usuario = self.buscar_usuario_por_id(identificacion=id_para_busqueda)
                        pos_recurso = self.buscar_recurso_por_signatura(signatura=signatura_para_busqueda)
                        if (pos_recurso == -1 and pos_usuario == -1):
                            print(f"El usuario con ID: {id_para_busqueda} no fue encontrado.")
                            print(f"El recurso con signatura topográfica: {signatura_para_busqueda} no fue encontrado.")
                            input("Presione Enter para continuar...")
                        elif (pos_recurso == -1 and pos_usuario != -1 ):
                            print(f"El recurso con signatura topográfica: {signatura_para_busqueda} no fue encontrado.")
                            input("Presione Enter para continuar...")
                        elif (pos_recurso != -1 and pos_usuario == -1):
                            print(f"El usuario con ID: {id_para_busqueda} no fue encontrado.")
                            input("Presione Enter para continuar...")
                        elif (pos_recurso != -1 and pos_usuario != -1):
                            if (self.registrar_prestamo(self.total_de_usuarios[pos_usuario], self.inventario_de_recursos[pos_recurso]) != None):
                                print("El préstamo fue registrado exitosamente.")
                                ##PUNTO DE GUARDADO
                                if (self.guardar_datos(self.prestamos_activos, self.ARCHIVO_PRESTAMOS_ACTIVOS)):
                                    if (self.guardar_datos(self.prestamos_inactivos, self.ARCHIVO_PRESTAMOS_INACTIVOS)):
                                        if (self.guardar_datos(self.total_de_usuarios, self.ARCHIVO_USUARIOS)):
                                            if (self.guardar_datos(self.inventario_de_recursos, self.ARCHIVO_RECURSOS)):
                                                print("Datos guardados con éxito.")
                                            else:
                                                print("Error: los datos no pudieron guardarse.")
                                        else:
                                            print("Error: los datos no pudieron guardarse.")
                                    else:
                                        print("Error: los datos no pudieron guardarse.")
                                else:
                                    print("Error: los datos no pudieron guardarse.")

                                input("Presione Enter para continuar...")
                            else:
                                input("El préstamo no pudo registrarse.\nPresione Enter para continuar...")
                    else:
                        input("No hay espacio disponible para registrar nuevos préstamos.\nPresione Enter para continuar...")
                case 5:
                    id_para_busqueda = int
                    pos_usuario = int
                    print("********\nREGISTRO-DEVOLUCIÓN\n********")
                    id_para_busqueda = leer_entero_no_acotado("Escriba la ID del usuario que desea realizar la devolución: ")
                    pos_usuario = self.buscar_usuario_por_id(identificacion=id_para_busqueda)
                    if (pos_usuario != -1):
                        if (self.devolver_prestamo(self.total_de_usuarios[pos_usuario])):
                            ##PUNTO DE GUARDADO
                            if (self.guardar_datos(self.prestamos_activos, self.ARCHIVO_PRESTAMOS_ACTIVOS)):
                                if (self.guardar_datos(self.prestamos_inactivos, self.ARCHIVO_PRESTAMOS_INACTIVOS)):
                                    if (self.guardar_datos(self.total_de_usuarios, self.ARCHIVO_USUARIOS)):
                                        if (self.guardar_datos(self.inventario_de_recursos, self.ARCHIVO_RECURSOS)):
                                            print("Datos guardados con éxito.")
                                        else:
                                            print("Error: los datos no pudieron guardarse.")
                                    else:
                                        print("Error: los datos no pudieron guardarse.")
                                else:
                                    print("Error: los datos no pudieron guardarse.")
                            else:
                                print("Error: los datos no pudieron guardarse.")
                            input("Presione Enter para continuar...")
                        else:
                            input("El usuario no tiene préstamos a su nombre\nPresione Enter para continuar...")
                    else:
                        input(f"El usuario con ID {id_para_busqueda} no fue encontrado.\nPresione Enter para continuar...")
                case 6:
                    pos_recurso = int
                    signatura_para_busqueda = verificar_cadena_alfanumerica("Ingrese la signatura topográfica del recurso: ")
                    pos_recurso = self.buscar_recurso_por_signatura(signatura=signatura_para_busqueda)
                    
                    if (pos_recurso != -1):
                        self.historial_prestamos_recurso(self.inventario_de_recursos[pos_recurso])
                        input("Presione Enter para continuar...")
                    else:
                        input(f"El recurso con signatura topográfica {signatura_para_busqueda} no fue encontrado.\nPresione Enter para continuar...")
                case 7:
                    id_para_busqueda = int
                    id_para_busqueda = leer_entero_no_acotado("Escriba la ID del usuario al cual desea ver su historial de préstamos: ")
                    pos_usuario = self.buscar_usuario_por_id(identificacion=id_para_busqueda)
                    if (pos_usuario != -1):
                        self.mostrar_historial_usuario(self.total_de_usuarios[pos_usuario])
                        input("Presione Enter para continuar...")
                    else:
                        input(f"El usuario con ID {id_para_busqueda} no fue encontrado.\nPresione Enter para continuar...")
                case 8:
                    print("Sesión cerrada.")
                    self.usuario_autenticado = None
 
    def mostrar_menu_administrador (self):
        decision = int
        decision = 0
        while (decision != 13):
            decision = leer_entero(1, 13, "**************\nMENÚ-ADMINISTRADOR\n**************\nSeleccione una opción:\n1.Registrar recurso.\n2.Modificar recurso.\n3.Buscar recurso.\n4.Registrar préstamo.\n5.Registrar devolución.\n6.Consultar el historial de préstamos de un recurso.\n7.Consultar el historial de préstamos de un usuario.\n8.Agregar usuario.\n9.Modificar usuario.\n10.Eliminar usuario.\n11.Generar reportes de usuarios morosos\n12.Generar Top 5 de recursos más prestados.\n13.Cerrar sesión y salir.")
            match decision:
                case 1:
                    if (self.numero_de_recursos < self.MAX_RECURSOS):
                        print("********\nREGISTRO\n********")
                        if(self.registrar_recurso()):
                    
                            ##PUNTO DE GUARDADO
                            if (self.guardar_datos (self.inventario_de_recursos, self.ARCHIVO_RECURSOS)):
                                print("Datos guardados exitosamente.")
                            else:
                                print("Error: los datos no pudieron guardarse.")

                            input ("Presione Enter para continuar...")
                        else:
                            input("Presione Enter para continuar...")
                    else:
                        input("No hay espacio disponible para registrar más recursos.\nPresione Enter para continuar...")
                case 2:
                    self.modificar_info_recurso()
                    ##PUNTO DE GUARDADO
                    if (self.guardar_datos(self.prestamos_activos, self.ARCHIVO_PRESTAMOS_ACTIVOS)):
                        if (self.guardar_datos(self.prestamos_inactivos, self.ARCHIVO_PRESTAMOS_INACTIVOS)):
                            if (self.guardar_datos(self.total_de_usuarios, self.ARCHIVO_USUARIOS)):
                                if (self.guardar_datos(self.inventario_de_recursos, self.ARCHIVO_RECURSOS)):
                                    print("Datos guardados con éxito.")
                                else:
                                    print("Error: los datos no pudieron guardarse.")
                            else:
                                print("Error: los datos no pudieron guardarse.")
                        else:
                            print("Error: los datos no pudieron guardarse.")
                    else:
                        print("Error: los datos no pudieron guardarse.")
                    input("Presione Enter para continuar...")
                case 3:
                    self.buscar_recurso()
                    input("Presione Enter para continuar...")
                case 4:
                    if (self.numero_de_prestamos_activos < self.MAX_PRESTAMOS):
                        print("********\nREGISTRO\n********")
                        id_para_busqueda = int
                        signatura_para_busqueda = str
                        pos_usuario = int
                        pos_recurso = int
                        id_para_busqueda = leer_entero_no_acotado("Ingrese la ID del usuario que desea realizar el préstamo: ")
                        signatura_para_busqueda = verificar_cadena_alfanumerica("Ingrese la signatura topográfica del recurso que desea prestar: ")
                        pos_usuario = self.buscar_usuario_por_id(identificacion=id_para_busqueda)
                        pos_recurso = self.buscar_recurso_por_signatura(signatura=signatura_para_busqueda)
                        if (pos_recurso == -1 and pos_usuario == -1):
                            print(f"El usuario con ID: {id_para_busqueda} no fue encontrado.")
                            print(f"El recurso con signatura topográfica: {signatura_para_busqueda} no fue encontrado.")
                            input("Presione Enter para continuar...")
                        elif (pos_recurso == -1 and pos_usuario != -1 ):
                            print(f"El recurso con signatura topográfica: {signatura_para_busqueda} no fue encontrado.")
                            input("Presione Enter para continuar...")
                        elif (pos_recurso != -1 and pos_usuario == -1):
                            print(f"El usuario con ID: {id_para_busqueda} no fue encontrado.")
                            input("Presione Enter para continuar...")
                        elif (pos_recurso != -1 and pos_usuario != -1):
                            if (self.registrar_prestamo(self.total_de_usuarios[pos_usuario], self.inventario_de_recursos[pos_recurso]) != None):
                                print("El préstamo fue registrado exitosamente.")
                                ##PUNTO DE GUARDADO
                                if (self.guardar_datos(self.prestamos_activos, self.ARCHIVO_PRESTAMOS_ACTIVOS)):
                                    if (self.guardar_datos(self.prestamos_inactivos, self.ARCHIVO_PRESTAMOS_INACTIVOS)):
                                        if (self.guardar_datos(self.total_de_usuarios, self.ARCHIVO_USUARIOS)):
                                            if (self.guardar_datos(self.inventario_de_recursos, self.ARCHIVO_RECURSOS)):
                                                print("Datos guardados con éxito.")
                                            else:
                                                print("Error: los datos no pudieron guardarse.")
                                        else:
                                            print("Error: los datos no pudieron guardarse.")
                                    else:
                                        print("Error: los datos no pudieron guardarse.")
                                else:
                                    print("Error: los datos no pudieron guardarse.")
                                
                                input("Presione Enter para continuar...")
                            else:
                                input("El préstamo no pudo registrarse.\nPresione Enter para continuar...")
        
                    else:
                        input("No hay espacio disponible para registrar nuevos préstamos.\nPresione Enter para continuar...")
                case 5:
                    id_para_busqueda = int
                    pos_usuario = int
                    print("********\nREGISTRO-DEVOLUCIÓN\n********")
                    id_para_busqueda = leer_entero_no_acotado("Escriba la ID del usuario que desea realizar la devolución: ")
                    pos_usuario = self.buscar_usuario_por_id(identificacion=id_para_busqueda)
                    if (pos_usuario != -1):
                        if (self.devolver_prestamo(self.total_de_usuarios[pos_usuario])):
                            ##PUNTO DE GUARDADO
                            if (self.guardar_datos(self.prestamos_activos, self.ARCHIVO_PRESTAMOS_ACTIVOS)):
                                if (self.guardar_datos(self.prestamos_inactivos, self.ARCHIVO_PRESTAMOS_INACTIVOS)):
                                    if (self.guardar_datos(self.total_de_usuarios, self.ARCHIVO_USUARIOS)):
                                        if (self.guardar_datos(self.inventario_de_recursos, self.ARCHIVO_RECURSOS)):
                                            print("Datos guardados con éxito.")
                                        else:
                                            print("Error: los datos no pudieron guardarse.")
                                    else:
                                        print("Error: los datos no pudieron guardarse.")
                                else:
                                    print("Error: los datos no pudieron guardarse.")
                            else:
                                print("Error: los datos no pudieron guardarse.")
                            input("Presione Enter para continuar...")
                        else:
                            input("El usuario no tiene préstamos a su nombre\nPresione Enter para continuar...")
                    else:
                        input(f"El usuario con ID {id_para_busqueda} no fue encontrado.\nPresione Enter para continuar...")
                case 6:
                    pos_recurso = int
                    signatura_para_busqueda = verificar_cadena_alfanumerica("Ingrese la signatura topográfica del recurso: ")
                    pos_recurso = self.buscar_recurso_por_signatura(signatura=signatura_para_busqueda)
                    
                    if (pos_recurso != -1):
                        self.historial_prestamos_recurso(self.inventario_de_recursos[pos_recurso])
                        input("Presione Enter para continuar...")
                    else:
                        input(f"El recurso con signatura topográfica {signatura_para_busqueda} no fue encontrado.\nPresione Enter para continuar...")
                case 7:
                    id_para_busqueda = int
                    id_para_busqueda = leer_entero_no_acotado("Escriba la ID del usuario al cual desea ver su historial de préstamos: ")
                    pos_usuario = self.buscar_usuario_por_id(identificacion=id_para_busqueda)
                    if (pos_usuario != -1):
                        self.mostrar_historial_usuario(self.total_de_usuarios[pos_usuario])
                        input("Presione Enter para continuar...")
                    else:
                        input(f"El usuario con ID {id_para_busqueda} no fue encontrado.\nPresione Enter para continuar...")
                case 8:
                    if (self.numero_de_usuarios < self.MAX_USUARIOS):
                        print("********\nREGISTRO\n********")
                        tipo_de_usuario = leer_entero(1, 4, "Seleccione el perfil del nuevo usuario:\n1.ADMINISTRADOR.\n2.BIBLIOTECARIO.\n3.ESTUDIANTE.\n4.EMPLEADO.")
                        
                        if (self.registrar_usuario()):
                            if (tipo_de_usuario == 1):
                                self.total_de_usuarios[self.numero_de_usuarios-1].tipo_de_usuario = Usuario.PERFIL_ADMIN
                            elif (tipo_de_usuario == 2):
                                self.total_de_usuarios[self.numero_de_usuarios-1].tipo_de_usuario = Usuario.PERFIL_BIBLIOTECARIO
                            elif (tipo_de_usuario == 3):
                                self.total_de_usuarios[self.numero_de_usuarios-1].tipo_de_usuario = Usuario.PERFIL_ESTUDIANTE
                            elif (tipo_de_usuario == 4):
                                self.total_de_usuarios[self.numero_de_usuarios-1].tipo_de_usuario = Usuario.PERFIL_EMPLEADO
                            
                            ###PUNTO DE GUARDADO
                            if (self.guardar_datos(self.total_de_usuarios, self.ARCHIVO_USUARIOS)):
                                print("Datos guardados exitosamente.")
                            else:
                                print("Error: los datos no pudieron guardarse.")

                            input("Presione Enter para continuar...")
                        else:
                            input("Presione Enter para continuar...")
                    else:
                        input("No hay espacio disponible para registrar nuevos usuarios.\nPresione Enter para continuar...")
                    
                case 9:
                    pos_usuario = int
                    id_para_busqueda = leer_entero_no_acotado("Ingrese la ID del usuario que desea modificar: ")
                    pos_usuario = self.buscar_usuario_por_id(identificacion=id_para_busqueda)
                    if (pos_usuario != -1):
                        if (self.modificar_usuario(self.total_de_usuarios[pos_usuario])):
                            print("Información modificada con éxito.")

                            ##PUNTO DE GUARDADO
                            if (self.guardar_datos(self.prestamos_activos, self.ARCHIVO_PRESTAMOS_ACTIVOS)):
                                if (self.guardar_datos(self.prestamos_inactivos, self.ARCHIVO_PRESTAMOS_INACTIVOS)):
                                    if (self.guardar_datos(self.total_de_usuarios, self.ARCHIVO_USUARIOS)):
                                        if (self.guardar_datos(self.inventario_de_recursos, self.ARCHIVO_RECURSOS)):
                                            print("Datos guardados con éxito.")
                                        else:
                                            print("Error: los datos no pudieron guardarse.")
                                    else:
                                        print("Error: los datos no pudieron guardarse.")
                                else:
                                    print("Error: los datos no pudieron guardarse.")
                            else:
                                print("Error: los datos no pudieron guardarse.")
                            
                            input("Presione Enter para continuar...")
                        else:
                            input("La información no pudo modificarse.\nPresione Enter para continuar...")
                    else:
                        input("El usuario no fue encontrado.\nPresione Enter para continuar...")
                case 10:
                    pos_usuario = int
                    id_para_busqueda = leer_entero_no_acotado("Ingrese la ID del usuario que desea eliminar: ")
                    pos_usuario = self.buscar_usuario_por_id(identificacion=id_para_busqueda)
                    if (pos_usuario != -1 and self.usuario_autenticado.id != self.total_de_usuarios[pos_usuario].id):
                        if (self.eliminar_usuario(self.total_de_usuarios[pos_usuario], pos_usuario)):
                            print("Información modificada con éxito.")

                            ###PUNTO DE GUARDADO
                            if (self.guardar_datos(self.prestamos_activos, self.ARCHIVO_PRESTAMOS_ACTIVOS)):
                                if (self.guardar_datos(self.prestamos_inactivos, self.ARCHIVO_PRESTAMOS_INACTIVOS)):
                                    if (self.guardar_datos(self.total_de_usuarios, self.ARCHIVO_USUARIOS)):
                                        if (self.guardar_datos(self.inventario_de_recursos, self.ARCHIVO_RECURSOS)):
                                            print("Datos guardados con éxito.")
                                        else:
                                            print("Error: los datos no pudieron guardarse.")
                                    else:
                                        print("Error: los datos no pudieron guardarse.")
                                else:
                                    print("Error: los datos no pudieron guardarse.")
                            else:
                                print("Error: los datos no pudieron guardarse.")
                            
                            input("Presione Enter para continuar...")
                        else:
                            input("Presione Enter para continuar...")
                    else:
                        input("El usuario no fue encontrado o la ID coincide con el usuario autenticado.\nPresione Enter para continuar...")
                case 11:
                    self.generar_reporte_usuarios_morosos()
                    input("Presione Enter para continuar...")
                case 12:
                    self.generar_top_5_recursos_prestados()
                    input("Presione Enter para continuar...")
                case 13:
                    print("Sesión cerrada.")
                    self.usuario_autenticado = None

    def eliminar_usuario(self, user:Usuario, pos):
        """
        Este método permite eliminar un usuario existente, siempre y cuando 
        NO haya multas o préstamos activos para ese usuario. 
        Este método da solución al requerimiento 10 del análisis del problema.

        PARÁMETEROS:
        usuario = Usuario (Que es el usuario a eliminar)
        pos -> pos_usuario (variable que almacena la posición del usuario)

        RETORNO:
        Booleano

        Autor: Mateo Daniel Galeano Quiñones 30/06/2025
        """

        print("*"*16)
        print("ELIMINAR USUARIO")
        print("*"*16)

        usuario_a_eliminar = user
        i = int
        eliminacion_exitosa = False
        
        #Primero, se muestra la información del usuario.
        usuario_a_eliminar.mostrar_informacion()

        #Se verifica que el usuario no tenga multas activas, en caso de que tenga retornar la variable eliminacion_exitosa que almacena el valor de False
        if (usuario_a_eliminar.numero_de_multas == 0):
            #Se verifica que el usuario no tenga prestamos activos, en caso de que los tenga retornar la variable eliminacion_exitosa que almacena el valor de False
            for i in range(self.numero_de_prestamos_activos):
                if (usuario_a_eliminar.id == self.prestamos_activos[i].titular_del_prestamo.id):
                    print("No se puede eliminar al usuario debido a que tiene préstamos activos.")
                    return eliminacion_exitosa

            
            
            #Si el usuario cumple con las condiciones para ser eliminado, se borran los préstamos inactivos a nombre del usuario:
            i = 0
            while (i <= (self.numero_de_prestamos_inactivos - 1)):
                if (self.prestamos_inactivos[i].titular_del_prestamo.id == usuario_a_eliminar.id):
                    self.prestamos_inactivos[i] = None
                    for j in range ((i+1), self.numero_de_prestamos_inactivos):
                        self.prestamos_inactivos[j-1] = self.prestamos_inactivos[j]

                    self.prestamos_inactivos[self.numero_de_prestamos_inactivos - 1] = None
                    self.numero_de_prestamos_inactivos -= 1
                else:
                    i += 1


            for i in range(pos + 1, self.numero_de_usuarios):
                self.total_de_usuarios[i - 1] = self.total_de_usuarios[i]

            #Se asigna el valor de None al usuario en la posicion numero_de_usuarios - 1 del arreglo total de usuarios
            self.total_de_usuarios[self.numero_de_usuarios - 1] = None
            self.numero_de_usuarios -= 1

            eliminacion_exitosa = True
            print("Usuario eliminado exitosamente.")
            return eliminacion_exitosa
        else:
            print("El usuario no puede eliminarse porque tiene multas activas.")
            return eliminacion_exitosa
        
    def historial_prestamos_recurso(self, recurso:Recurso):
        """
        Este método muestra el historial de préstamos de un recurso 
        en específicico
        Este método da solución al requerimiento 7 del análisis del problema.

        PARÁMETEROS:
        recurso = Recurso (Recurso del cuál queremos mostrar su historial, esto por medio de su signatura topográfica)

        RETORNO:
        Vacío

        Autor: Mateo Daniel Galeano Quiñones 02/07/2025
        """

        print("*"*32)
        print("HISTORIAL DE PRÉSTAMOS DEL RECURSO")
        print("*"*32)

        contador_de_prestamos = int
        contador_de_prestamos = 0
        i = int
        #Se muestra la información del recurso
        recurso.mostrar_informacion()

        #Se recorre el arreglo de préstamos activos y se muestra la información del préstamo con la misma signatura topográfica del recurso ingresado
        for i in range(self.numero_de_prestamos_activos):
            if (recurso.signatura_topografica == self.prestamos_activos[i].recurso_prestado.signatura_topografica):
                self.prestamos_activos[i].mostrar_informacion(para_el_usuario = False)
                print("En prestamo actualmente\n") #Se indica que el recurso está en préstamo actualmente

        #Se recorre el arreglo de préstamos inactivos y se muestra la información de los préstamos con la misma signatura topográfica del recurso ingresado
        for i in range(self.numero_de_prestamos_inactivos - 1, -1, -1):
            if (self.prestamos_inactivos[i] != None):
                if (recurso.signatura_topografica == self.prestamos_inactivos[i].recurso_prestado.signatura_topografica):
                    self.prestamos_inactivos[i].mostrar_informacion(para_el_usuario = False)
                    contador_de_prestamos += 1
                    print("\n")
                
        if (contador_de_prestamos == 0):
            print("El historial de préstamos de este recurso se encuentra actualmente vacío.")

    def mostrar_historial_usuario (self, user:Usuario):
        """
            Este método permite mostrar el historial de préstamos de un usuario.
            Este método da solución al requerimiento 8 del análisis del problema.

            PARÁMETEROS:
            user: Usuario cuyo historial de préstamos será mostrado.

            RETORNO:
            Ninguno.

            Autor: Daniel Sánchez Escobar 1/07/2025
        """
        #variables
        usuario = user
        numero_de_prestamos = int
        numero_de_prestamos = 0
        i = int
        sign_recursos_con_multa = np.ndarray

        #Se verifica si el usuario tiene multas activas
        if (usuario.numero_de_multas > 0):
            #Se crea un arreglo auxiliar donde se guardarán las signaturas de los recursos con los que el usuario tiene multa activa.
            sign_recursos_con_multa = np.full((usuario.numero_de_multas), fill_value="",dtype=object)

            for i in range (len(sign_recursos_con_multa)):
                sign_recursos_con_multa[i] = usuario.multas_vigentes[i].recurso_con_multa.signatura_topografica
            
            #Una vez llenado, se comienza el recorrido del arreglo de préstamos inactivos
            for i in range((self.numero_de_prestamos_inactivos-1),-1,-1):
                if(self.prestamos_inactivos[i].titular_del_prestamo.id == usuario.id):

                    #Muestra la info. normal del préstamo
                    self.prestamos_inactivos[i].mostrar_informacion()
                    #Aumenta el contador
                    numero_de_prestamos += 1

                    """Se verifica si el préstamo que se está analizando tiene como recurso asociado
                    aquel con signatura topográfica igual a alguna de las signaturas almacenadas
                    en el arreglo auxiliar de recursos asociados a las multas activas del usuario"""
                    for j in range(len(sign_recursos_con_multa)):
                        if (self.prestamos_inactivos[i].recurso_prestado.signatura_topografica == sign_recursos_con_multa[j]):
                            #Busca la multa que está asociada a ese recurso
                            
                            #Si se da el caso de que la signatura del recurso está incluida en el arreglo auxiliar
                            #Se busca la multa asociada y se muestra su valor adeudado como información adicional
                            for k in range(usuario.numero_de_multas):
                                if (usuario.multas_vigentes[k].recurso_con_multa.signatura_topografica == self.prestamos_inactivos[i].recurso_prestado.signatura_topografica):
                                    print(f"Valor adeudado por multa: ${usuario.multas_vigentes[k].valor_adeudado}")
                                    break
                            
                            #Una vez mostrado el valor adeudado de la multa, se elimina la signatura del arreglo auxiliar
                            """El objetivo detrás de eliminar la signatura del arreglo auxiliar radica en
                            evitar que, si el usuario tiene varios préstamos devueltos sobre el mismo recurso,
                            no se reflejen multas sobre esos préstamos pasados"""
                            sign_recursos_con_multa[j] = ""
                            break
            
            if (numero_de_prestamos == 0):
                print("El historial de préstamos de este usuario se encuentra vacío actualmente.")
        else:
            #Si el usuario no tiene multas, se muestran los préstamos a su nombre
            #Se recorre el arreglo de préstamos inactivos, de derecha a izquierda
            for i in range((self.numero_de_prestamos_inactivos - 1), -1, -1):
                #Se verifica si el préstamo inactivo tiene como titular al usuario, si se cumple, se muestra:
                if (self.prestamos_inactivos[i].titular_del_prestamo.id == usuario.id):
                    self.prestamos_inactivos[i].mostrar_informacion()
                    numero_de_prestamos += 1
            
            #Si al finalizar el recorrido, el contador permanece en cero, entonces el historial está vacío
            if (numero_de_prestamos == 0):
                print("El historial de préstamos de este usuario se encuentra vacío actualmente.")

    def modificar_usuario (self, user:Usuario, modificacion_de_administrador = True):
        """
        Este método permite modificar la información de un usuario existente.
        La información que permite modificarse depende del usuario en cuestión,
        un administrador modificando la información de un usuario puede eliminar
        las multas de dicho usuario (si las tiene), siempre y cuando NO haya 
        multas o préstamos activos para ese usuario.
        Este método da solución al requerimiento 9 del análisis del problema.

        PARÁMETEROS:
        usuario = Usuario (Que es el usuario a modificar)
        modificacion_de_administrador (Que permite identificar si es un administrador el que está modificando la info. de un usuario.)

        RETORNO:
        Booleano

        Autor: Mateo Daniel Galeano Quiñones 27/06/2025
        """
        print("*"*32)
        print("MODIFICAR INFORMACIÓN DE USUARIO")
        print("*"*32)
        #Se declaran las variables locales al método
        usuario_a_modificar = user
        i = int
        modificacion_exitosa = False

        #El siguiente bloque de instrucciones permite modificar la información del usuario si lo hace un administrador
        if (modificacion_de_administrador):

            while (True):
                usuario_a_modificar.mostrar_informacion()

                # Se declaran las variables para que el usuario elija qué va a modificar
                decision = int
                decision = 0
                opcion = int
                opcion = 0

                print("Seleccione el atributo a modificar del usuario, indicando el número correspondiente.")
                print("1.Nombre.")
                print("2.Dirección de residencia.")
                print("3.Número telefónico.")
                print("4.Correo electrónico.")
                print("5.Código.")
                print("6.Número de identificación.")
                print("7.Eliminar multa.")
                decision = leer_entero(1, 7, "Ingrese su selección aquí: ")

                match (decision):
                    case 1:
                        usuario_a_modificar.nombre_usuario = verificar_si_esta_vacio("Escriba el nuevo nombre del usuario: ")
                    case 2:
                        usuario_a_modificar.direccion_residencia = verificar_si_esta_vacio("Escriba la nueva dirección de residencia: ")
                    case 3:
                        usuario_a_modificar.telefono = leer_entero_no_acotado("Esciba el nuevo número telefónico: ")
                    case 4:
                        usuario_a_modificar.email = verificar_email("Escriba el nuevo email: ")
                    case 5:
                        nuevo_codigo = str
                        existe_un_codigo_igual = True
                        while (existe_un_codigo_igual):
                            existe_un_codigo_igual = False
                            nuevo_codigo = verificar_cadena_alfanumerica("Escriba el nuevo código: ")
                            for i in range (self.numero_de_usuarios):
                                if (nuevo_codigo == self.total_de_usuarios[i].codigo):
                                    print("El código ingresado ya está en uso. Ingrese otro código.")
                                    existe_un_codigo_igual = True
                        
                        #Si el código ingresado no está repetido, entonces se asigna al atributo codigo
                        usuario_a_modificar.codigo = nuevo_codigo
                    case 6:
                        nuevo_id = int
                        existe_un_id_igual = True
                        while (existe_un_id_igual):
                            existe_un_id_igual = False
                            nuevo_id = leer_entero_no_acotado("Escriba el nuevo ID del usuario: ")
                            for i in range (self.numero_de_usuarios):
                                if (nuevo_id == self.total_de_usuarios[i].id):
                                    print("El ID ingresado ya está en uso. Ingrese otro ID.")
                                    existe_un_id_igual = True
                        
                        #Si el ID ingresado no está repetido, entonces se asigna al atributo id
                        usuario_a_modificar.id = nuevo_id

                    case 7:
                    
                        i = int
                        total_de_multas = int
                        total_de_multas = 0
                        print("***MULTAS***")

                        #Se verifica que el usuario tenga multas
                        if (usuario_a_modificar.numero_de_multas > 0):

                            #Se recorre el arreglo de multas del usuario y se muestran las multas que tiene

                            for i in range (usuario_a_modificar.numero_de_multas):
                                print(f"Multa #{i+1}:")
                                usuario_a_modificar.multas_vigentes[i].mostrar_informacion()
                                total_de_multas += 1
                            
                            #Esta variable permite elegir la multa a eliminar
                            opcion = leer_entero(1, total_de_multas, "Seleccione la multa que desea eliminar: ")
                            
                            #Se elimina la multa moviendo los elementos hacia la izquierda, desde la posición de la multa + 1
                            opcion -= 1
                            for i in range ((opcion + 1), usuario_a_modificar.numero_de_multas):
                                usuario_a_modificar.multas_vigentes[i-1] = usuario_a_modificar.multas_vigentes[i]
                            
                            usuario_a_modificar.multas_vigentes[usuario_a_modificar.numero_de_multas-1] = None
                            usuario_a_modificar.numero_de_multas -= 1
                        else:
                            print("Este usuario no tiene multas.")
                        
                
                continuar = leer_entero(1, 2, "¿Desea modificar otro dato del usuario? 1.Si 2.No: ")
                if (continuar == 2):
                    modificacion_exitosa = True
                    break

            return modificacion_exitosa
        else:
            #Este bloque de instrucciones permite desplegar las opciones que un usuario puede modificar se su propia información

            while (True):
                usuario_a_modificar.mostrar_informacion()

                # Se declaran las variables para que el usuario elija qué modificar
                decision = int
                decision = 0
                opcion = int
                opcion = 0

                print("Seleccione el atributo a modificar del usuario, indicando el número correspondiente.")
                print("1.Nombre.")
                print("2.Dirección de residencia.")
                print("3.Número telefónico.")
                print("4.Correo electrónico.")
                print("5.Código.")
                print("6.Número de identificación.")

                decision = leer_entero(1, 6, "Ingrese su selección aquí: ")

                match (decision):
                    case 1:
                        usuario_a_modificar.nombre_usuario = verificar_si_esta_vacio("Escriba el nuevo nombre del usuario: ")
                    case 2:
                        usuario_a_modificar.direccion_residencia = verificar_si_esta_vacio("Escriba la nueva dirección de residencia: ")
                    case 3:
                        usuario_a_modificar.telefono = leer_entero_no_acotado("Esciba el nuevo número telefónico: ")
                    case 4:
                        usuario_a_modificar.email = verificar_email("Escriba el nuevo email: ")
                    case 5:
                        nuevo_codigo = str
                        existe_un_codigo_igual = True
                        while (existe_un_codigo_igual):
                            existe_un_codigo_igual = False
                            nuevo_codigo = verificar_cadena_alfanumerica("Escriba el nuevo código: ")
                            for i in range (self.numero_de_usuarios):
                                if (nuevo_codigo == self.total_de_usuarios[i].codigo):
                                    print("El código ingresado ya está en uso. Ingrese otro código.")
                                    existe_un_codigo_igual = True
                        
                        #Si el código ingresado no está repetido, entonces se asigna al atributo codigo
                        usuario_a_modificar.codigo = nuevo_codigo
                    case 6:
                        nuevo_id = int
                        existe_un_id_igual = True
                        while (existe_un_id_igual):
                            existe_un_id_igual = False
                            nuevo_id = leer_entero_no_acotado("Escriba el nuevo ID del usuario: ")
                            for i in range (self.numero_de_usuarios):
                                if (nuevo_id == self.total_de_usuarios[i].id):
                                    print("El ID ingresado ya está en uso. Ingrese otro ID.")
                                    existe_un_id_igual = True
                        
                        #Si el ID ingresado no está repetido, entonces se asigna al atributo id
                        usuario_a_modificar.id = nuevo_id
                
                continuar = leer_entero(1, 2, "¿Desea modificar otro dato del usuario? 1.Si 2.No: ")
                if (continuar == 2):
                    modificacion_exitosa = True
                    break
            
            return modificacion_exitosa

    def registrar_prestamo (self, usuario:Usuario, recurso):
            """
                Este método permite registrar un préstamo y da solución al requerimiento 5 del análisis del problema.

                PARÁMETEROS:
                usuario = Usuario
                recurso = Recurso

                RETORNO:
                obj = Prestamo

                Autor: Daniel Sánchez Escobar 25/06/2025
            """

            #Se declaran las variables locales al método
            objeto = Prestamo
            objeto = None
            usuario_que_realiza_el_prestamo = usuario
            recurso_a_prestar = recurso
            contador_de_prestamos, i = int, int
            contador_de_prestamos = 0
            prestamos_vencidos = int
            prestamos_vencidos = 0
            
            #Se cuentan los préstamos que estén activos y su titular sea el usuario a realizar el préstamo
            #Adicionalmente, se verifica si hay algún préstamo vencido
            for i in range (len(self.prestamos_activos)):
                if (self.prestamos_activos[i] != None):
                    if (self.prestamos_activos[i].titular_del_prestamo.id == usuario_que_realiza_el_prestamo.id):
                        contador_de_prestamos += 1
                    
                    if (self.prestamos_activos[i].verificar_dias_de_mora() != 0):
                        prestamos_vencidos += 1

            #Se hacen las verificaciones
            #Se verifica que el usuario tenga menos de 5 préstamos
            if (contador_de_prestamos < 5):

                #Se verifica que el usuario sea un estudiante o un empleado
                if (usuario_que_realiza_el_prestamo.tipo_de_usuario == Usuario.PERFIL_ESTUDIANTE or usuario_que_realiza_el_prestamo.tipo_de_usuario == Usuario.PERFIL_EMPLEADO):

                    #Se verifica que el recurso esté disponible
                    if (recurso_a_prestar.estado == "DISPONIBLE"):

                        #Se verifica que no haya ningún préstamo vigente y vencido asociado al usuario
                        if (prestamos_vencidos == 0):

                            #Se verifica que no tenga multas
                            if (usuario_que_realiza_el_prestamo.numero_de_multas == 0):

                                #Una vez realizadas todas las verificaciones, se crea el objeto préstamo y se asigna
                                #el tiempo en días permitido para el préstamo, según el perfil y la colección
                                #luego se guarda en el arreglo de préstamos activos
                                if (usuario_que_realiza_el_prestamo.tipo_de_usuario == Usuario.PERFIL_ESTUDIANTE):
                                    if (recurso_a_prestar.coleccion == "GENERAL"):
                                        objeto = Prestamo(usuario_que_realiza_el_prestamo, recurso_a_prestar, 15)
                                        self.prestamos_activos[self.numero_de_prestamos_activos] = objeto
                                        self.numero_de_prestamos_activos += 1
                                    elif (recurso_a_prestar.coleccion == "RESERVA"):
                                        objeto = Prestamo(usuario_que_realiza_el_prestamo, recurso_a_prestar, 1)
                                        self.prestamos_activos[self.numero_de_prestamos_activos] = objeto
                                        self.numero_de_prestamos_activos += 1
                                    elif (recurso_a_prestar.coleccion == "HEMEROTECA"):
                                        objeto = Prestamo(usuario_que_realiza_el_prestamo, recurso_a_prestar, 3)
                                        self.prestamos_activos[self.numero_de_prestamos_activos] = objeto
                                        self.numero_de_prestamos_activos += 1
                                    recurso_a_prestar.estado = "PRESTADO"
                                elif (usuario_que_realiza_el_prestamo.tipo_de_usuario == Usuario.PERFIL_EMPLEADO):
                                    if (recurso_a_prestar.coleccion == "GENERAL"):
                                        objeto = Prestamo(usuario_que_realiza_el_prestamo, recurso_a_prestar)
                                        self.prestamos_activos[self.numero_de_prestamos_activos] = objeto
                                        self.numero_de_prestamos_activos += 1
                                    elif (recurso_a_prestar.coleccion == "RESERVA"):
                                        objeto = Prestamo(usuario_que_realiza_el_prestamo, recurso_a_prestar, 15)
                                        self.prestamos_activos[self.numero_de_prestamos_activos] = objeto
                                        self.numero_de_prestamos_activos += 1
                                    elif (recurso_a_prestar.coleccion == "HEMEROTECA"):
                                        objeto = Prestamo(usuario_que_realiza_el_prestamo, recurso_a_prestar, 22)
                                        self.prestamos_activos[self.numero_de_prestamos_activos] = objeto
                                        self.numero_de_prestamos_activos += 1
                                    recurso_a_prestar.estado = "PRESTADO"

                            else:
                                print("El usuario tiene multas activas.")
                        else:
                            print("El usuario tiene préstamos vencidos sin devolver.")
                    else:
                        print("El recurso no se encuentra disponible en este momento.")
                else:
                    print("El usuario no es estudiante o empleado.")
            else:
                print("El usuario ha alcanzado el límite de préstamos simultáneos.")
            
            return objeto

    def devolver_prestamo (self, user:Usuario):
        """
            Este método permite realizar la devolución de un préstamo.
            Este método da solución al requerimiento 6 del análisis del problema.

            PARÁMETEROS:
            user: Usuario que realiza la devolución del préstamo

            RETORNO:
            Booleano, True si la devolución tuvo éxito y False si fracasó.

            Autor: Daniel Sánchez Escobar 30/06/2025
        """
        #Variables
        usuario = user #Se almacena al usuario que realiza la devolución
        contador_de_prestamos = int #Cuenta los préstamos que están a nombre del usuario
        contador_de_prestamos = 0
        i = int
        j = int
        arr_aux = np.ndarray #Arreglo auxiliar donde se almacenarán los préstamos del usuario
        decision = int #Para almacenar qué préstamo desea devolver el usuario
        hay_multa = bool #Para identificar si existe una multa por la devolución

        #Se recorre el arreglo de préstamos activos, en búsqueda de los préstamos que pertenecen al usuario
        for i in range (len(self.prestamos_activos)):
            if (self.prestamos_activos[i] != None):
                if (self.prestamos_activos[i].titular_del_prestamo.id == usuario.id):
                    contador_de_prestamos += 1

        #Se verifica si el contador permanece en cero o es mayor a cero tras el recorrido
        if (contador_de_prestamos > 0):
            #Se inicializa el arreglo de objetos, con tamaño dado por el contador de préstamos
            arr_aux = np.full((contador_de_prestamos), fill_value=None, dtype=object)

            #Se recorre de nuevo el arreglo de préstamos activos, para asignar al arreglo auxiliar los préstamos del usuario
            j = 0 #Para controlar el índice del arreglo auxiliar
            for i in range (len(self.prestamos_activos)):
                if (self.prestamos_activos[i] != None):
                    if (self.prestamos_activos[i].titular_del_prestamo.id == usuario.id):
                        arr_aux [j] = self.prestamos_activos[i]
                        j += 1
            
            #Tras finalizar el llenado del arreglo auxiliar, se muestra su información a modo de menú:
            for i in range (len(arr_aux)):
                print(f"** PRÉSTAMO #{i+1} **")
                print(f"Título del recurso: {arr_aux[i].recurso_prestado.titulo}")
                print(f"Signatura Topográfica: {arr_aux[i].recurso_prestado.signatura_topografica}")
                print(f"Fecha de generación del préstamo: {arr_aux[i].fecha_de_prestamo}")
                print(f"Titular del préstamo: {arr_aux[i].titular_del_prestamo.nombre_usuario}")
                print(f"ID del titular: {arr_aux[i].titular_del_prestamo.id}")
            
            #Se pide al usuario que elija cuál préstamo desea devolver
            decision = leer_entero(1, contador_de_prestamos, "\nEscriba el número del préstamo que desea devolver aquí: ")
            #Se resta 1 a la variable para usarla como índice en el arreglo auxiliar
            decision -= 1

            arr_aux[decision].recurso_prestado.estado = "DISPONIBLE" #El atributo estado pasa a DISPONIBLE

            #Se recorre el arreglo de recursos, y se busca el recurso que es titular de ese préstamo
            for i in range (len(self.inventario_de_recursos)):
                if (self.inventario_de_recursos[i] != None):
                    if (self.inventario_de_recursos[i].signatura_topografica == arr_aux[decision].recurso_prestado.signatura_topografica):
                        self.inventario_de_recursos[i].estado = "DISPONIBLE"
                        break

            arr_aux[decision].fecha_de_devolucion = date.today() #Se genera la fecha de devolución

            #Seguidamente, el préstamo debe ser transferido al arreglo de préstamos inactivos.

            #Primero, se debe verificar que el arreglo no esté lleno

            if (self.numero_de_prestamos_inactivos < self.MAX_PRESTAMOS_INACTIVOS):
                #Si el arreglo no está lleno, simplemente se asigna el nuevo préstamo finalizado
                self.prestamos_inactivos[self.numero_de_prestamos_inactivos] = arr_aux[decision]
                self.numero_de_prestamos_inactivos += 1
            else:
                #Si el arreglo está lleno, se elimina el primer préstamo inactivo del arreglo, para hacer espacio
                self.prestamos_inactivos[0] = None
                for i in range(1, self.numero_de_prestamos_inactivos):
                    self.prestamos_inactivos[i-1] = self.prestamos_inactivos[i]
                
                self.prestamos_inactivos[self.numero_de_prestamos_inactivos - 1] = None
                self.numero_de_prestamos_inactivos -= 1

                #Después de realizar la eliminación, se procede a registrar el nuevo préstamo inactivo

                self.prestamos_inactivos[self.numero_de_prestamos_inactivos] = arr_aux[decision]
                self.numero_de_prestamos_inactivos += 1
            
            #Una vez registrado el préstamo en el arreglo de préstamos inactivos, se verifica si hay multa
            if (arr_aux[decision].verificar_dias_de_mora(arr_aux[decision].fecha_de_devolucion) != 0):
                
                #Si el número de días de mora es diferente a cero, se hace el cálculo de nuevo y se almacena
                dias_de_mora = int
                dias_de_mora = arr_aux[decision].verificar_dias_de_mora(arr_aux[decision].fecha_de_devolucion)
                # Se crea un objeto multa, guardándolo en el arreglo de multas del usuario
                usuario.multas_vigentes[usuario.numero_de_multas] = Multa(dias_de_mora*1000, arr_aux[decision].fecha_de_devolucion, arr_aux[decision].recurso_prestado)
                usuario.numero_de_multas +=1
                hay_multa = True
            else:
                #Si el número de días de mora es cero, entonces simplemente no hay multa
                hay_multa = False

            #Se elimina la instancia del préstamo del arreglo de préstamos activos

            posicion_del_prestamo = int #Denota la posición del préstamo en el arreglo de préstamos activos

            #Se recorre de nuevo el arreglo de préstamos activos
            #Y se busca, por signatura del recurso, el préstamo que se está devolviendo
            for i in range (len(self.prestamos_activos)):
                if (self.prestamos_activos[i] != None):
                    if (arr_aux[decision].recurso_prestado.signatura_topografica == self.prestamos_activos[i].recurso_prestado.signatura_topografica):
                        posicion_del_prestamo = i
                        break
            
            #Una vez obtenida la posición, se procede a realizar la eliminación
            self.prestamos_activos[posicion_del_prestamo] = None
            for i in range((posicion_del_prestamo + 1), self.numero_de_prestamos_activos):
                self.prestamos_activos[i-1] = self.prestamos_activos[i]
            
            self.prestamos_activos[self.numero_de_prestamos_activos - 1] = None
            self.numero_de_prestamos_activos -= 1

            #Finalmente, se muestra el mensaje que indica la devolución exitosa y la multa, si hay

            print("El recurso fue devuelto exitosamente.")
            if (hay_multa):
                print("Se ha generado una multa:")
                usuario.multas_vigentes[usuario.numero_de_multas - 1].mostrar_informacion()
            else:
                print("No se ha generado multa.")
            
            return True
        else:
            return False

    def generar_reporte_usuarios_morosos(self):
        """
        Este método muestra los usuarios morosos 
        
        Este método da solución al requerimiento 12 del análisis del problema.

        PARÁMETEROS:
        Ninguno

        RETORNO:
        Vacío

        Autor: Daniel Sánchez Escobar 02/07/2025
        """

        i = int
        dias_de_mora = int
        numero_de_usuarios_morosos = int
        numero_de_usuarios_morosos = 0

        for i in range(self.numero_de_prestamos_activos):
            if (self.prestamos_activos[i].verificar_dias_de_mora(date.today()) != 0):
                dias_de_mora = self.prestamos_activos[i].verificar_dias_de_mora(date.today())
                print(f"Nombre del titular: {self.prestamos_activos[i].titular_del_prestamo.nombre_usuario}")
                print(f"ID del titular: {self.prestamos_activos[i].titular_del_prestamo.id}")
                print(f"Recurso: {self.prestamos_activos[i].recurso_prestado.titulo}")
                print(f"Signatura topográfica: {self.prestamos_activos[i].recurso_prestado.signatura_topografica}")
                print(f"Días de mora: {dias_de_mora} | Valor adeudado: ${dias_de_mora * 1000}")
                numero_de_usuarios_morosos += 1

        if (numero_de_usuarios_morosos == 0):
            print("Actualmente no hay usuarios morosos.")

    def generar_top_5_recursos_prestados(self):
        """
            Este método permite generar un reporte del top 5 de recursos más prestados de la biblioteca,
            muestra el nombre del recurso, número de inventario y el número de veces prestado.
            Este método permite dar solución al requerimiento 11 del análisis del problema.

            PARÁMETEROS:
            NINGUNO

            RETORNO:
            NINGUNO

            Autor: Daniel Sánchez Escobar 3/07/2025
        """
        #Variables
        arr_recursos_copia = np.ndarray
        contador = np.ndarray
        veces_prestado = int
        #Se verifica que el arreglo de recursos si tenga recursos registrados
        if (self.numero_de_recursos > 0):
            arr_recursos_copia = self.inventario_de_recursos.copy()
            contador = np.full((len(arr_recursos_copia)), fill_value=0,dtype=int)

            for i in range(len(arr_recursos_copia)):
                if (arr_recursos_copia[i] != None):
                    veces_prestado = 0

                    for j in range (self.numero_de_prestamos_activos):
                        if (self.prestamos_activos[j].recurso_prestado.signatura_topografica == arr_recursos_copia[i].signatura_topografica):
                            veces_prestado += 1
                    
                    for j in range (self.numero_de_prestamos_inactivos):
                        if (self.prestamos_inactivos[j].recurso_prestado.signatura_topografica == arr_recursos_copia[i].signatura_topografica):
                            veces_prestado += 1
                    
                    contador[i] = veces_prestado
            
            #Una vez terminado el conteo, se organizan los arreglos por selección
            for i in range (len(contador)-1):
                for j in range((i+1), len(contador)):
                    if (contador[i] < contador[j]):
                        aux = contador[i]
                        contador[i] = contador[j]
                        contador[j] = aux

                        aux = arr_recursos_copia[i]
                        arr_recursos_copia[i] = arr_recursos_copia[j]
                        arr_recursos_copia[j] = aux
            
            #Finalmente, se muestran los primeros 5 recursos

            i = 0
            while (i <= 4):
                if (arr_recursos_copia[i] != None):
                    print("*************************************************************")
                    print(f"Número de inventario: {arr_recursos_copia[i].num_inventario}")
                    print(f"Título: {arr_recursos_copia[i].titulo}")
                    print(f"Veces prestado: {contador[i]}")
                i+=1
        else:
            print("Actualmente no hay recursos registrados en la biblioteca.")

    def buscar_usuario_por_id (self, identificacion):
        """
            Este método permite buscar a un usuario por medio de su número de identificación (id), 
            se utiliza como método auxiliar para la solución del requerimiento 13 del análisis del problema.

            PARÁMETEROS:
            identificacion: id del usuario a buscar

            RETORNO:
            Entero

            Autor: Daniel Sánchez Escobar 25/06/2025
        """
        #Declaración de variables
        i = int
        pos = int
        pos = -1
        
        #El ciclo recorre el arreglo de usuarios, una vez encuentre un id igual al que se busca, lo almacena en pos
        #Y rompe el ciclo
        for i in range (self.numero_de_usuarios):
            if (self.total_de_usuarios[i].id == identificacion):
                pos = i
                break
        
        #Retorna la posición del usuario en el arreglo
        return pos

    def buscar_recurso_por_signatura (self, signatura):
        """
            Este método permite buscar a un recurso por medio de su signatura topográfica, 
            se utiliza como método auxiliar para la solución del requerimiento 13 del análisis del problema.

            PARÁMETEROS:
            signatura: signatura topográfica del recurso a buscar

            RETORNO:
            Entero

            Autor: Daniel Sánchez Escobar 25/06/2025
        """
        #Declaración de variables
        i = int
        pos = int
        pos = -1

        #El ciclo recorre el arreglo de recursos, una vez encuentre una signatura igual a la ingresada como
        #párametro, almacena la posición en pos y rompe el ciclo
        for i in range (self.numero_de_recursos):
            if (self.inventario_de_recursos[i].signatura_topografica == signatura):
                pos = i
                break
        
        #Retorna la posición
        return pos


    def main (self):
        decision = int
        decision = 0
        while (decision != 3):
            decision = leer_entero(1, 3, "*****SISTEMA DE BIBLIOTECA-MENÚ PRINCIPAL*****\nSeleccione una opción:\n1.Registrarse.\n2.Autenticarse.\n3.Finalizar el programa.\n")
            match decision:
                case 1:
                    if (self.numero_de_usuarios < self.MAX_USUARIOS):
                        print("********\nREGISTRO\n********")
                        decision = leer_entero (1, 2, "Indique su perfil:\n1.ESTUDIANTE.\n2.EMPLEADO.")
                        if (decision == 1):
                            if (self.registrar_usuario()):
                                ##PUNTO DE GUARDADO###
                                if (self.guardar_datos(self.total_de_usuarios, self.ARCHIVO_USUARIOS)):
                                    print("Guardado de datos exitoso.")
                                else:
                                    print("Error: no se pudo realizar el guardado de datos.")
                        else:
                            if (self.registrar_usuario()):
                                self.total_de_usuarios[self.numero_de_usuarios-1].tipo_de_usuario = Usuario.PERFIL_EMPLEADO
                                ##PUNTO DE GUARDADO###
                                if (self.guardar_datos(self.total_de_usuarios, self.ARCHIVO_USUARIOS)):
                                    print("Guardado de datos éxitoso.")
                                else:
                                    print("Error: no se pudo realizar el guardado de datos.")
                        
                        input("Presione Enter para continuar...")
                    else:
                        input("No hay espacio para registrar nuevos usuarios.\nPresione Enter para continuar...")
                
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