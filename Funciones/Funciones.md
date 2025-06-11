<!-- filepath: /home/gerarddiaz/ConquerX/Github-Projects/Aprendizaje/Aprendizaje_Python/Funciones/Funciones.md -->
# 🐍 **Paradigmas de Programación**

En programación, un **paradigma** es un enfoque o modelo que define cómo
se deben diseñar, estructurar y escribir los programas. Los principales
paradigmas de programación incluyen:

## Programación Imperativa

-   **Enfoque:** Se centra en **cómo** se deben ejecutar las
    instrucciones, describiendo paso a paso las órdenes que modificán el
    estado del programa.

-   **Características:** El código se organiza como una secuencia de
    comandos (instrucciones) que cambian variables o datos en memoria y
    realizan acciones específicas.

-   **Ejemplo típico:** La mayoría de los lenguajes tradicionales (C,
    Pascal, Python en su uso básico) siguen este paradigma. Un programa
    imperativo suele usar variables que cambian de valor, bucles y
    condicionales para lograr un resultado.

## Programación Funcional

-   **Enfoque:** Se basa en la **evaluación de funciones matemáticas** y
    en evitar estados mutables. Es decir, se promueve la inmutabilidad
    (no cambiar los datos existentes, sino crear nuevos) y la ausencia
    de efectos secundarios.

-   **Características:** Las funciones en este paradigma son **funciones
    puras** (el resultado depende solo de sus entradas y no de variables
    externas), se prefieren las expresiones en lugar de instrucciones.
    Se hace hincapié en operaciones como mapeos, filtrados y
    recursividad, en lugar de bucles con variables mutables.

-   **Ejemplo típico:** Haskell y Lisp son lenguajes principalmente
    funcionales. En Python, se puede programar en estilo funcional
    usando funciones como map, filter, expresiones lambda, etc., aunque
    Python no es puramente funcional.

## Programación Estructurada

-   **Enfoque:** Propone dividir el programa usando **estructuras de
    control** bien definidas (bucles, condicionales, etc.) evitando el
    uso de saltos arbitrarios como el "goto".

-   **Características:** Busca la claridad y organización del código.
    Todo programa estructurado se compone de secuencias, selecciones
    (if/elif/else) y bucles (while, for), formando bloques anidados en
    lugar de romper el flujo secuencial abruptamente. La programación
    estructurada es en realidad una forma disciplinada de programación
    imperativa (todos los programas estructurados son imperativos, pero
    con buenas prácticas de estructuración).

-   **Ejemplo típico:** Prácticamente todos los lenguajes modernos
    fomentan la programación estructurada. Por ejemplo, en Python
    siempre usamos indentación y bloques en lugar de saltos no
    estructurados, lo que nos obliga a mantener esta disciplina.

## Programación Orientada a Objetos (POO)

-   **Enfoque:** Organiza el código alrededor de **objetos** que
    representan entidades del mundo real, encapsulando tanto **datos**
    como **comportamientos** (métodos) relacionados.

-   **Características:** Cada objeto es una instancia de una **clase** y
    tiene atributos (datos) y métodos (funciones asociadas). La POO
    introduce conceptos clave como **encapsulamiento** (proteger y
    agrupar datos con sus funciones), **herencia** (poder crear nuevas
    clases basadas en otras existentes, compartiendo comportamiento) y
    **polimorfismo** (la capacidad de que diferentes clases definan
    métodos con el mismo nombre, pero comportamiento adaptado a cada
    clase).

-   **Ejemplo típico:** Java, C++ y C# son lenguajes principalmente
    orientados a objetos. Python también soporta plenamente la POO:
    podemos definir clases y crear objetos, combinando este paradigma
    con el imperativo y estructurado.

**Nota:** Muchos lenguajes de programación (incluido Python) **admiten
múltiples paradigmas** y permiten combinarlos según sea necesario. La
elección del paradigma o combinación de ellos depende del problema a
resolver, de la preferencia del desarrollador y de los requisitos del
proyecto. Python, por ejemplo, soporta programación imperativa,
estructurada, orientada a objetos e incluso algunos elementos de
funcional, todo en uno.

# 🐍 **Introducción a las Funciones en Python**

¿Qué es una Función?

Una **función** es un bloque de código reutilizable al que asignamos un
nombre. Está diseñada para realizar una **tarea específica** y puede ser
**llamada (ejecutada) repetidamente** en diferentes lugares del
programa. En resumen, una función nos permite agrupar un conjunto de
instrucciones bajo un nombre, de modo que para ejecutar esas
instrucciones solo tengamos que "llamar" a la función por su nombre,
en lugar de escribir todo el código nuevamente.

**Ventajas de usar funciones:**

-   **Reutilización de código:** evitamos duplicar código, escribiendo
    la lógica una sola vez y llamándola múltiples veces.

-   **Modularidad:** dividimos un programa complejo en piezas más
    pequeñas (funciones), facilitando la lectura y el mantenimiento.

-   **Abstracción:** podemos pensar en *qué* hace una función sin
    preocuparnos en cada uso de *cómo* lo hace internamente, una vez que
    está definida correctamente.

Definición y Creación de una Función

En Python, para **definir** (crear) una función nueva utilizamos la
palabra clave def, seguida de un nombre de función, un par de paréntesis
() (dentro de los cuales irán los parámetros si la función recibe datos
de entrada) y dos puntos :. En la siguiente línea y subsiguientes,
indentadas (con cuatro espacios o una tabulación) con respecto a la
definición, escribimos las **instrucciones** que componen el cuerpo de
la función. La sintaxis básica es:

```python
def nombre_de_la_funcion(param1, param2, ...):
    # Cuerpo de la función: instrucciones a ejecutar
    # (esta línea y las siguientes deben estar indentadas)
    ...
```

Algunos detalles importantes de la sintaxis:

-   La línea de definición **siempre comienza con** def y termina con :
    (dos puntos). Olvidar los dos puntos al final es un error sintáctico
    común.

-   El **nombre de la función** sigue las mismas reglas que los
    identificadores en Python (letras, números, guion bajo _, sin
    empezar por número, evitando palabras reservadas).

-   Los **paréntesis** () deben estar presentes incluso si la función no
    recibe ningún parámetro. Si no hay parámetros, simplemente se dejan
    vacíos ().

-   El cuerpo de la función **debe estar indentado** (normalmente 4
    espacios). Todas las instrucciones de la función van con este nivel
    de sangría. Si olvida indentar, Python dará un IndentationError.

-   Opcionalmente, una función puede devolver un valor usando la
    sentencia return. Si no se incluye return, la función ejecutará sus
    instrucciones pero *no devolverá* un resultado útil al programa (en
    ese caso, técnicamente devuelve None).

A continuación vemos un ejemplo sencillo de definición de una función y
cómo llamarla:

```python
def saludar():
    print("¡Hola, mundo!")

# Llamamos a la función definida:
saludar()
saludar()
```

**Salida:**
```python
¡Hola, mundo!

¡Hola, mundo!
```
En este ejemplo, saludar es una función sin parámetros que simplemente
imprime un saludo. La hemos llamado dos veces y efectivamente realizó la
acción (imprimir el mensaje) en cada llamada. Como no hay return, la
función devuelve None implícitamente, pero en este caso no nos interesa
un valor de retorno, solo el efecto de imprimir en pantalla.

Veamos otro ejemplo con una función que realiza un cálculo y utiliza
return para devolver un resultado:

```python
def sumar(a, b):
    """Devuelve la suma de a y b."""
    resultado = a + b
    return resultado

# Ejemplo de uso:
x = sumar(5, 7)
print("El resultado de sumar 5 y 7 es:", x)
```

**Salida:**
```python
El resultado de sumar 5 y 7 es: 12
```
Aquí definimos sumar(a, b) que toma dos parámetros (a y b), calcula su
suma y la **devuelve** con return. Al llamar sumar(5, 7), la función
retorna 12, que almacenamos en x y luego imprimimos. Si omitieramos la
sentencia return, la función imprimiría la suma (si lo hiciéramos
dentro) pero no permitiría al programa obtener ese valor para usarlo
posteriormente. Por eso es importante usar return cuando queremos que la
función proporcione un resultado al resto del programa.

## Parámetros y Argumentos en Funciones

Las funciones pueden recibir **parámetros** para trabajar con datos de
entrada, y al llamar a la función debemos proporcionar **argumentos**
concretos para esos parámetros. Es importante entender la diferencia:

-   **Parámetro:** es la **variable** que se declara en la definición de
    la función, entre los paréntesis. Representa un dato que la función
    espera recibir para realizar su tarea. Es como una "variable
    local" cuyo valor será asignado cuando la función sea invocada. Por
    ejemplo, en def sumar(a, b):, a y b son parámetros. Dentro del
    cuerpo de la función, podemos usar a y b como variables que
    contienen los valores que se le pasen a la función.

-   **Argumento:** es el **valor concreto** que proporcionamos a una
    función cuando la llamamos, el cual se asigna al parámetro
    correspondiente. Por ejemplo, en resultado = sumar(5, 7), los
    valores 5 y 7 son los argumentos que se pasan a la función sumar.
    Durante esa ejecución, a tomará el valor 5 y b el valor 7.

En otras palabras, los **parámetros** son como las variables
**formales** definidas por la función, mientras que los **argumentos**
son los datos **reales** que se pasan a la función en cada llamada.

Veamos un ejemplo para aclarar estos términos:

```python
def multiplicar(x, y):
    # x e y son parámetros formales
    return x * y

producto = multiplicar(4, 5) # 4 y 5 son argumentos reales
print("4 * 5 =", producto)
```

**Salida:**
```python
4 * 5 = 20
```
En la definición de multiplicar(x, y), x y y son parámetros. Al llamar
multiplicar(4, 5), estamos pasando los argumentos 4 y 5; dentro de la
función, x vale 4 e y vale 5, y la función devuelve el producto de
ambos.

## Argumentos Posicionales

Cuando llamamos a una función, la forma más común de pasarle los valores
es **por posición**, es decir, listando los argumentos en el mismo orden
en que los parámetros fueron definidos. A estos se les llama
**argumentos posicionales**. En el ejemplo anterior multiplicar(4, 5), 4
se asigna al primer parámetro x y 5 al segundo parámetro y por su
posición en la llamada.

El mecanismo posicional es sencillo: el primer argumento va al primer
parámetro, el segundo al segundo, y así sucesivamente. La cantidad de
argumentos que pasamos debe coincidir con el número de parámetros
esperados, a menos que algunos tengan un valor por defecto (veremos esto
más adelante).

Ejemplo con argumentos posicionales:

```python
def describir_persona(nombre, edad, ciudad):
    print(f"{nombre} tiene {edad} años y vive en {ciudad}.")

# Llamada con argumentos posicionales:
describir_persona("Ana", 30, "Madrid")
```

**Salida:**
```python
Ana tiene 30 años y vive en Madrid.
```
En la llamada, "Ana" se asigna a nombre, 30 a edad y "Madrid" a
ciudad basándose únicamente en sus posiciones.

Argumentos por Palabra Clave (Keyword)

Python también permite llamar a las funciones especificando
**explícitamente el nombre de los parámetros** a los que queremos
asignar cada argumento. A esto se le conoce como **argumentos de palabra
clave** o argumentos nombrados. En lugar de depender estrictamente del
orden, indicamos parametro=valor en la llamada. Esto tiene varias
ventajas:

-   Podemos pasar los argumentos en un orden diferente al definido en la
    función, especificando a qué parámetro corresponde cada uno.

-   Aumenta la legibilidad, pues queda claro qué significado tiene cada
    valor pasado.

-   Podemos incluso mezclar con argumentos posicionales, siempre y
    cuando los posicionales vayan primero.

Volviendo al ejemplo describir_persona, podríamos llamar a la función
con argumentos de palabra clave:

```python
# Llamadas con argumentos por palabra clave (orden diferente al original):
describir_persona(edad=30, ciudad="Madrid", nombre="Ana")
describir_persona(ciudad="Madrid", nombre="Ana", edad=30)
```

Ambas llamadas producirían el **mismo resultado** que el ejemplo
posicional, ya que estamos asociando explícitamente cada valor con su
parámetro correspondiente, sin importar el orden.

Otro ejemplo con la función multiplicar definida antes:

```python
# Usando argumentos nombrados:
print(multiplicar(x=4, y=5)) # equivalente a multiplicar(4, 5)
print(multiplicar(y=5, x=4)) # equivalente, cambiando el orden de los argumentos
```

**Salida:**
```python
20
20
```
En este caso, especificamos x=4 y y=5, o incluso invertimos el orden
y=5, x=4. Ambos llamados son válidos y Python asigna correctamente los
valores a cada parámetro por nombre, ignorando el orden.

Usando argumentos por keyword se pueden crear argumentos opcionales que
no aparecerán si no se ponen explícitamente:

```python
def imprimir_info_alumno(nombre, edad=None, curso=None, promedio=None):
    print("Nombre:", nombre)
    if edad is not None:
        print("Edad:", edad)
    if curso is not None:
        print("Curso:", curso)
    if promedio is not None:
        print("Promedio:", promedio)

imprimir_info_alumno("Juan", curso=3, edad=13, promedio=8.0)
```

En éste caso el argumento nombre es obligatorio pero el resto de
argumentos están por keyword = None, lo que significa que sino se
especifican al llamar la función no aparecerán y no saldrá error.

**Regla:** Si combinamos argumentos posicionales y por clave en una
misma llamada, primero deben aparecer los posicionales y luego los
nombrados. Por ejemplo, func(a, b, c=3) es válido, pero func(a, b=2,
c=3, d) **no lo es** (no se puede poner d posicional después de haber
usado b=2 nombrado).

Valores por Defecto en Parámetros

Al definir una función, Python permite asignar **valores por defecto** a
uno o más parámetros. Esto hace que dichos parámetros sean opcionales al
llamar a la función: si el argumento correspondiente no se proporciona,
el parámetro tomará el valor por defecto especificado en la definición.

La sintaxis es def nombre_func(param1, param2=valor_defecto,
param3=valor_defecto, ...). Cualquier parámetro con un valor por
defecto debe ir *después* de los parámetros que no lo tienen (no podemos
definir un parámetro sin default después de otro con default).

Ejemplo de definición con parámetro opcional:

```python
def saludar(nombre, saludo="Hola"):
    """Imprime un saludo. El parámetro 'saludo' es opcional."""
    print(f"{saludo}, {nombre}!")

# Llamadas:
saludar("Carlos") # Usa el valor por defecto de 'saludo'
saludar("Ana", "Buenos días")
```

**Salida:**
```python
Hola, Carlos!
Buenos días, Ana!
```
En la definición de saludar, el segundo parámetro saludo tiene como
valor por defecto "Hola". Al llamar saludar("Carlos"), no
especificamos el segundo argumento, por lo que dentro de la función
saludo tomará el valor "Hola" automáticamente. En la llamada
saludar("Ana", "Buenos días"), proporcionamos "Buenos días" para
saludo, sobrescribiendo el valor por defecto.

Otro ejemplo, con una función que eleva un número a una potencia, donde
la potencia por defecto es 2 (es decir, al cuadrado):

```python
def elevar(numero, potencia=2):
    """Devuelve 'numero' elevado a 'potencia'. Por defecto, potencia=2."""
    return numero ** potencia

print(elevar(5)) # Eleva 5 al cuadrado (potencia por defecto 2)
print(elevar(5, 3)) # Eleva 5 al cubo (sobrescribe el valor por defecto)
```

**Salida:**
```python
25
125
```
La primera llamada elevar(5) devolvió 25 porque se interpretó como 5²
(potencia=2 por omisión). La segunda llamada elevar(5, 3) devolvió 125,
ya que especificamos potencia=3.

## Llamadas Equivalentes

Gracias a los valores por defecto y a los argumentos por nombre, una
función en Python puede llamarse de múltiples formas **equivalentes**.
Es decir, distintas maneras de invocar producen el mismo resultado
final. Por ejemplo, usando la función elevar definida arriba (donde
potencia por defecto es 2), todas las siguientes llamadas logran lo
mismo:

```python
print(elevar(5)) # Usa potencia por defecto (2)
print(elevar(5, 2)) # Explicita la potencia aunque sea el mismo valor por defecto
print(elevar(numero=5, potencia=2)) # Usa argumentos nombrados en cualquier orden
print(elevar(potencia=2, numero=5)) # Invierte el orden de los argumentos nombrados
```

**Salida:**
```python
25
25
25
25
```
Las cuatro formas producen 25 como resultado. Son maneras diferentes de
llamar a elevar para obtener 5². En un código real no se usarían todas a
la vez; se escoge la que sea más clara. Por ejemplo, normalmente
llamaríamos elevar(5) directamente, pero saber que elevar(5,2) o
elevar(numero=5, potencia=2) son equivalentes ayuda a entender la
flexibilidad y la correspondencia entre parámetros y argumentos en
Python.

## Errores Comunes al Utilizar Funciones

Al comenzar a escribir y usar funciones en Python, es normal cometer
algunos errores típicos. A continuación enumeramos **errores comunes**
relacionados con la definición y llamada de funciones, junto con
consejos para evitarlos:

**Olvidar los paréntesis al llamar una función:** Si define una función,
por ejemplo def mi_funcion(): ..., debe llamarla con mi_funcion(). Si
escribe solo mi_funcion sin (), no ejecutará la función sino que
obtendrá una referencia al objeto función. Esto no causa un error
inmediato, pero la función no se lleva a cabo. Por ejemplo:

```python
def saludar():
    print("Hola")

saludar # ← Olvidó los paréntesis, no se ejecuta la función

saludar() # ← Llamada correcta, aquí sí se ejecuta la función
```

En el primer caso, no sucede nada (o si intentáramos usar ese valor,
veríamos algo como <function saludar at 0x7f...> en pantalla).
Asegúrese de incluir () para **invocar** la función.

**Olvidar los dos puntos : al definir la función:** Por ejemplo,
escribir def nueva_funcion() en una línea e intentar empezar el cuerpo
en la siguiente dará error. Siempre debe terminar la línea de definición
con :. Si olvida ponerlo, Python mostrará un SyntaxError indicando
sintaxis inválida.

**No indentar el cuerpo de la función (o indentarlo incorrectamente):**
Después de la línea def ...:, todas las instrucciones que pertenezcan a
la función deben ir con una sangría adicional. Si no las indenta, o si
las indenta mal (por ejemplo, alineadas con def), Python lanzará un
error de indentación. Un mensaje típico sería IndentationError: expected
an indented block (se esperaba un bloque indentado). La consistencia en
la indentación es crucial.

**Usar un nombre de variable/función no definido (fuera de alcance):**
Si intenta acceder dentro de la función a una variable que no ha sido
definida dentro de ella ni pasada como parámetro, obtendrá un NameError.
Asimismo, si llama a una función que aún no se ha definido (o está
definida más abajo sin haber sido interpretada aún), también es un
NameError. El orden y alcance de las definiciones importa. Asegúrese de
definir funciones antes de usarlas, y de pasar todos los datos
necesarios como parámetros o definir variables globales si realmente es
necesario (aunque es mejor práctica retornar valores y usar variables
externas explícitamente).

**Cantidad incorrecta de argumentos en la llamada:** Si una función
espera ciertos parámetros y no se proporcionan correctamente, Python
lanzará un TypeError.

**Faltan argumentos:** Si la función tiene, por ejemplo, 2 parámetros
obligatorios y usted le pasa solo 1 argumento, el error será algo como:
TypeError: funcion_x() missing 1 required positional argument. Por
ejemplo:

```python
def restar(a, b):
    return a - b

restar(5) # Llamada incorrecta: falta el segundo argumento
```

*Error producido:*
```python
TypeError: restar() missing 1 required positional argument: 'b'
```
**Argumentos de más:** Si pasa más argumentos de los que la función
define, ocurrirá un error similar indicando que recibió argumentos
extras. Ejemplo: restar(5, 3, 2) generaría TypeError: restar() takes 2
positional arguments but 3 were given.

**Duplicación por nombre y posición:** Caso particular de pasar un
argumento dos veces, por ejemplo, llamar restar(5, a=3) (donde a ya se
pasó como 5 posicionalmente y luego otra vez por nombre) causará un
error de duplicación de valor para el parámetro a. Evite mezclar de
forma incorrecta posicionales y nombrados.

**Confundir imprimir (print) con retornar (return):** Un error lógico
frecuente es asumir que imprimir un resultado dentro de la función
equivale a devolverlo. Si una función solo hace print pero no return, al
almacenarla en una variable obtendrá None. Por ejemplo:

```python
def sumar_print(a, b):
    print(a + b) # Imprime el resultado pero no lo retorna

resultado = sumar_print(2, 3)
print("Resultado:", resultado)
```

**Salida:**
```python
5
Resultado: None
```
En este código, la función sumar_print imprime 5, pero luego al hacer
resultado = sumar_print(2,3), la variable resultado vale None porque la
función no retornó nada. La línea print("Resultado:", resultado)
muestra None. La lección aquí es: use return para que la función
entregue valores al exterior. Use print solo para mostrar algo en
pantalla si es necesario, pero no como sustituto de return.

**Modificar inadvertidamente variables globales (efectos secundarios):**
Si una función usa variables definidas fuera de ella, podría cambiarlas
sin darse cuenta, lo que puede ser fuente de confusiones (esto se
relaciona con los *efectos secundarios* y por qué la programación
funcional los evita). Aunque Python lo permite, es buena práctica que
las funciones se mantengan lo más independientes posible de variables
globales. Si necesita modificar una variable global dentro de una
función, debería declararla como global nombre_variable dentro de la
función, pero esto debe usarse con precaución. Una alternativa mejor es
que la función retorne un resultado y asignarlo fuera, en lugar de
modificar directamente variables externas.

# 🐍 Retorno de funciones, argumentos arbitrarios y módulos en Python

En Python, las **funciones** nos permiten organizar código reusable para
tareas específicas. En esta guía didáctica cubriremos varios conceptos
importantes relacionados con funciones: cómo **devolver valores** con
return, cómo manejar un **número arbitrario de argumentos** (*args y
**kwargs), y cómo **organizar funciones en módulos** separados para
mejorar la estructura de nuestros programas. Cada sección incluye
explicaciones claras y ejemplos de código prácticos que puedes copiar y
probar. ¡Vamos a ello! 😃

## 🔙 Valores de retorno de una función

Cuando definimos una función en Python, podemos hacer que **devuelva un
valor** al programa principal usando la palabra clave return. Esto
permite que la función *produzca* un resultado que luego podemos
almacenar en una variable o usar directamente. Por ejemplo, una función
puede realizar un cálculo y **retornar** el resultado para que el código
que la llamó lo utilice.

Algunos puntos a recordar sobre la sentencia return:

-   La ejecución de la función **termina** en cuanto se ejecuta un
    return. Cualquier código después de return dentro de la función no
    se ejecutará.

-   Si una función **no** incluye un return, o este se escribe sin
    especificar un valor (por ejemplo, return a secas), la función
    retornará automáticamente **None** (que representa "ningún valor").

-   Podemos usar return para devolver **cualquier tipo de dato**:
    números, cadenas, listas, diccionarios, objetos, etc. Incluso es
    posible devolver múltiples valores separados por comas (Python los
    agrupa en una tupla). Veamos estos casos con más detalle.

```python
def formatear_nombre(nombre, apellido, segundo_nombre=''):
    """Devuelve un nombre completo formateado elegantemente."""
    if segundo_nombre:
        nombre_completo = f"{nombre} {segundo_nombre} {apellido}"
    else:
        nombre_completo = f"{nombre} {apellido}"
    return nombre_completo.title()

# Ejemplos de uso de la función:
nombre1 = formatear_nombre("ada", "lovelace")
print(nombre1) # Ada Lovelace

nombre2 = formatear_nombre("ada", "lovelace", "byron")
print(nombre2) # Ada Byron Lovelace
```

En este ejemplo, formatear_nombre construye la cadena nombre_completo y
la **retorna** con formato de título (title()). Observa que la función
acepta un tercer argumento segundo_nombre con un valor por defecto de
'' (cadena vacía). Esto lo hace **opcional**: si la función se llama
proporcionando un segundo nombre, se usará; si no, la variable
segundo_nombre estará vacía y la función simplemente formateará *nombre*
y *apellido*. Gracias al return, las variables nombre1 y nombre2 reciben
el resultado y podemos imprimirlo o usarlo después.

### Retornar un diccionario (valores compuestos)

Una función no está limitada a devolver solo tipos básicos; también
puede retornar **estructuras de datos más complejas** como listas o
diccionarios. De hecho, a veces es útil que una función devuelva un
diccionario para empaquetar múltiples resultados con etiquetas (claves).
Por ejemplo, supongamos que queremos crear un perfil de usuario a partir
de su nombre, apellido y otros datos opcionales como edad o ubicación.
Podemos hacer que la función construya un diccionario con toda la
información y lo retorne:

```python
def construir_persona(nombre, apellido, edad=None):
    """Crea un diccionario con información de una persona."""
    persona = {'nombre': nombre, 'apellido': apellido}
    if edad:
        persona['edad'] = edad # añade la edad solo si se proporciona
    return persona

perfil1 = construir_persona("Marie", "Curie", 35)
print(perfil1) # {'nombre': 'Marie', 'apellido': 'Curie', 'edad': 35}

perfil2 = construir_persona("Ada", "Lovelace")
print(perfil2) # {'nombre': 'Ada', 'apellido': 'Lovelace'}
```

Aquí, construir_persona devuelve un **diccionario** con el nombre y
apellido siempre, y la edad solo si se suministra. Estamos usando un
parámetro opcional edad=None para que el usuario de la función pueda o
no proveer ese dato. Fíjate que en perfil1 la edad sí aparece, mientras
que en perfil2 no, porque no la pasamos al llamar la función.

Este enfoque de retornar un diccionario es útil cuando una función
necesita devolver más de un valor relacionado, ya que las claves del
diccionario actúan como etiquetas descriptivas. Otra manera de devolver
múltiples valores es retornar una **tupla** o lista con varios
elementos. Por ejemplo, podríamos hacer return nombre, apellido, edad y
Python retornaría una tupla (nombre, apellido, edad). Luego podríamos
desempaquetarla al llamar la función. Sin embargo, usar un diccionario
puede hacer el código más legible al saber qué representa cada valor
retornado.

**Resumen:** Usamos return para enviar de vuelta un resultado de la
función al punto donde fue llamada. Ese resultado puede ser cualquier
tipo de dato, desde un número simple hasta estructuras como
diccionarios. Asegúrate de almacenar o usar lo que la función retorna;
si no, el trabajo de la función se perderá. Veamos ahora cómo invocar
funciones repetidamente en bucles y cómo manejar estructuras mutables
como listas al pasarlas a funciones.

## 🔄 Uso de funciones en bucles

Una de las ventajas de las funciones es que podemos llamarlas cuantas
veces necesitemos, evitando repetir código. Es muy común usar funciones
dentro de bucles (por ejemplo, un for o while) para procesar conjuntos
de datos o realizar tareas repetitivas de forma elegante.

Imagina que tenemos una lista de nombres de usuarios y queremos saludar
a cada uno. Podríamos simplemente hacer un bucle y llamar a una función
saludar(nombre) para cada elemento de la lista:

```python
def saludar(nombre):
    print(f"Hola, {nombre.title()}!")

usuarios = ["ana", "luis", "maría"]

for user in usuarios:
    saludar(user)

# Salida:
# Hola, Ana!
# Hola, Luis!
# Hola, María!
```

En este código, el bucle for itera por cada nombre en la lista usuarios
y llama a saludar(user) en cada iteración. La función saludar se encarga
de imprimir un saludo personalizado. De esta manera, se reutiliza la
lógica de saludo sin duplicarla, simplemente llamando a la función en
cada pasada del bucle. Este patrón se puede usar con cualquier función
que deba aplicarse a múltiples elementos o repetidamente hasta cierta
condición.

Otra forma de usar funciones en bucles es dentro de un while para
ejecutar la función hasta que se cumpla una condición de salida. Lo
importante es que una función puede ser invocada múltiples veces,
facilitando la **reutilización** de código y la organización lógica del
programa.

### 📋 Listas en funciones

Las **listas** son estructuras mutables (modificables) y suelen usarse
para agrupar conjuntos de valores. Es posible **pasar listas como
argumentos** a las funciones, igual que se pasan enteros, cadenas u
otros tipos. Trabajar con listas dentro de las funciones tiene algunas
particularidades debido a su mutabilidad:

-   Podemos permitir que la función **modifique** la lista que recibe
    (añadiendo, removiendo o cambiando elementos). En ese caso, dichos
    cambios afectarán a la lista original fuera de la función.

-   O podemos diseñar la función para *no* modificar la lista original,
    ya sea trabajando sobre una copia de la lista o simplemente leyendo
    sus valores.

Veamos estos escenarios.

**Pasar una lista como argumento**

Pasar una lista a una función es tan sencillo como pasar cualquier otra
variable. Dentro de la función, podemos recorrer la lista, realizar
cálculos o simplemente mostrar información. Por ejemplo, definamos una
función que reciba una lista de magos y muestre cada nombre en pantalla:

```python
def mostrar_magos(lista_magos):
    """Imprime el nombre de cada mago en la lista."""
    for mago in lista_magos:
        print(mago.title())

magos = ["merlin", "harry houdini", "juan tamariz"]
mostrar_magos(magos)
```
**Salida:**
```python
# Merlin
# Harry Houdini
# Juan Tamariz
```

En este ejemplo, la función mostrar_magos recibe lista_magos y recorre
cada elemento imprimiéndolo con la primera letra en mayúscula. Al llamar
mostrar_magos(magos), le pasamos la referencia de nuestra lista magos.
La función simplemente **lee** cada valor para mostrarlo, **sin
modificar la lista**. Al terminar, la lista original magos permanece
intacta.

**Modificar una lista dentro de una función**

Ahora supongamos que queremos que la función no solo lea la lista sino
que la modifique. Por ejemplo, imaginemos un programa que gestione una
cola de impresiones de modelos 3D: tenemos una lista de diseños
*pendientes* de imprimir y una lista de diseños *completados*. Vamos a
escribir una función imprimir_modelos que simule el proceso de impresión
moviendo cada diseño de la lista de pendientes a la lista de
completados. Es decir, la función irá *sacando* elementos de la primera
lista y *agregándolos* a la segunda:

```python
def imprimir_modelos(pendientes, completados):
    """
    Simula la impresión de cada modelo 3D, transfiriendo cada diseño de la
    lista de pendientes a la lista de completados.
    """
    while pendientes:
        modelo_actual = pendientes.pop(0) # toma el primer modelo pendiente
        print(f"Imprimiendo modelo: {modelo_actual}")
        completados.append(modelo_actual)

diseños_pendientes = ['robot', 'cohete', 'tren']
diseños_completados = []

imprimir_modelos(diseños_pendientes, diseños_completados)

print("Pendientes:", diseños_pendientes) # Pendientes: []
print("Completados:", diseños_completados) # Completados: ['robot', 'cohete', 'tren']
```

En imprimir_modelos, el bucle while pendientes: continúa mientras la
lista pendientes tenga elementos. Dentro del bucle, usamos
pendientes.pop(0) para **remover el primer elemento** de la lista de
pendientes (simulando tomar el siguiente diseño a imprimir). Agregamos
ese elemento a la lista completados usando append(). Además, imprimimos
un mensaje indicando qué modelo se está imprimiendo.

Después de llamar a imprimir_modelos(diseños_pendientes,
diseños_completados), verás que la lista diseños_pendientes quedó vacía
([]), y diseños_completados contiene todos los diseños. Esto sucede
porque la función modificó directamente las listas que le pasamos:

-   Removió todos los elementos de diseños_pendientes.
-   Agregó esos elementos a diseños_completados.

Como las listas se pasan por referencia (es decir, la función opera
sobre *las mismas* listas en memoria que la variable externa), los
cambios dentro de la función **persisten** fuera de ella. Esto es útil
si *queremos* que la función transforme nuestra estructura de datos
original.

**Evitar modificar la lista original**

¿Qué sucede si *no* queremos que la lista original se vacíe o cambie? Es
decir, usar la función para obtener algún resultado pero preservando los
datos originales. En ese caso, tenemos un par de opciones:

-   Hacer una **copia** de la lista y pasar esa copia a la función, de
    modo que se modifique la copia y no la original.

-   O reescribir la función para que no modifique la lista, sino que por
    ejemplo construya una nueva lista con los resultados y la retorne.

La solución más sencilla cuando no queremos que una función altere
nuestra lista es pasarle una copia. En Python, la manera rápida de
copiar una lista es utilizando **slice** [:] (rebanado sin límites
copia todos los elementos) o la función list()/método .copy(). Veamos
cómo evitar que diseños_pendientes se vacíe pasando una copia a
imprimir_modelos:

```python
# Reestablecemos la lista de pendientes original
diseños_pendientes = ['robot', 'cohete', 'tren']
diseños_completados = []

# Llamamos a la función pasando una COPIA de la lista de pendientes
imprimir_modelos(diseños_pendientes[:], diseños_completados)

print("Pendientes (original):", diseños_pendientes) # Pendientes (original): ['robot', 'cohete', 'tren']
print("Completados:", diseños_completados) # Completados: ['robot', 'cohete', 'tren']
```

Aquí usamos diseños_pendientes[:] al llamar la función. Esa sintaxis
crea una nueva lista que es una copia superficial de diseños_pendientes.
La función imprimir_modelos vaciará esa copia, pero la lista original
diseños_pendientes quedará intacta. La salida confirma que después de la
llamada:

-   diseños_completados tiene los elementos procesados (porque a la
    función le pasamos la referencia de esta lista, y sí queríamos
    llenarla).
-   diseños_pendientes (original) conserva sus elementos originales, ya
    que no la pasamos directamente sino que pasamos una copia.

**Nota:** Alternativamente, podríamos haber escrito la función para que
construya y retorne una nueva lista en lugar de modificar la existente.
Por ejemplo, imprimir_modelos podría crear una lista de completados
interna y devolverla, dejando la lista original de pendientes sin tocar.
Dependiendo de la situación, podría convenir un enfoque u otro. Lo
importante es saber que las listas (y otros objetos mutables como
diccionarios) pasarán su referencia a la función. Si dentro de la
función se alteran, esos cambios se reflejarán afuera. Si necesitas
evitarlo, pasa una copia o trabaja con una copia interna.

**¿Y qué hay de los diccionarios?** Los **diccionarios** se comportan de
forma muy similar a las listas en este sentido. Puedes pasarlos como
argumento a una función y modificar sus pares clave-valor dentro.
Cualquier cambio (añadir, eliminar o cambiar entradas) afectará al
diccionario original fuera de la función, a menos que trabajes sobre una
copia (por ejemplo usando dict.copy()). Por ejemplo, si tuviéramos:

```python
def agregar_puntuacion(juego):
    juego["puntuacion"] = 0

videojuego = {"nombre": "Pac-Man"}
agregar_puntuacion(videojuego)
print(videojuego) # {'nombre': 'Pac-Man', 'puntuacion': 0}
```

Después de llamar a agregar_puntuacion, el diccionario videojuego ahora
tiene una nueva clave 'puntuacion' porque la función lo modificó
directamente. Igual que con listas, pasar videojuego.copy() en lugar de
videojuego habría prevenido el cambio en el original.

En resumen, las funciones pueden recibir listas y diccionarios para
procesarlos. Solo debes decidir si quieres que la función altere la
estructura original o no, y tomar medidas en consecuencia (usar copias o
retornar nuevas estructuras).
Después de llamar a agregar_puntuacion, el diccionario videojuego ahora
tiene una nueva clave 'puntuacion' porque la función lo modificó
directamente. Igual que con listas, pasar videojuego.copy() en lugar de
videojuego habría prevenido el cambio en el original.

En resumen, las funciones pueden recibir listas y diccionarios para
procesarlos. Solo debes decidir si quieres que la función altere la
estructura original o no, y tomar medidas en consecuencia (usar copias o
retornar nuevas estructuras).

# 📚 Guía de Estilo en Python (PEP 8)

Python cuenta con una guía oficial de estilo conocida como [PEP
8](https://peps.python.org/pep-0008/). Seguir estas convenciones hace
que el código sea más **legible**, **mantenible** y fácil de integrar
por otros desarrolladores. A continuación se resumen las recomendaciones
clave de PEP 8, con ejemplos ilustrativos:

## 🔤 Nombres descriptivos y convenciones de nomenclatura

-   **Funciones y módulos:** Nombres **en minúsculas**, utilizando
    guiones bajos para separar palabras (snake_case). Ejemplo:
    calcular_promedio, mimodulo_utilidades. Los nombres deben ser
    descriptivos sobre lo que hacen.

-   **Variables:** También en minúsculas con guiones bajos (contador,
    suma_total). Deben reflejar su propósito.

-   **Constantes:** Usar MAYÚSCULAS y guiones bajos para constantes que
    no cambian (MAX_CONEXIONES, PI).

-   **Clases:** Nombres en **CamelCase** capitalizando cada palabra
    (PascalCase). Ejemplo: ClaseBanco, UsuarioAdmin.

-   **Evitar nombres confusos:** No usar nombres de una sola letra
    (excepto variables contadoras en bucles como i, j) ni palabras
    reservadas de Python.

## 📝 Docstrings y comentarios claros

-   **Docstrings:** Cada función (y módulo) debería incluir un
    **docstring** (cadena de documentación entre triple comillas
    """...""") que explique de forma concisa qué hace la función.
    Por ejemplo, describir los parámetros y qué valor retorna. Esto
    ayuda a que **cualquier programador**, con solo ver el nombre, los
    argumentos y el docstring, entienda cómo usar la función.

-   **Comentarios inline:** Usar comentarios con # para aclarar partes
    complejas del código cuando sea necesario. Deben ser breves y al
    grano, preferiblemente en español si el código es para
    hispanohablantes, o en inglés si el proyecto lo usa.

-   **Mantener la claridad:** El código bien escrito a veces se
    **"documenta a sí mismo"** (self-documenting). Aún así, un
    comentario o docstring que explique *por qué* se hace algo (no solo
    *qué* hace) es muy útil.

Ejemplo de una función con buen estilo de nomenclatura y docstring:

```python
def calcular_area_rectangulo(base, altura):
    """Calcula el área de un rectángulo dada la base y la altura."""
    area = base * altura  # Multiplica base por altura
    return area
```

En el ejemplo, el nombre calcular_area_rectangulo es descriptivo, los
parámetros base y altura son claros, y el docstring explica la función.

## 📏 Formato general (indentación, líneas y espacios)

-   **Indentación:** Utiliza **4 espacios** por nivel de indentación (no
    tabulaciones). Una indentación consistente hace que la estructura
    del código sea evidente.

-   **Longitud de línea:** Limita la longitud de las líneas a **79
    caracteres** como recomienda PEP 8.

-   **Espacios en blanco:**

    -   No coloques espacios adicionales innecesarios. Ejemplo:
        funcion(valor) es correcto, no funcion( valor ).

    -   **Alrededor del =:** En las asignaciones **sí** se usan espacios
        antes y después de = (e.g. x = 5). **No** se deben poner
        espacios alrededor del = **en parámetros por defecto**. Ej: def
        conectar(host='localhost'): es correcto.

    -   Coloca **un espacio** alrededor de operadores (+, -, ==, etc.) y
        después de comas.

-   **Líneas en blanco:** Separar las secciones lógicas con líneas en
    blanco mejora la legibilidad. Dos líneas entre funciones o clases,
    una línea entre métodos dentro de una clase.

## 📂 Importaciones y organización del código

-   **Imports al inicio:** Después del docstring o comentario inicial.

-   **Orden de imports:** Primero biblioteca estándar, luego paquetes de
    terceros, luego módulos locales. Separados con líneas en blanco.

-   **Un import por línea:** Mejor legibilidad. Evita import os, sys.

✅ Ejemplo comparativo

**❌ Mal estilo**

```python
def SumarDos(num1,num2):#Función mal escrita
    resultado=num1+ num2
    return(resultado)
```

**✅ Buen estilo**

```python
def sumar_dos(numero1, numero2):
    """Devuelve la suma de dos números."""
    resultado = numero1 + numero2
    return resultado
```

# 🔄 Recursividad en Python

La **recursividad** es una técnica de programación donde una función se
**llama a sí misma** para resolver un problema. En lugar de usar bucles,
la función resuelve una parte del problema y luego se invoca de nuevo
con una versión más pequeña del mismo problema, acumulando resultados en
cada retorno. Es un concepto básico en informática que se basa en
dividir un problema en *sub-problemas más fáciles de resolver*,
resolviendo cada uno por separado para finalmente combinar los
resultados.

Dos elementos clave en recursividad son:

-   **Caso base:** La condición en la que la función *no* se llama a sí
    misma, sino que retorna un resultado simple directamente. Este evita
    una recursión infinita.

-   **Caso recursivo:** La parte en la que la función se llama a sí
    misma con un sub-problema más pequeño, avanzando hacia el caso base.

Si una función recursiva no define bien su caso base o nunca lo alcanza,
provocará un bucle infinito (en Python terminaría en un error de
**RecursionError** al exceder la profundidad máxima de recursión).

Veamos un ejemplo sencillo para ilustrar la recursividad.

## 🔁 Ejemplo: imprimir números pares positivos hasta N

Supongamos que queremos **imprimir todos los números pares positivos
menores o iguales a N** usando recursividad. La idea es que la función
llamará a N si es par, y luego llamará recursivamente para N-1.

Implementación en código Python:

```python
def imprimir_pares_descendente(n):
    if n <= 0:
        return
    if n % 2 == 0:
        print(n)
    imprimir_pares_descendente(n - 1)

imprimir_pares_descendente(8)  # Imprimirá: 8, 6, 4, 2
```

**Cómo funciona:** Al llamar imprimir_pares_descendente(8), la función
verifica 8 > 0 (no caso base, sigue), luego como 8 es par lo imprime, y
llama recursivamente a imprimir_pares_descendente(7). En la llamada con
7, 7 no es par, así que no imprime nada pero sigue la recursión con 6.
El 6 sí se imprime y la función llama a 5, y así sucesivamente hasta
llegar a imprimir_pares_descendente(0). Cuando n es 0, se cumple el caso
base n <= 0 y la función retorna sin llamar más recursiones, cerrando
el ciclo. En esencia, la secuencia de llamadas fue: 8 -> 7 -> 6 -> 5
-> 4 -> 3 -> 2 -> 1 -> 0; imprimiendo solo los pares (8, 6, 4, 2)
en el camino de bajada.

En este ejemplo, cada llamada recursiva **reduce el problema** (imprimir
pares de N) a un subproblema más pequeño (imprimir pares de N-1). Es
importante que eventualmente lleguemos al caso base (cuando n <= 0)
para terminar la recursión.

## 🐇 Ejemplo clásico: Fibonacci recursivo

La **serie de Fibonacci** es un ejemplo clásico para demostrar
recursividad. La serie se define así: *cada número es la suma de los dos
anteriores*, comenzando con 0 y 1. Los primeros términos son: 0, 1, 1,
2, 3, 5, 8, 13, 21, ... donde:

-   F(0) = 0 (caso base 1)
-   F(1) = 1 (caso base 2)
-   F(n) = F(n-1) + F(n-2) para n ≥ 2 (definición recursiva)

Podemos implementar esta definición de forma directa en Python con
recursividad:

```python
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

Así, fibonacci(0) retornará 0, fibonacci(1) retornará 1, y por ejemplo
fibonacci(5) calculará recursivamente fibonacci(4) + fibonacci(3).

**Paso a paso de la recursión:** Veamos cómo se evalúa fibonacci(3) paso
a paso para entender el flujo:

1.  Llamamos fibonacci(3). Como 3 no es menor que 2, entra en el caso
    recursivo y necesita calcular fibonacci(2) + fibonacci(1). La
    ejecución queda en pausa a la espera del resultado de esas
    sub-llamadas.

2.  Para calcular fibonacci(2), Python invoca la función de nuevo:
    fibonacci(2) a su vez necesita fibonacci(1) + fibonacci(0).

    -   La llamada fibonacci(1) llega al caso base (n<2) y retorna
        **1** inmediatamente.
    -   La llamada fibonacci(0) también es caso base y retorna **0**.
    -   Con esos resultados, fibonacci(2) puede resolver su suma: 1 + 0
        = 1. Por lo tanto, fibonacci(2) retorna **1**.

1.  Ahora retomamos la primera llamada fibonacci(3). Ya tenemos el
    resultado de fibonacci(2) (que es 1) y aún falta fibonacci(1). Se
    invoca fibonacci(1) (caso base) que retorna **1**.

2.  Con ambos resultados, fibonacci(3) suma fibonacci(2) + fibonacci(1)
    = **1 + 1** = **2**. Finalmente, fibonacci(3) retorna **2**.

Podemos visualizar el árbol de llamadas para fibonacci(3) así:

-   fibonacci(3)
    -   fibonacci(2)
        -   fibonacci(1) → *retorna 1*
        -   fibonacci(0) → *retorna 0*
        -   *fibonacci(2) retorna 1+0 = 1*
    -   fibonacci(1) → *retorna 1*
    -   *fibonacci(3) retorna 1+1 = 2*

Cada llamada recursiva espera el resultado de sus llamadas internas. Una
vez que las llamadas más profundas alcanzan el caso base y empiezan a
devolver valores, esas devoluciones se propagan hacia arriba,
resolviendo las llamadas pendientes hasta llegar al resultado final.

**Costo de la recursividad:** La implementación recursiva de Fibonacci
es clara y directa, pero **no es eficiente**. Si observamos el árbol de
llamadas, fibonacci(1) se calcula múltiples veces innecesariamente. Para
fibonacci(5), por ejemplo, se calculan varios valores repetidos (la
función recalcula fibonacci(3) y fibonacci(2) varias veces en ramas
diferentes). Esta explosión de llamadas repetidas hace que el tiempo de
ejecución crezca exponencialmente con n. A continuación, veremos cómo
optimizar este tipo de funciones recursivas usando *memoización*.

## ⚡ Memoización

La **memoización** es una técnica de optimización que consiste en
**almacenar en memoria los resultados ya calculados** de una función,
para evitar computarlos de nuevo en el futuro cuando se repitan las
mismas llamadas. En otras palabras, guarda los resultados de
invocaciones anteriores para que si la función es llamada otra vez con
los mismos parámetros, se pueda retornar el resultado inmediatamente
desde la cache en lugar de recalcularlo.

Esto puede **mejorar drásticamente el rendimiento** de funciones que
realizan cálculos costosos o repetitivos, como es el caso de la versión
recursiva de Fibonacci. La memoización es especialmente útil en
recursividad cuando la solución de un problema involucra *subproblemas
superpuestos* (overlapping subproblems), es decir, llamadas recursivas
que repiten los mismos cálculos una y otra vez.

Existen dos formas de aplicar memoización en Python: implementarla
**manualmente** o utilizar una solución **automática (implícita)**
proporcionada por la librería estándar.

### 🗃️ Implementación manual de memoización (explícita) (con diccionario)

Podemos modificar nuestra función Fibonacci para que use un
**diccionario** (u otra estructura) donde guarde los resultados ya
calculados. Antes de calcular fibonacci(n), la función verifica si ese
valor ya está almacenado; si es así, lo devuelve directamente, y si no,
lo calcula y luego lo almacena para usos futuros.

Una implementación manual de Fibonacci con memoización:

```python
# Diccionario global para almacenar resultados ya calculados
fib_cache = {}

def fibonacci_memo(n):
    if n < 2:
        return n
    # Si el resultado ya está en la cache, lo usamos
    if n in fib_cache:
        return fib_cache[n]
    # Si no está, lo calculamos recursivamente y lo guardamos
    resultado = fibonacci_memo(n-1) + fibonacci_memo(n-2)
    fib_cache[n] = resultado
    return resultado
```

En este código, fib_cache es un diccionario que actúa como cache. Las
primeras veces que se llame a fibonacci_memo(n) para valores nuevos de
n, irá llenando el diccionario. Si luego se vuelve a solicitar
fibonacci_memo(5) (por ejemplo) tras haber calculado antes
fibonacci_memo(5), la función retornará inmediatamente el resultado
almacenado en fib_cache sin recomputar toda la recursión.

**Ventaja:** La mejora en rendimiento es significativa. Sin memoización,
fibonacci(5) realizaría 15 llamadas recursivas en total; con
memoización, fibonacci_memo(5) realiza muchas menos, porque cada valor
hasta 5 se calcula una vez. En general, la versión con memoización
convierte un algoritmo exponencial (muy lento al crecer n) en
aproximadamente lineal, al reutilizar subresultados.

**Consideración:** La cache fib_cache ocupará memoria adicional para
guardar resultados. En problemas como Fibonacci esto no es un
inconveniente serio (solo guarda hasta n valores), pero hay que estar
consciente del equilibrio entre **tiempo de cómputo** ahorrado y
**espacio de memoria** utilizado.

### ⚙️ Memoización automática con @lru_cache

```python
from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci_rapido(n):
    if n < 2:
        return n
    return fibonacci_rapido(n-1) + fibonacci_rapido(n-2)
```

Aquí, @lru_cache(maxsize=None) envuelve la función con una capacidad
ilimitada de cache (si quisiéramos limitar cuántos resultados almacenar,
podríamos poner un número en maxsize). Cada vez que se llame a
fibonacci_rapido(n), Python verificará automáticamente si ese resultado
ya fue calculado:

-   Si es la **primera vez** para ese n, la función se ejecuta
    normalmente y el resultado se guarda en la cache.
-   Si ya se ha calculado antes fibonacci_rapido(n), entonces **no** se
    ejecuta de nuevo la función; en su lugar, el decorador devuelve el
    resultado guardado previamente.

El comportamiento es equivalente a nuestra versión manual con
diccionario, pero @lru_cache maneja internamente todo el
almacenamiento. Además, implementa una política LRU (descarta los
resultados menos usados si la cache alcanza un límite de tamaño, en caso
de que maxsize no sea None).

Uso de la versión optimizada:

```python
print(fibonacci_rapido(5))  # Calcula y almacena resultados intermedios
print(fibonacci_rapido(6))  # Reutiliza fib(5) de la cache en lugar de recalcularlo
```

La segunda llamada aprovecha que fibonacci_rapido(5) ya se conoce, por
lo que solo necesita calcular el nuevo término fibonacci_rapido(6) =
fibonacci_rapido(5) + fibonacci_rapido(4), y fibonacci_rapido(4) también
estará en cache de la primera llamada, haciendo el cálculo muy rápido.

### 🤔 Cuándo y por qué usar memoización

-   **Cálculos repetitivos:** Aplica memoización cuando tu función
    realiza muchas veces los **mismos cálculos**. Esto suele ocurrir en
    algoritmos recursivos con subproblemas superpuestos (como Fibonacci,
    caminos en grafos, cálculos combinatorios, etc.) o en funciones
    puras llamadas frecuentemente con los mismos argumentos.

-   **Mejora de rendimiento:** Si identificas que una función es un
    **cuello de botella** por cálculos redundantes, la memoización puede
    reducir drásticamente el tiempo de ejecución al evitar recomputar
    resultados. En problemas donde la complejidad sin memoización crece
    exponencialmente, agregar memoización típicamente reduce la
    complejidad a linear o polinomial, haciendo posibles cálculos que de
    otra forma serían prohibitivos.

-   **Facilidad de implementación:** En Python, usar @lru_cache es muy
    sencillo y suele ser preferible para rapidez, a menos que necesites
    un control muy específico de la cache. Con una sola línea (el
    decorador) puedes obtener grandes beneficios de rendimiento.

-   **Consideraciones de memoria:** La memoización intercambia tiempo
    por espacio. Almacenar resultados consumirá memoria. Si el rango de
    posibles entradas es muy grande (por ejemplo, calcular fibonacci(n)
    para valores enormes de n donde se almacenarían muchísimos
    resultados diferentes), la cache podría crecer mucho. En esos casos,
    puedes limitar maxsize en lru_cache o limpiar la cache si ya no se
    necesita.

-   **Funciones puras:** Es importante usar memoización principalmente
    con funciones que dependan solo de sus parámetros y siempre retornen
    el mismo valor para los mismos inputs (sin efectos colaterales). Si
    una función usa variables globales cambiantes, lee archivos, o
    depende de una base de datos, almacenar un resultado antiguo podría
    ser incorrecto la próxima vez. Para esas funciones no deterministas,
    la memoización no es adecuada.
La segunda llamada aprovecha que fibonacci_rapido(5) ya se conoce, por
lo que solo necesita calcular el nuevo término fibonacci_rapido(6) =
fibonacci_rapido(5) + fibonacci_rapido(4), y fibonacci_rapido(4) también
estará en cache de la primera llamada, haciendo el cálculo muy rápido.

# 🐍 Funciones Lambda y Decoradores

## ⚡ Funciones *lambda* en Python

### ❓ ¿Qué son las funciones *lambda*?

Las **funciones lambda** en Python son funciones anónimas, es decir,
funciones *sin nombre*. En lugar de definirlas con un nombre mediante
def, se crean usando la palabra clave lambda. Estas funciones suelen ser
pequeñas y de una sola línea, diseñadas para realizar una operación
simple.

### 🤔 ¿Para qué se usan las funciones lambda?

El principal objetivo de las funciones lambda es **abreviar la
sintaxis** y permitirnos definir funciones cortas *sobre la marcha* (es
decir, en el momento que se necesitan) sin tener que darles un nombre
formal. Son útiles para ahorrar tiempo cuando se requieren funciones
simples, por ejemplo al pasar una función como parámetro a otra función
(como veremos con map, filter o sorted). En resumen, las lambdas nos
permiten escribir código más conciso para tareas puntuales.

**Nota:** Todo lo que puedes hacer con una función lambda puedes
lograrlo también con una función normal definida con def. Sin embargo,
**no todo lo que se puede hacer con una función normal se puede hacer
con una lambda** debido a las restricciones de su sintaxis.

### 📝 Sintaxis de una función lambda

La sintaxis de una función lambda es:
```python
lambda <parametros>: <expresion>
```
-   **Parámetros:** una lista opcional de parámetros (igual que en una
    función común). Puede tener cero, uno o varios parámetros, separados
    por comas.

-   **Expresión:** una única expresión cuyo resultado será el valor de
    retorno de la función lambda. La expresión se evalúa usando los
    parámetros y su resultado es lo que la función devuelve.

Por ejemplo, una función lambda que suma dos números sería:
```python
suma = lambda a, b: a + b
print(suma(3, 5))  # Salida: 8
```
Equivalente a definir:
```python
def suma(a, b):
    return a + b

print(suma(3,5)) # 8
```

Como se ve, la versión lambda lambda a, b: a + b logra lo mismo que la
función normal def suma(a, b): \... pero en una sola línea y sin nombre
explícito (hemos asignado la lambda a la variable suma para poder
usarla).

## ⚠️ Limitaciones de las lambdas

Las funciones lambda **tienen limitaciones** importantes debido a su
naturaleza concisa:

-   Solo pueden contener **una única expresión**. No es posible escribir
    varias líneas de código, bucles for o instrucciones if tradicionales
    dentro de una lambda. (Aunque es posible usar expresiones
    condicionales simples tipo valor_if_true if condición else
    valor_if_false dentro de una lambda, no se pueden usar estructuras
    de control complejas).

-   No tienen un nombre propio ni documentación asociada (no puedes
    directamente definir una *docstring* dentro de una lambda). Esto
    puede dificultar la depuración o legibilidad si la función es
    compleja.

-   Por claridad, si la lógica que necesitas implementar requiere varios
    pasos, múltiples expresiones o es reutilizable, suele ser mejor
    definir una función normal con def y un nombre descriptivo.

En general, las lambdas se usan para **funciones pequeñas y de vida
corta**. Si encuentras que estás escribiendo lógica compleja en una
lambda, probablemente sea señal de que deberías usar una función normal
para mayor claridad.

## 🔄 Lambdas vs. funciones normales: un ejemplo comparativo

Para ilustrar la diferencia en uso, consideremos un ejemplo sencillo.
Supongamos que queremos una función que calcule la potencia de un número
elevado al cuadrado. Podemos hacerlo de dos formas:

**Con una función normal:**
```python
def al cuadrado(x):
    return x**2

print(al_cuadrado(5)) # Output: 25
``` 

Con una función lambda:
```python
al_cuadrado_lambda = lambda x: x ** 2
print(al_cuadrado_lambda(5))  # Salida: 25
```

Ambas implementaciones hacen exactamente lo mismo (tomar un número y
devolver su cuadrado). La versión con def tiene un nombre (al_cuadrado)
y podemos reutilizarla en cualquier parte; la versión lambda es anónima
y la asignamos a una variable al_cuadrado_lambda solo para usarla en ese
momento. Si no la asignáramos a una variable, podríamos invocarla
inmediatamente, por ejemplo:
```python
print((lambda x: x ** 2)(5))  # Salida: 25
```

Esta última sintaxis define la función lambda y la ejecuta al instante
con el argumento 5.

## 📚 Uso de lambdas con map, filter y sorted

Una de las situaciones más comunes donde las lambdas resultan útiles es
al usarlas junto con funciones integradas como map, filter o sorted, que
esperan otra función como argumento.

-   **map(func, secuencia)**: aplica la función func a cada elemento de
    la secuencia, devolviendo un iterable con los resultados.

-   **filter(func, secuencia)**: devuelve un iterable con los elementos
    de la secuencia para los cuales la función func devuelve True (es
    decir, filtra la secuencia según una condición).

-   **sorted(secuencia, key=func)**: ordena la secuencia según la clave
    de ordenamiento dada por la función func aplicada a cada elemento.

En estos casos, usar lambdas nos permite definir rápidamente la
transformación o criterio de filtro/orden **sin tener que definir una
función aparte** con def.

### 🔀 Ejemplo con map: doblar valores

Supongamos que queremos doblar cada número en una lista:
```python
numeros = [1, 2, 3, 4]
doblados = list(map(lambda x: x * 2, numeros))
print(doblados)  # Salida: [2, 4, 6, 8]
```

Aquí map aplica la función lambda lambda x: x \* 2 a cada elemento de la
lista numeros. El resultado es una nueva lista \[2, 4, 6, 8\] con cada
valor duplicado.

*(Alternativamente, podríamos lograr lo mismo con una comprensión de
listas: \[x \* 2 for x in numeros\], pero el ejemplo con map ilustra el
uso de lambda.)*

📏 Ejemplo con filter: filtrar números pares

Ahora, imaginemos que queremos filtrar solo los números pares de una
lista:
```python
numeros = [1, 2, 3, 4, 5, 6]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)  # Salida: [2, 4, 6]
```

La función lambda lambda x: x % 2 == 0 devuelve True si x es par. filter
utiliza esa función para **quedarse** solo con aquellos elementos para
los que la condición es verdadera. El resultado es \[2, 4, 6\].

*(La equivalencia con una comprensión de listas sería \[x for x in
numeros if x % 2 == 0\].)*

### 🗃️ Ejemplo con sorted: ordenar con clave personalizada

Las lambdas son muy útiles para proporcionar la función *clave* (key) en
ordenamientos. Por ejemplo, supongamos que tenemos una lista de tuplas
con nombres de frutas y su cantidad, y queremos ordenarla por la
cantidad (el segundo elemento de la tupla):
```python
frutas = [("manzana", 5), ("banana", 2), ("naranja", 8), ("kiwi", 3)]
# Ordenar por la cantidad (elemento índice 1 de cada tupla)
ordenado = sorted(frutas, key=lambda item: item[1])
print(ordenado)
# Output: [('banana', 2), ('kiwi', 3), ('manzana', 5), ('naranja', 8)]
```

En este caso, la lambda lambda item: item\[1\] indica que se debe usar
el segundo valor de cada tupla (item\[1\]) como clave para la
comparación al ordenar. Así, la lista de tuplas queda ordenada de menor
a mayor según la cantidad de frutas.

Otro ejemplo común: ordenar una lista de palabras por su longitud usando
una lambda:
```python
palabras = ["perro", "gato", "elefante", "abeja"]
ordenado_por_longitud = sorted(palabras, key=lambda p: len(p))
print(ordenado_por_longitud)
# Output: ['gato', 'perro', 'abeja', 'elefante']
```

Aquí la función clave lambda p: len(p) hace que sorted ordene las
palabras desde la más corta a la más larga en términos de número de
letras.

## 💡 Cuándo (no) conviene usar lambdas

**Cuándo usarlas:** las funciones lambda son recomendables cuando
necesitamos definir una función sencilla de forma rápida, especialmente
si es para usarla una sola vez o en el momento. Son ideales para casos
como los mostrados (transformaciones con map, filtrados con filter,
claves de ordenamiento con sorted, callbacks sencillos, etc.). También
mantienen el código compacto cuando una función trivial se utiliza como
argumento.

**Cuándo evitarlas:** si la operación es compleja, requiere varias
expresiones, o si planeamos reutilizar la función en muchos lugares, es
mejor definir una función normal con un nombre. Las lambdas abusivamente
largas pueden dificultar la legibilidad. Asimismo, si necesitas
documentar la función o realizar pasos intermedios (como bucles,
múltiples condiciones, manejo de excepciones), una función normal es la
elección adecuada.

En resumen, utiliza lambdas para funciones **pequeñas y simples**, y
funciones definidas con def para tareas **más complejas o
reutilizables**.

# 🎁 Decoradores en Python

## ❓ ¿Qué es un decorador?

Un **decorador** en Python es, en esencia, una función que recibe otra
función como entrada y devuelve una nueva función modificada. Dicho de
otra forma, un decorador *envuelve* a una función existente para aportar
funcionalidad extra, sin alterar directamente el código de la función
original. Los decoradores permiten añadir capacidades (por ejemplo,
registro de llamadas, control de acceso, caché de resultados, etc.) a
funciones ya definidas de una manera sencilla y reutilizable.

En términos de estructura, cuando hablamos de un decorador normalmente
tenemos **tres funciones involucradas**:

-   **A**: la función decoradora en sí (la que vamos a definir). Esta
    función recibe como parámetro otra función (la función objetivo a
    decorar).

-   **B**: la función original que deseamos decorar (aquella a la que
    queremos agregar comportamiento adicional).

-   **C**: la función resultante que el decorador retorna. Esta es una
    función interna (a menudo llamada wrapper o *envoltura*) que añade
    las nuevas funcionalidades y dentro de sí llama a la función
    original B.

En resumen, **A (decorador)** toma **B (función original)** y produce
**C (función decorada)**. Cada vez que llamemos a C, dentro de C se
ejecutará B más lo añadido.

## 🔧 ¿Cómo se define y utiliza un decorador?

Veamos paso a paso cómo crear un decorador simple. La estructura típica
de un decorador es:
```python
def mi_decorador(funcion_original):
    def wrapper(*args, **kwargs):
        # (1) Acciones opcionales antes de llamar a la función original
        resultado = funcion_original(*args, **kwargs)
        # (2) Acciones opcionales después de llamar a la función original
        return resultado
    return wrapper
```

Aquí mi_decorador es la función **A** (el decorador) que recibe
funcion_original (función **B**) y define la función interna wrapper
(**C**). En wrapper, usamos \*args y \*\*kwargs para aceptar cualquier
número de argumentos posicionales o nombrados que la función original
pudiese necesitar. Dentro de wrapper podemos ejecutar código antes y/o
después de invocar funcion_original(\*args, \*\*kwargs). Finalmente,
mi_decorador retorna la función wrapper.

Ahora, para aplicar este decorador a una función, Python ofrece una
sintaxis especial usando el símbolo @. Por ejemplo:
```python
@mi_decorador
def saludar():
    print("Hola!")
```

Equivale a definir la función normalmente y luego pasarla por el
decorador:
```python
def saludar():
    print("Hola!")

saludar = mi_decorador(saludar)
```

En ambos casos, el resultado es que la función saludar queda
\"envuelta\" por la lógica de mi_decorador. Cada vez que llamemos a
saludar(), en realidad se ejecutará el código de wrapper dentro del
decorador y éste a su vez llamará a la implementación original de
saludar.

## 🏗️ Ejemplo básico de un decorador

Para clarificar, construyamos un ejemplo concreto. Supongamos que
queremos crear un decorador que imprima un mensaje *antes y después* de
ejecutar una función dada (sin importar qué hace esa función). Podemos
definir el decorador así:
```python
def decorador_anuncia(func):
    def wrapper():
        print("Antes de ejecutar la función...")
        func()  # llamada a la función original
        print("Después de ejecutar la función.")
    return wrapper
```

Este decorador decorador_anuncia asume que la función original no tiene
parámetros (para simplificar el ejemplo). Ahora apliquémoslo a una
función simple:
```python
@decorador_anuncia
def saludar():
    print("¡Hola, mundo!")

# Ahora llamamos a la función decorada:
saludar()
```

Al ejecutar saludar(), la salida en pantalla sería:
```python
Antes de ejecutar la función...
¡Hola, mundo!
Después de ejecutar la función.
```

Vemos que gracias al decorador, alrededor del saludo original se
imprimieron los mensajes adicionales.

## 📌 Decoradores con funciones que tienen parámetros

En el ejemplo anterior, nuestra función saludar() no aceptaba
parámetros, y por eso definimos wrapper() sin *args ni **kwargs.
Pero, ¿qué pasa si queremos decorar funciones que **sí reciben
argumentos**?

La solución es hacer que el wrapper acepte parámetros arbitrarios y se
los pase a la función original. Es muy común ver el patrón de *args y
**kwargs en los decoradores para asegurar que funcionen con cualquier
firma de función. Reescribamos nuestro decorador para que sea más
general:
```python
def decorador_anuncia(func):
    def wrapper(*args, **kwargs):
        print("Antes de ejecutar la función...")
        resultado = func(*args, **kwargs)  # llamamos a la función original con sus argumentos
        print("Después de ejecutar la función.")
        return resultado
    return wrapper
```

Ahora decorador_anuncia puede decorar **cualquier** función, tenga o no
tenga parámetros, y retornará lo que la función original retorne
(gracias a que capturamos su resultado en resultado y lo devolvemos).

**Nota:** Para que el decorador sea transparente respecto a la función
original (por ejemplo, que conserve el nombre y la documentación de la
función original), Python proporciona el decorador functools.wraps. Al
usarlo sobre el wrapper, copia los metadatos apropiados de la función
original. No es obligatorio para que el decorador funcione, pero es una
buena práctica cuando se escriben decoradores reutilizables.

## 📝 Ejemplo práctico: Decorador de *logging* (registro de llamadas)

Uno de los usos más comunes de los decoradores es llevar un registro de
las llamadas a funciones (lo que se conoce como *logging*). Por ejemplo,
podemos crear un decorador que imprima información cada vez que se llama
a cierta función, incluyendo sus argumentos y eventualmente su valor de
retorno.
```python
def decorador_log(func):
    def wrapper(*args, **kwargs):
        print(f"Llamando a `{func.__name__}` con args={args} kwargs={kwargs}")
        resultado = func(*args, **kwargs)
        print(f"`{func.__name__}` ha retornado {resultado}")
        return resultado
    return wrapper

@decorador_log
def sumar(a, b):
    return a + b

# Al llamar a la función decorada:
resultado = sumar(5, 7)
```

Salida en consola:
```python
Llamando a `sumar` con args=(5, 7) kwargs={}
`sumar` ha retornado 12
```


En este ejemplo, cada vez que invocamos sumar(5, 7), automáticamente el
decorador decorador_log imprimirá los argumentos con los que se llamó la
función y lo que retornó. Este tipo de decorador es muy útil para
depuración o monitoreo de aplicaciones.

## 🔒 Ejemplo práctico: Decorador de autenticación

Otro caso de uso frecuente es controlar el acceso a ciertas funciones,
por ejemplo verificando si el usuario está autenticado o tiene permisos.
Podemos escribir un decorador requiere_autenticacion que, antes de
ejecutar la función original, chequea alguna condición de autenticación.

Imaginemos que tenemos una variable global usuario_autenticado que
indica si el usuario actual ha iniciado sesión (en un caso real,
podríamos verificar un token, una sesión, etc.). Nuestro decorador
podría ser:
```python
usuario_autenticado = False

def requiere_autenticacion(func):
    def wrapper(*args, **kwargs):
        if not usuario_autenticado:
            print("Acceso denegado: el usuario no está autenticado.")
            return  # no llama a la función original
        return func(*args, **kwargs)  # usuario autenticado, procede con la función
    return wrapper

@requiere_autenticacion
def funcion_sensible():
    print("Datos sensibles: Solo usuarios autenticados pueden ver esto.")

# Probando la función decorada:
funcion_sensible()  # Usuario no autenticado actualmente

# Autenticamos al usuario y volvemos a intentar:
usuario_autenticado = True
funcion_sensible()
```

Resultado al ejecutar:
```python
Acceso denegado: el usuario no está autenticado.
Datos sensibles: Solo usuarios autenticados pueden ver esto.
```

Primero, con usuario_autenticado = False, el decorador impide la
ejecución de funcion_sensible mostrando un mensaje de acceso denegado.
Luego, tras \"autenticar\" al usuario poniendo usuario_autenticado =
True, la llamada a funcion_sensible() pasa la comprobación y se ejecuta
el código interno de la función.

Este patrón se puede extender para comprobar roles de usuario (por
ejemplo, decoradores \@requiere_admin, \@requiere_permiso(\"X\"), etc.),
y es muy útil para separar la lógica de autorización del código
principal de las funciones.

## ♻️ Ejemplo práctico: Decorador de *memoización* (caché)

La *memoización* es una técnica de optimización que consiste en
almacenar los resultados ya calculados de una función para no repetir
cálculos costosos. Los decoradores ofrecen una forma elegante de
implementar memoización de forma transparente.

Creemos un decorador memoize que almacene en un diccionario los
resultados de invocar la función original, usando los argumentos de la
llamada como clave:

```python
def memoize(func):
    cache = {}
    def wrapper(*args, **kwargs):
        # formamos una clave a partir de los argumentos (asumiendo que son hashables)
        clave = (args, tuple(sorted(kwargs.items())))
        if clave in cache:
            # Devolvemos el resultado almacenado si ya se calculó antes con estos args
            return cache[clave]
        resultado = func(*args, **kwargs)
        cache[clave] = resultado  # Guardamos el resultado en caché
        return resultado
    return wrapper

@memoize
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
```

En este ejemplo, decoramos la función fibonacci (que computa el n-ésimo
número de Fibonacci de forma recursiva). Gracias a \@memoize, la primera
vez que se calcule fibonacci(10) (por ejemplo), el decorador almacenará
el resultado. Si luego en el código se vuelve a pedir fibonacci(10), no
se recalculará todo de nuevo, sino que el decorador devolverá
inmediatamente el valor guardado en la caché.

Este decorador mejora drásticamente la eficiencia de funciones
recursivas costosas como Fibonacci, ya que evita recomputar valores ya
obtenidos. Asimismo, se puede utilizar para cachear resultados de
funciones puras (que con los mismos argumentos siempre devuelven el
mismo resultado), por ejemplo en cálculos matemáticos pesados o
consultas repetitivas.

Con estos ejemplos, podemos ver el poder de los decoradores: permiten
agregar características transversales (*cross-cutting concerns*) a
nuestras funciones de forma clara y reutilizable. Ya sea para hacer
logging, controlar acceso, cachear resultados u otras aplicaciones, los
decoradores son una herramienta muy potente en Python para escribir
código más modular y limpio.
