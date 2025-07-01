from datetime import date
from ClaseRecurso import *
from ClaseLibro import *
from ClaseVideo import *
from ClaseAudio import *
from ClaseRevista import *
class Multa:
    """
        Esta clase representa una multa  y se encarga de crear el objeto, almacenar los datos de la multa y mostrar
        la información de esta.

        ATRIBUTOS:
        valor_adeudado: almacena el precio de la multa.
        fecha_de_generacion: que almacena la fecha en la que se generó la multa.
        recurso_con_multa: que almacena el recurso asociado a esa multa.

    """
    #DECLARACIÓN DE ATRIBUTOS
    valor_adeudado = float
    fecha_de_generacion = date
    recurso_con_multa = Recurso
    #MÉTODO CONSTRUCTOR DE LA CLASE
    def __init__ (self, valor_adeudado:float, fecha_de_generacion:date, recurso_con_multa):
        self.valor_adeudado = valor_adeudado
        self.fecha_de_generacion = fecha_de_generacion
        self.recurso_con_multa = recurso_con_multa

    #MÉTODO PARA MOSTRAR LA INFORMACIÓN DE LA MULTA:
    def mostrar_informacion (self):
        print(f"Valor adeudado: ${self.valor_adeudado}")
        print(f"Fecha de generación (aaaa-mm-dd): {self.fecha_de_generacion}")
        print(f"Recurso: {self.recurso_con_multa.titulo} | Signatura topográfica: {self.recurso_con_multa.signatura_topografica}")