#CODIFICACIÓN DE LA CLASE USUARIO-AUTOR: MATEO GALEANO 29/05/2025
from funciones_para_verificar import *
import numpy as np
class Usuario:
    """
    Esta clase almacena la información de un usuario que es su nombre, dirección de residencia, teléfono,
    email, código, tipo (o sea su perfil) y la multa vigente (cuyos detalles
    se tratarán en la siguiente entrega del proyecto)
    Además, hay algunos atributos ocultos para el manejo de perfiles de usuario y el máximo de multas que pueden almacenarse.

    ATRIBUTOS:
    nombre_usuario: que es el nombre del usuario.
    direccion_residencia: que es la direccíon donde vive el usuario.
    telefono: que es el número de telefono del usuario.
    email: que es el correo electrónico del usuario.
    código: que es el código que identifica al usuario y le permite autenticarse e ingresar al sistema.
    tipo_de_usuario: que es el perfil del usuario (ESTUDIANTE, ADMINISTRADOR, BIBLIOTECARIO, EMPLEADO).
    multas_vigentes: que contiene las multas del usuario.
    id: que se refiere a la identificación del usuario.
    numero_de_multas: que es un contador el cuál indica el número de multas que tiene el usuario actualmente.

    CONSTANTES:
    PERFIL_ADMIN: contiene la constante que identifica a un usuario con perfil normal
    PERFIL_BIBLIOTECARIO: contiene la constante que identifica a un usuario con perfil bibliotecario.
    PERFIL_EMPLEADO: contiene la constante que identifica a un usuario con perfil empleado.
    PERFIL_ESTUDIANTE: contiene la constante que identifica a un usuario con perfil estudiante.
    MAX_MULTAS: contiene la constante que indica el número máximo de multas que pueden ser almacenadas para un usuario.
    """
    #ATRIBUTOS
    nombre_usuario = str
    direccion_residencia = str
    telefono = int
    email = str
    codigo = str
    tipo_de_usuario = str
    id = int
    multas_vigentes = np.ndarray
    numero_de_multas = int

    #CONSTANTES
    PERFIL_ADMIN = "ADMINISTRADOR"
    PERFIL_BIBLIOTECARIO = "BIBLIOTECARIO"
    PERFIL_EMPLEADO = "EMPLEADO"
    PERFIL_ESTUDIANTE = "ESTUDIANTE"
    MAX_MULTAS = 5

    #CONSTRUCTOR DE LA CLASE: POR DEFECTO EL USUARIO ES ESTUDIANTE
    def __init__ (self, nombre_usuario = None, direccion_residencia = None, telefono = None, email = None, codigo = None, id = None):
        self.nombre_usuario = nombre_usuario
        self.direccion_residencia = direccion_residencia
        self.telefono = telefono
        self.email = email
        self.codigo = codigo
        self.tipo_de_usuario = self.PERFIL_ESTUDIANTE
        self.id = id
        self.multas_vigentes = np.full((self.MAX_MULTAS), fill_value = None, dtype=object)
        self.numero_de_multas = 0
   
    #ESTE MÉTODO PIDE POR CONSOLA LOS DATOS BÁSICOS DEL USUARIO
    def pedir_datos (self):
        self.nombre_usuario = verificar_si_esta_vacio("Ingrese su nombre: ")
        self.id = leer_entero_no_acotado("Ingrese su número de identificación: ")
        self.direccion_residencia = verificar_si_esta_vacio("Ingrese la dirección de su residencia: ")
        self.telefono = leer_entero_no_acotado("Ingrese su número telefónico: ")
        self.email = verificar_email("Ingrese su dirección de correo electrónico: ")
        self.codigo = verificar_cadena_alfanumerica("Crea tu código de usuario: ")

    #ESTE MÉTODO SE ENCARGA DE MOSTRAR LA INFORMACIÓN BÁSICA DEL USUARIO
    def mostrar_informacion (self):
        print("## INFORMACIÓN DEL USUARIO ##")
        print(f"Nombre: {self.nombre_usuario}")
        print(f"Dirección: {self.direccion_residencia}")
        print(f"Teléfono: {self.telefono}")
        print(f"Email: {self.email}")
        print(f"Código: {self.codigo}")
        print(f"Tipo de usuario: {self.tipo_de_usuario}")
        print(f"Identificación: {self.id}")
        print(f"Multas activas: {self.numero_de_multas}")