# ESTA FUNCIÓN PERMITE VERIFICAR DATOS ENTEROS ACOTADOS-Autor: Daniel Sánchez 28/05/2025
def leer_entero(min:int, max:int, mensaje:str):
    while(True):
        try:
            print(mensaje)
            num = int(input())
            if (num >= min and num <= max):
                return num
            else:
                print(f"Error, el número debe ser mayor o igual que {min} y menor o igual que {max}. Por favor, intente de nuevo.")
        except ValueError:
            print ("Error, está ingresando un valor que no es un número Entero. Por favor, intente de nuevo.")

# ESTA FUNCION PERMITE VERIFICAR DATOS ENTEROS POSITIVOS NO ACOTADOS-Autor: Daniel Sánchez 28/05/2025
def leer_entero_no_acotado (mensaje:str):
    while (True):
        try:
            print(mensaje)
            num = int(input())
            if (num >= 0):
                return num
            else:
                print("Error, el número ingresado debe ser positivo. Por favor, intente de nuevo.")
        except ValueError:
            print("Error, el dato ingresado no corresponde a un número. Por favor, intente de nuevo.")

# ESTA FUNCION PERMITE VERIFICAR QUE UN DATO DE ENTRADA DE TIPO CADENA NO SEA VACÍO-Autor: Daniel Sánchez 28/05/2025
def verificar_si_esta_vacio (mensaje:str):
    while (True):
        try:
            print(mensaje)
            cadena = input()
            if (cadena.replace(" ", "") != ""): # SE VERIFICA QUE AL ELIMINAR LOS ESPACIOS EN BLANCO DE LA CADENA DE TEXTO, EL RESULTADO NO SEA LA CADENA VACÍA.
                return cadena
            else:
                print("Error, este espacio no puede dejarse vacío. Por favor, intente nuevamente.")
        except ValueError:
            print("Error, usted ha ingresado un dato que no es válido. Por favor, intente de nuevo.")

# ESTA FUNCION PERMITE VERIFICAR QUE UNA CADENA SEA ALFANUMÉRICA-Autor: Daniel Sánchez 28/05/2025
def verificar_cadena_alfanumerica (mensaje:str):
    while (True):
        try:
            print(mensaje)
            cadena = input()
            """La condición verifica que la cadena ingresada sea alfanumerica y
            no esté compuesta solamente por números y
            no esté compuesta solamente por letras """
            if (cadena.isalnum() and (not cadena.isdigit() and not cadena.isalpha())):
                """Se verifica que los caracteres sean todos ASCII, para evitar signaturas
                que lleven caracteres especiales como letras con acento o espacios, por ejemplo """
                if(cadena.isascii()):
                    return cadena
                else:
                    print("Error, los datos ingresados no son válidos. Por favor, intente de nuevo.")
            else:
                print("Error, los datos ingresados deben ser alfanuméricos y no deben llevar espacios. Por favor, intente de nuevo.")
        except ValueError:
            print("Error, el dato ingresado no es válido. Por favor, intente de nuevo.")

# ESTA FUNCIÓN PERMITE VERIFICAR EL ISBN DE UN LIBRO-Autor: Daniel Sánchez 28/05/2025
def verificar_isbn (mensaje:str):
    while (True):
        try:
            print(mensaje)
            isbn = int(input())
            if (len(str(isbn)) == 13):
                return isbn
            else:
                print("Error, el código ISBN debe ser un número con exactamente 13 dígitos. Por favor, Intente de nuevo.")
        except ValueError:
            print("Error, el dato ingresado no es un número. Por favor, intente de nuevo.")

#ESTA FUNCIÓN PERMITE VERIFICAR EL ISSN DE UNA REVISTA-Autor: Daniel Sánchez 28/05/2025
def verificar_issn (mensaje:str):
    while (True):
        try:
            print(mensaje)
            issn = int(input())
            if (len(str(issn)) == 8):
                return issn
            else:
                print("Error, el código ISSN debe ser un número con exactamente 8 dígitos. Por favor, intente de nuevo.")
        except ValueError:
            print("Error, el dato ingresado no es un número. Por favor, intente de nuevo.")



# ESTA FUNCIÓN PERMITE NORMALIZAR (REMOVER PUNTUACIONES, ACENTOS, ESPACIOS Y CONVERTIR A MINÚSCULA) CADENAS
#Autor-Daniel Sánchez 30/06/2025
def normalizar_cadena (cadena_a_verificar:str):
    """
    Esta función normaliza las cadenas de texto eliminando acentos, signos de puntuación, espacios y diferencias de mayúsculas
    o minúsculas. Su propósito es facilitar comparaciones entre textos, como los nombres de los recursos bibliográficos,
    evitando que caracteres especiales impidan detectar coincidencias.
    """

    import re #Se importa el módulo que permite realizar búsquedas de patrones regulares en cadenas.
    import unicodedata #Se importa el módulo que permite realizar la normalización del texto (eliminar acentos).

    #Se declara la variable en la que se almacena la cadena de texto a normalizar.
    cadena = str
    cadena = cadena_a_verificar
    #Se declara la variable donde se almacenará el resultado final
    resultado = str
    resultado = ""
    #Se convierten todos los términos de la expresión a minúsculas
    cadena = cadena.lower()
    #Se remueven los espacios en blanco
    cadena = cadena.replace(" ", "")


    """
    Una vez removidos los espacios y mayúsculas, se eliminan los acentos. Para ello se utiliza el
    módulo unicodedata y su función normalize para descomponer las letras con acentos.
    
    """
    #Esta función de unicodedata descompone caracteres con acentos, por ejemplo, separa "á" en "a" y "´"
    cadena = unicodedata.normalize("NFKD", cadena)

    # Luego, se usa un ciclo for que itere a lo largo de la cadena normalizada.
    for i in cadena:
        """Se verifica, por medio de unicodedata.combining(), que el valor en i no sea un carácter
        de combinación, como las tildes, e irá concatenando a resultado la cadena sin sus tildes o acentos"""
        if (unicodedata.combining(i) == 0): #La función retorna 0 cuando el carácter no es de combinación.
            resultado += i


    """Una vez removidos los acentos, se eliminan las puntuaciones, para ello
    se utiliza el módulo regex. En este sentido, se realiza una sustitución de las puntuaciones,
    reemplazándolas por cadenas vacías"""

    resultado = re.sub(r"[^a-z0-9\s]", "", resultado)

    r"""
    El método sub del módulo re encuentra todas las subcadenas de carácteres donde coincida el
    patrón [^a-z0-9\s]. Dicho patrón significa:
    1. Los corchetes [] se usan para especificar el conjunto de caracteres que se desea hacer coincidir o buscar.
    2. El término \s se refiere a todos los caracteres especiales de espacio en blanco.
    3. El término a-z se refiere a todos los caracteres que son letras minúsculas (sin acento) 
    del alfabeto, desde la a hasta la z.
    4. El término 0-9 se refiere a todos los dígitos que están comprendidos entre el 0 y el 9.
    5. El término ^ al principio indica que el conjunto será el que contiene a todos aquellos carácteres
    que NO son especiales en blanco, letras a-z o dígitos 0-9 como lo son las puntuaciones, es decir, el complemento
    del conjunto que contiene a las letras, números y espacios en blanco.
    Luego, los dos parámetros adicionales indican que el reemplazo se hará por cadenas vacías y se
    hará sobre la variable resultado.
    """ 
    return resultado #Se retorna la cadena normalizada






#ESTA FUNCIÓN PERMITE VERIFICAR EL EMAIL DE UN USUARIO-Autor: Mateo Galeano

def verificar_email(mensaje:str):
    import re #Se importa el módulo que permite verificar patrones regulares
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    r"""
    La expresión regular \b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b se utiliza para: 
    verificar si una cadena tiene el formato de un correo electrónico válido. 
    1. El patrón empieza y termina con \b que indica los límites de palabra, es decir, se asegura de que el correo no esté pegado a otros textos. 
    2. La parte [A-Za-z0-9._%+-]+ indica que antes del símbolo @ puede haber letras, números y ciertos caracteres especiales permitidos en correos electrónicos. 
    3. El símbolo @ aparece de forma literal. 
    4. La parte [A-Za-z0-9.-]+, representa el dominio compuesto por letras, números, puntos y guiones. 
    5. La parte \.[A-Z|a-z]{2,7} busca un punto seguido por una extensión de dominio que tenga entre 2 y 7 letras.
    """
    while (True):
        try:
            print(mensaje)
            email = input()
            if (re.fullmatch(regex, email)):
                return email
            else:
                print("El correo ingresado no es correcto. Por favor, intente de nuevo.")
        except ValueError:
            print("Hubo un error durante el ingreso de los datos. Intente de nuevo.")

#ESTA FUNCIÓN PERMITE VERIFICAR SI LA FECHA INGRESADA POR EL USUARIO ESTA BIEN ESCRITA - Autor: Mateo Galeano

def verificar_fecha(mensaje:str):
    import re
    pattern_str = r'^\d{2}-\d{2}-\d{4}$'
    r"""
    La expresión regular '^\d{2}-\d{2}-\d{4}$' se usa para verificar si una cadena tiene el formato de una fecha escrita como “dd-mm-aaaa”. 
    1. El símbolo '^' al inicio indica que la coincidencia debe empezar desde el comienzo de la cadena 
    2. El símbolo '$' al final indica que debe terminar ahí mismo, no se permiten caracteres adicionales. 
    3. La parte '\d{2}' representa dos dígitos numéricos (del 0 al 9) y se repite dos veces separados por guiones -, lo que corresponde al día y al mes. 
    4. Luego, '\d{4}' indica cuatro dígitos consecutivos para el año.
    """
    while(True):
        try:
            print(mensaje)
            fecha = input()
            if (re.fullmatch(pattern_str, fecha)):
                return fecha
            else:
                print("La fecha ingresada no es correcta. Por favor, intente de nuevo.")
        except ValueError:
            print("Hubo un error durante el ingreso de los datos. Intente de nuevo.")