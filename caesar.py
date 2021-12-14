# GcanDev

# Función para cifrar el textotexto únicamente con la ecuación del ejercicio (19x+23)mod26. Para utilizarlo con otras fórmulas, habria que modificarlo en posicion_caracter_codificado
def cifrar(texto_claro):
    msj_cifrado = ""
    for caracter in texto_claro:
        indice_unicode_caracter = ord(caracter) - ord('a')  #ord() convierte un carácter a su representación numérica en Unicode. Luego restamos el valor en unicode de 'a' para tener el íncicen en un rango de [0-25)
        posicion_caracter_codificado = (19*indice_unicode_caracter + 23) % 26 + ord('a') #aplicamos la fórmula del enunciado: 19x+23 mod26 para hallar la posición del caracter que nos interesa.
        caracter_codificado = chr(posicion_caracter_codificado) #chr() convierte la representacion numerica Unicode en el caracter correspondiente
        msj_cifrado += caracter_codificado #añadimos el carácter codificado a la cadena del mensaje
    return msj_cifrado

# Función para descifrar el texto únicamente con la ecuación del ejercicio (y-23)*11 mod26. Para utilizarlo con otras fórmulas, habria que modificarlo en posicion_caracter_descodificado
def descifrar(texto_cifrado):
    msj_descifrado = ""
    for caracter in texto_cifrado: 
        indice_unicode_caracter = ord(caracter) - ord('a') #ord() convierte un carácter a su representación numérica en Unicode. Luego restamos el valor en unicode de 'a' para tener el íncicen en un rango de [0-25)
        posicion_caracter_descodificado = ((indice_unicode_caracter -  23)*11)  % 26 + ord('a') #aplicamos la fórmula del enunciado: (y-23)*11 mod26 para hallar la posición del caracter que nos interesa.
        caracter_descodificado = chr(posicion_caracter_descodificado) #chr() convierte la representacion numerica Unicode en el caracter correspondiente
        msj_descifrado += caracter_descodificado #añadimos el carácter codificado a la cadena del mensaje
    return msj_descifrado
