import random
import string

def generar_contrasena(longitud, incluir_mayusculas=True, incluir_minusculas=True, incluir_numeros=True, incluir_simbolos=True):
    # Definimos una variable para almacenar todos los caracteres que queremos incluir en la contraseña.
    caracteres = ''
    
    # Si el argumento incluir_mayusculas es True, añadimos todas las letras mayúsculas a la variable caracteres.
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    
    # Si el argumento incluir_minusculas es True, añadimos todas las letras minúsculas a la variable caracteres.
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    
    # Si el argumento incluir_numeros es True, añadimos todos los dígitos numéricos a la variable caracteres.
    if incluir_numeros:
        caracteres += string.digits
    
    # Si el argumento incluir_simbolos es True, añadimos todos los símbolos especiales a la variable caracteres.
    if incluir_simbolos:
        caracteres += string.punctuation

    # Si no se ha seleccionado ningún tipo de caracter para generar la contraseña, lanzamos un ValueError.
    if len(caracteres) == 0:
        raise ValueError("Debes seleccionar al menos un tipo de caracter para generar la contraseña.")

    # Usamos random.choices para generar una lista de longitud 'longitud' con caracteres aleatorios de la variable caracteres.
    # Esto nos da una contraseña aleatoria con la longitud especificada.
    contrasena = random.choices(caracteres, k=longitud)
    
    # Unimos todos los caracteres generados en la lista en una sola cadena y devolvemos la contraseña generada.
    return ''.join(contrasena)

if __name__ == "__main__":
    longitud = int(input("Ingresa la longitud deseada de la contraseña: "))
    incluir_mayusculas = input("¿Incluir mayúsculas? (s/n): ").lower() == 's'
    incluir_minusculas = input("¿Incluir minúsculas? (s/n): ").lower() == 's'
    incluir_numeros = input("¿Incluir números? (s/n): ").lower() == 's'
    incluir_simbolos = input("¿Incluir símbolos? (s/n): ").lower() == 's'

    try:
        # Llamamos a la función generar_contrasena con los argumentos proporcionados por el usuario.
        contrasena_generada = generar_contrasena(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
        print("Contraseña generada:", contrasena_generada)
    except ValueError as e:
        print("Error:", e)
