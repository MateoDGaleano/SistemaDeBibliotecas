from datetime import date
from ClaseUsuario import *
from ClaseRecurso import *
from ClaseLibro import *
from ClaseAudio import *
from ClaseRevista import *
from ClaseVideo import *
class Prestamo:
    """
    Esta clase representa un préstamo  y se encarga de crear el objeto, almacenar los datos del préstamo y mostrar
    la información del mismo.

    ATRIBUTOS:
    tiempo_maximo_permitido: almacena la cantidad máxima de tiempo en días del préstamo.
    titular_del_prestamo: que almacena al usuario titular del préstamo.
    recurso_prestado: que almacena el recurso asociado a ese préstamo.
    fecha_de_prestamo: que almacena la fecha (aaaa-mm-dd) en la que se generó el préstamo
    fecha_de_devolucion: que almacena la fecha (aaaa-mm-dd) en la que se devolvió finalizó el préstamo (se devolvió el recurso)

    """
    #DECLARACIÓN DE ATRIBUTOS
    tiempo_maximo_permitido = int
    titular_del_prestamo = Usuario
    fecha_de_prestamo = date
    fecha_de_devolucion = date
    recurso_prestado = Recurso


    #MÉTODO CONSTRUCTOR DE LA CLASE
    def __init__(self, titular_del_prestamo, recurso_prestado, tiempo_maximo_permitido = None, fecha_de_prestamo = date.today(), fecha_de_devolucion = date(1900,1,1)):
        
        #Cada atributo recibe un valor por defecto.
        self.fecha_de_prestamo = fecha_de_prestamo
        self.fecha_de_devolucion = fecha_de_devolucion
        self.recurso_prestado = recurso_prestado
        self.titular_del_prestamo = titular_del_prestamo

        #En caso de que el valor del tiempo máximo permitido sea None, por defecto se asignará la cantidad de días equivalente a un mes
        if (tiempo_maximo_permitido == None):
            #La fecha inicial es la fecha de préstamo
            fecha_inicial = self.fecha_de_prestamo 
            #La fecha final es la fecha en que se cumple un mes
            fecha_final = date
            #Esta variable almacena la diferencia entre las fechas inicial y final
            diferencia_fechas = date
            #Estas variables se usan para separar la fecha en día, mes y año
            dia, mes, anno = int, int, int 
            
            dia = fecha_inicial.day
            mes = fecha_inicial.month
            anno = fecha_inicial.year

            #Esta variable permitirá almacenar el número de días que tiene el siguiente mes
            num_dias_del_mes = int

            #Se aumenta el mes en 1, si es diciembre, se reinicia el mes a 1 y se aumenta el año
            if (mes == 12):
                mes = 1
                anno += 1
            else:
                mes += 1
            
            #Se verifica cuántos días tiene el nuevo mes
            #Si el mes es 2 (Febrero), se determina si el año es bisiesto
            if (mes == 2): 
                #Un año es bisiesto si es divisible entre 400 o si es divisible entre 4 pero no entre 100
                if ((anno%4 == 0 and anno%100 != 0) or (anno%400 == 0)):
                    num_dias_del_mes = 29
                else:
                    num_dias_del_mes = 28
            elif (mes == 4 or mes == 6 or mes == 9 or mes == 11): #Los meses 4, 6, 9 y 11 tienen 30 días
                num_dias_del_mes = 30
            else:
                num_dias_del_mes = 31 #Los demás meses tienen 31 días
        
            #Se verifica si el día original es menor o igual al máximo día que tiene el nuevo mes
            if (dia <= num_dias_del_mes):
                #Si se cumple, entonces la fecha en que se cumple el mes será
                fecha_final = date(anno, mes, dia)
            else:
                #Si no se cumple, entonces el día original no existe en el siguiente mes
                #Por ejemplo, Marzo tiene 31 días pero Abril no.
                fecha_final = date(anno, mes, num_dias_del_mes)
            
            #Se calcula la diferencia entre las fechas
            diferencia_fechas = fecha_final - fecha_inicial
            
            #Se guarda en el atributo tiempo máximo el número de días que hay entre ambas fechas
            self.tiempo_maximo_permitido = diferencia_fechas.days
        else:
            #En caso de que no sea el valor None, entonces se asigna el valor ingresado en el parámetro
            self.tiempo_maximo_permitido = tiempo_maximo_permitido
            

        
    #MÉTODO PARA MOSTRAR LA INFORMACIÓN DEL PRÉSTAMO
    def mostrar_informacion (self, para_el_usuario = True):
        #El parámetro "para_el_usuario" tiene su principal función en mostrar un tipo de informació u otra del préstamo
        #Este método es utilizado en la generación de los historiales de usuarios y de recursos
        if (para_el_usuario):
            print("************************\nINFORMACIÓN DEL PRÉSTAMO\n************************\n")
            self.recurso_prestado.mostrar_informacion()
            print(f"Fecha de generación del préstamo: {self.fecha_de_prestamo}")
            print(f"Fecha de devolución del recurso: {self.fecha_de_devolucion}")
        else:
            print("************************\nINFORMACIÓN DEL PRÉSTAMO\n************************")
            print(f"Usuario: {self.titular_del_prestamo.nombre_usuario}")
            print(f"ID del usuario: {self.titular_del_prestamo.id}")
            print(f"Fecha de generación del préstamo: {self.fecha_de_prestamo.isoformat()}")
            print(f"Fecha de devolución del recurso: {self.fecha_de_devolucion}")


    #MÉTODO QUE CALCULA LOS DÍAS ATRASADOS QUE LLEVA UN USUARIO SIN DEVOLVER EL RECURSO
    def verificar_dias_de_mora (self, fecha_actual = date.today()):
        #Por defecto, se asume que la fecha actual es la del día en que se ejecuta al método
        dias_totales = int
        dias_de_mora = int
        dias_totales = fecha_actual - self.fecha_de_prestamo
        dias_totales = dias_totales.days
        dias_de_mora = dias_totales - self.tiempo_maximo_permitido
        if (dias_de_mora > 0):
            return dias_de_mora
        else:
            return 0
    



