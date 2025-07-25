'''
Desarrolla un script que recibiendo de entrada 
una cadena de caracteres devuelva el texto codificado según el cifrado ROT13
'''

### podemos desarrollar el script con strings
alfabeto = "abcdefghijklmnopqrstuvwxyz"
alfabeto_mayusculas = alfabeto.upper()

### o podemos desarrollarlo con listas
'''
alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
alfabeto_mayusculas = []
for letra in alfabeto:
    alfabeto_mayusculas.append(letra.upper())
'''

# pedimos el mensaje por pantalla
mensaje = input("Introduce un mensaje a encriptar: ")
# iniciamos una variable de tipo string 
# vacia que contendra el mensaje cifrado
mensaje_cifrado = ""

# --- recorrer cada una de las letras del mensaje
for char in mensaje: 
    # compruebo si se encuentra en el alfabeto en minusculas
    if char in alfabeto:
        # recorrer el alfabeto
        for i in range(len(alfabeto)):
            # cuando encuentre la letra guardo el indice
            if char == alfabeto[i]:
                char_indice = i

                # si la letra está en la segunda mitad del alfabeto
                if char_indice + 13 >= 26:
                    # restamos 26 para que al sumar 13 comencemos desde
                    # el comienzo del alfabeto de nuevo
                    char_indice = char_indice - 26

                # el nuevo indice cifrado será el antiguo + 13
                nuevo_indice = char_indice + 13
                # accedemos a la letra cifrada
                letra_cifrada = alfabeto[nuevo_indice]

        # añadimos la letra cifrada al mensaje cifrado
        mensaje_cifrado = mensaje_cifrado + letra_cifrada

    # compruebo si se encuentra en el alfabeto en mayúsculas
    elif char in alfabeto_mayusculas:
        # recorror el alfabeto
        for i in range(len(alfabeto_mayusculas)):
            # cuando ecuentre la letra guardo el indice
            if char == alfabeto_mayusculas[i]:
                char_indice = i

                # si la letra está en la segunda mitas del alfabeto
                if char_indice + 13 >= 26:
                    # restamos 26 para que al sumar 13 comencemos desde
                    # el comienzo del alfabeto de nuevo
                    char_indice = char_indice - 26

                # el nuevo indice cifrado será el antiguo + 13
                nuevo_indice = char_indice + 13
                # accedemos a la letra cifrada
                letra_cifrada = alfabeto_mayusculas[nuevo_indice]
        # añadimos la letra cifrada al mensaje cifrado
        mensaje_cifrado = mensaje_cifrado + letra_cifrada

    # si la letra no forma parte de las 26 letras del alfabeto latino
    # no la ciframos
    else:
        mensaje_cifrado = mensaje_cifrado + char

mensaje_comparacion = ""
if mensaje_cifrado == mensaje_comparacion:
    print(f"Los mensajes {mensaje} y {mensaje_comparacion} son una encriptacion el uno del otro")
else:
    print(f"Los mensajes {mensaje} y {mensaje_comparacion} no son una encriptacion el uno del otro")







