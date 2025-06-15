# Programación Orientada a Objetos en Python

# Introducción a la Programación Orientada a Objetos (POO)
La **Programación Orientada a Objetos (POO)** es un paradigma de programación que se basa en organizar el código en torno a **objetos** en lugar de funciones y datos separados. En vez de tener datos sueltos y procedimientos independientes, la POO propone unir los datos y la funcionalidad en una sola estructura, formando entidades llamadas **objetos** que interactúan entre sí. En otras palabras, un objeto combina tanto **información (datos)** como **comportamiento (operaciones)** en una unidad cohesionada.

Este enfoque constituye un conjunto de principios de programación que nos permite modelar conceptos del mundo real de forma más cercana a cómo los percibimos.

Al trabajar con POO, dejamos de pensar únicamente en funciones que manipulan datos, y comenzamos a pensar en **clases** que encapsulan datos y métodos para operar sobre esos datos. Dicho de otro modo, trabajamos con **objetos** en vez de con datos y procedimientos separados. Cada objeto en un programa orientado a objetos representa algo concreto (una persona, un coche, un producto, etc.) con sus propiedades y acciones asociadas. Estos objetos se crean a partir de **clases**, que actúan como plantillas o planos.

> **Nota:** La POO se sustenta en varios principios fundamentales, entre ellos el **encapsulamiento** (combinar datos y métodos que operan sobre esos datos en una entidad), la **abstracción** (modelar elementos complejos de forma simplificada), la **herencia** (poder crear nuevas clases basadas en clases existentes) y el **polimorfismo** (la capacidad de que métodos con el mismo nombre se comporten de manera distinta según el contexto). En esta primera parte nos centraremos en encapsulamiento y los conceptos básicos; otros principios como herencia y polimorfismo suelen abordarse más adelante.

---

# 🏗 Clases y Objetos
En POO, **clase** y **objeto** son dos conceptos centrales. Una **clase** es una especie de plantilla o modelo que describe un conjunto de objetos. Podemos pensar en una clase como una definición abstracta que representa algo del mundo real. Por ejemplo, podríamos tener una clase **Silla** o una clase **Coche**, que capturan las características genéricas de todos los objetos de ese tipo. Cada clase define qué **atributos** (datos) y **métodos** (comportamientos) tendrán sus objetos.

Un **objeto**, en cambio, es una instancia concreta de una clase. Si la clase es el plano arquitectónico, el objeto es la casa construida según ese plano. El objeto tiene valores específicos para los atributos definidos por la clase y puede ejecutar los métodos definidos por la clase. En la vida diaria, si **Coche** es una clase (concepto general de coche), entonces mi coche Ferrari es un objeto particular de la clase Coche. Del mismo modo, podríamos tener la clase **Persona** y crear objetos concretos como una persona llamada Ana, otra llamada Juan, etc. Cada objeto persona tendrá sus propios datos (su nombre, edad, etc.) pero todos comparten la estructura definida por la clase Persona.

> **Resumen:** La clase define la estructura y comportamiento posible, mientras que el objeto es la realización concreta con la que trabajamos en el código. A menudo escucharemos que "un objeto es una instancia de una clase" – justamente significa que el objeto fue creado a partir de esa definición de clase y cumple con el “molde” establecido.

Para ilustrarlo, imaginemos la clase **Coche**. Podemos definir que todos los coches (objetos de la clase Coche) tienen ciertos atributos como **color**, **marca**, **modelo**, y pueden realizar ciertas acciones como `acelerar()`, `frenar()` o `tocar_claxon()`. La clase es el concepto genérico; por ejemplo, **Coche** (con atributos comunes a cualquier coche y comportamientos comunes). Un objeto sería un coche en particular, por ejemplo un Coche rojo marca Ferrari modelo 488, que es una instancia específica con `color="rojo"`, `marca="Ferrari"`, `modelo="488"`, etc. Si creamos otro objeto de la clase Coche, digamos un Coche azul marca Tesla modelo Model 3, tendrá sus propios valores (`color="azul"`, `marca="Tesla"`, `modelo="Model 3"`), pero tanto el Ferrari como el Tesla son objetos que comparten la estructura y métodos definidos en la clase Coche.

En Python, definir una clase se hace con la sintaxis `class NombreDeLaClase:` seguida por un bloque indentado donde se definen sus atributos y métodos. Veamos un ejemplo simple de definición de una clase en Python (por ahora sin entrar en detalles de los métodos especiales):

```python
class Persona:
    # Un atributo de clase (común a todas las personas, por ejemplo)
    especie = "Humano"
    # Método (comportamiento) definido dentro de la clase
    def saludar(self):
        print("Hola, mucho gusto")
```

En este ejemplo, hemos definido una clase **Persona** con un atributo de clase `especie` y un método `saludar`. Más adelante profundizaremos en cómo dar valores iniciales a los atributos de instancia (propios de cada objeto) mediante el método `__init__`, y cómo crear objetos a partir de la clase.

---

# 📋 Atributos y Métodos

Una de las ideas clave de la POO es que los objetos combinan datos y funcionalidades. Los datos se almacenan en forma de **atributos** (también conocidos como propiedades o campos), mientras que las funcionalidades se implementan mediante **métodos** (que son funciones definidas dentro de la clase). En términos sencillos:

- **Atributos:** Son las características o información que tiene un objeto. En Python, típicamente son variables que viven dentro de cada objeto. Por ejemplo, un objeto de clase Persona puede tener atributos como `nombre`, `edad` y `nacionalidad`. Un objeto de clase Coche puede tener atributos como `marca`, `modelo`, `color` o `velocidad_actual`.
- **Métodos:** Son las acciones que un objeto puede realizar, o en general, las funciones que están asociadas a la clase y que operan usando los datos del objeto. Por ejemplo, la clase Persona podría tener un método `cumplir_años()` que aumenta en 1 el atributo edad de la persona, o un método `presentarse()` que imprime un saludo usando el nombre. La clase Coche podría tener métodos como `acelerar()` (que aumenta la velocidad_actual), `frenar()` (que la disminuye) o `tocar_claxon()` (que imprime "Beep beep!" por consola).

En una representación más general, un objeto puede verse así: tiene una parte de datos (**atributos**) y otra de funcionalidades (**métodos**). Siguiendo con el ejemplo de un coche:

- **Atributos (datos):** motor, número de puertas, color, marca, etc.
- **Métodos (funcionalidades):** acelerar, tocar el claxon, girar el volante, frenar, etc.

Por ejemplo, si modelamos un Coche en Python, podríamos hacer:

```python
class Coche:
    def __init__(self, marca, color):
        # Atributos de instancia
        self.marca = marca
        self.color = color
        self.velocidad = 0 # velocidad inicial en 0
    # Método acelerar: incrementa la velocidad
    def acelerar(self, incremento):
        self.velocidad += incremento
        print(f"El coche {self.marca} aceleró a {self.velocidad} km/h")
    # Método tocar_claxon: imprime un sonido de claxon
    def tocar_claxon(self):
        print("Beep beep!")
```

En esta clase **Coche**, `marca`, `color` y `velocidad` son atributos. Los definimos dentro de `__init__` (explicado en la siguiente sección) para que cada objeto Coche tenga su propia marca, color y velocidad independiente. Los métodos `acelerar` y `tocar_claxon` son comportamientos que pueden usar y modificar esos atributos. Por ejemplo, `acelerar` utiliza `self.velocidad` para actualizar la velocidad del coche y reportar la nueva velocidad.

Notemos que los métodos son esencialmente funciones asociadas a la clase. De hecho, podemos decir que un método es una función relacionada con los objetos. La única diferencia sintáctica es que se definen dentro de la clase y que siempre reciben al menos un parámetro especial (`self` en Python, que veremos en detalle pronto). Pero en comportamiento, son como funciones: pueden tener parámetros adicionales, realizar cálculos, modificar atributos, retornar valores, etc., solo que su contexto es la instancia del objeto.

> **Nota:** En Python, también es posible definir **atributos de clase**, los cuales no pertenecen a un objeto individual sino que son compartidos por todas las instancias de esa clase. En el ejemplo de Persona anterior, definimos `especie = "Humano"` fuera de cualquier método, lo que lo convierte en un atributo de clase Persona (todas las personas compartirían el valor "Humano"). En cambio, los atributos definidos mediante `self` dentro de `__init__` son **atributos de instancia**: cada objeto persona tendrá su propio valor para esos atributos. Por lo general, usaremos atributos de instancia para la mayoría de propiedades (porque suelen variar entre objetos) y atributos de clase para constantes o valores comunes a todos.

---

# El método `__init__`

El método especial `__init__` de Python es el método de inicialización de una clase, comúnmente conocido como el **constructor** (aunque técnicamente no crea el objeto, sí lo inicializa). Python invoca automáticamente `__init__` cada vez que creamos una nueva instancia de una clase. Por ello, no necesitamos llamar manualmente a `__init__` como haríamos con un método normal; simplemente al instanciar la clase (usando la sintaxis `Clase(...)`), Python lo ejecuta por nosotros.

Las principales características de `__init__` son:

- Se ejecuta automáticamente con cada nueva instancia de una clase. Es decir, si hacemos `obj = MiClase()`, Python creará el objeto `obj` y luego llamará a `MiClase.__init__(obj, ...)` internamente para inicializarlo.
- Es el lugar donde inicializamos los atributos del objeto. Dentro de `__init__`, normalmente asignamos a `self` los valores iniciales de las propiedades del objeto, a veces usando parámetros que se pasaron al crear la instancia.
- Tiene un nombre reservado por Python (`__init__`); debemos usar exactamente ese nombre y respetar su sintaxis, ya que Python lo reconoce específicamente como el inicializador de objetos.

Veamos un ejemplo con la clase Persona para ilustrar el uso de `__init__`:

```python
# Definimos la clase Persona con __init__ y un método
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")
```

En este ejemplo, `__init__` recibe, además del omnipresente `self` (que representa al objeto que se está creando), dos parámetros `nombre` y `edad`. Dentro de `__init__`, asignamos los parámetros a los atributos correspondientes usando `self`. Así, al crear una nueva `Persona("Ana", 30)`, la nueva instancia tendrá un atributo `nombre` con valor "Ana" y `edad` con valor 30.

Como mencionamos, no llamamos a `__init__` directamente. Lo que hacemos es llamar a la clase como si fuera una función: por ejemplo, `persona1 = Persona("Ana", 30)`. Python entonces crea un objeto Persona vacío, lo referencia como `self` dentro de `__init__`, y pasa los argumentos "Ana" y 30 a los parámetros `nombre` y `edad`. Todo esto sucede detrás de escena. Una vez termina `__init__`, `persona1` queda listo con sus atributos inicializados.

> **Importante:** Si no definimos un `__init__` en nuestra clase, Python simplemente creará instancias vacías sin inicializar atributos específicos (salvo que hubiese atributos de clase). Podemos luego asignar atributos manualmente, pero lo normal es definir `__init__` para asegurarnos de que cada objeto nuevo empiece con un estado válido. Por ejemplo, si omitiéramos `__init__` en Persona, podríamos hacer `persona2 = Persona()` sin parámetros (porque no hay init), pero esa persona no tendría nombre ni edad hasta que se los asignáramos: `persona2.nombre = ...` etc.

El `__init__` puede tener cero o más parámetros según la clase necesite. En el caso de Coche en la sección anterior, exigía marca y color, pero podríamos dar valores por defecto a algunos parámetros de `__init__` para hacerlos opcionales.

---

# El uso de `self`

Dentro de la definición de una clase en Python, el parámetro `self` aparece en prácticamente todos los métodos, incluido `__init__`. ¿Qué es exactamente `self`? Es una referencia al propio objeto que se está instanciando o utilizando. Cuando escribimos métodos en una clase, Python internamente los trata de forma que siempre reciben la instancia actual como primer argumento (`self`).

Veamos un caso práctico. Supongamos que olvidamos usar `self` en un método:

```python
# Ejemplo (error común – olvidar self):
class Producto:
    def __init__(self, caducidad):
        caducidad = caducidad # ¡Error! se está creando una variable local, no un atributo
    def detalles(self):
        print(f"La caducidad del producto es {caducidad}")
```

En esta clase Producto, la intención probablemente era almacenar la caducidad (fecha de caducidad) del producto. Sin embargo, en `__init__` se olvidó anteponer `self`. La línea `caducidad = caducidad` no hace nada útil: simplemente toma el parámetro caducidad y lo asigna a una variable local con el mismo nombre (que en realidad no cambia nada y se perderá al salir de `__init__`). No se creó ningún atributo en el objeto. Luego, en el método `detalles`, al intentar imprimir `caducidad`, Python buscará una variable local llamada así (no la hay), luego una variable global (tampoco la hay en este contexto), y no encontrará nada, generando un error. Efectivamente, si intentamos usar esta clase:

Obtendríamos un **NameError** indicando que el nombre 'caducidad' no está definido, ya que el método `detalles` no tiene acceso a la variable local que se creó en `__init__` (y que ya no existe). El mensaje de error sería algo similar a: `NameError: name 'caducidad' is not defined`.

La solución es utilizar `self` para almacenar la información en un atributo del objeto en lugar de una variable local:

```python
class Producto:
    def __init__(self, caducidad):
        self.caducidad = caducidad  # Ahora sí guardamos caducidad
    def detalles(self):
        print(f"La caducidad del producto es {self.caducidad}")
```

Ahora, con `self.caducidad = caducidad`, el objeto creado tendrá un atributo llamado caducidad. El método `detalles` al llamar `self.caducidad` encontrará ese valor y lo mostrará correctamente. Hemos convertido caducidad en un atributo del objeto, definiéndolo en el método adecuado (en este caso, `__init__`). Comprobemos su uso correcto: ¡Funciona sin error! Este ejemplo ilustra por qué `self` es necesario: permite que los métodos "compartan" estado a través de los atributos del objeto. Aunque dos métodos hagan cosas diferentes, ambos pueden acceder a los mismos atributos gracias a `self`, ya que esos atributos están almacenados en el objeto (referenciado por `self`).

Otro detalle importante: `self` se pasa automáticamente al llamar a métodos en instancias. Uno nunca escribe algo como `obj.metodo(self, arg1)`. Simplemente se hace `obj.metodo(arg1)` y Python se encarga de enviar `obj` como `self`. En la definición del método, sin embargo, sí debemos incluir `self` como primer parámetro. Si definimos un método que no acepta `self`, Python no sabrá pasar el objeto y dará error. En síntesis, siempre definimos los métodos de instancia con `def nombre_metodo(self, otros_parametros...)`.

> **Equivalencia con otros lenguajes:** En otros lenguajes orientados a objetos, el concepto de `self` existe con nombres distintos. Por ejemplo, en Java, C++ y JavaScript se utiliza `this` para referirse al objeto actual. La idea es la misma. La diferencia es que en Python debemos declarar `self` explícitamente en la definición del método, mientras que en otros lenguajes suele ser implícito. Asimismo, lo que Python logra con clases y `__init__`, en JavaScript clásico se hacía con funciones constructoras usando `this` dentro (antes de la introducción de la sintaxis de clases en ES6).

---

# Creación y uso de instancias de clases

Una **instancia de clase** es simplemente un objeto creado a partir de esa clase. Para crear una instancia (es decir, instanciar una clase), utilizamos la sintaxis `NombreDeLaClase(parametros_del_constructor)`. Esto ejecuta el método `__init__` de la clase y nos devuelve el nuevo objeto. Podemos asignarlo a una variable para poder manipularlo luego.

Por ejemplo:

```python
persona1 = Persona("Ana", 31)
persona2 = Persona("Juan", 45)
```

En este fragmento, `persona1` y `persona2` son instancias de la clase Persona. Cada vez que llamamos `Persona("...")`, se construye un nuevo objeto Persona, se inicializa con los datos proporcionados (nombre y edad en este caso) y se asigna a la variable correspondiente. Es literalmente correcto decir que asignamos nuestra clase a una variable cuando creamos un objeto, ya que la variable `persona1` contendrá un objeto cuyo tipo es Persona.

Una vez que tenemos instancias, ¿cómo las usamos? Podemos acceder a sus atributos y llamar a sus métodos a través de la notación de punto (`.`). En Python, la sintaxis es `objeto.atributo` para leer (o incluso modificar) un atributo, y `objeto.metodo(args)` para invocar un método. Por ejemplo, siguiendo con las personas creadas arriba:

```python
print(persona1.nombre)      # salida: Ana
print(persona2.edad)        # salida: 45
# Modificar atributos
persona1.edad = 32
print(persona1.edad)        # salida: 32 (Ana tuvo un cumpleaños)
# Invocar métodos
persona1.saludar()
persona2.saludar()
# salida: Hola, soy Ana y tengo 32 años.
# salida: Hola, soy Juan y tengo 45 años.
```

Como se ve, después de crear `persona1` y `persona2`, podemos acceder a sus atributos (por ejemplo, `persona1.nombre`) y también reasignar el valor de esos atributos (por ejemplo, `persona1.edad = 31`). Modificar un atributo de una instancia no afecta a las demás; en el ejemplo, cambiar la edad de `persona1` no toca la de `persona2`. Cada objeto tiene su propio espacio de atributos.

Llamar a métodos es igualmente sencillo:

```python
persona1.saludar()
```

ejecuta el código del método `saludar` en el contexto del objeto `persona1`. Internamente, Python pasa `persona1` como `self`, por lo que dentro de `saludar`, `self.nombre` será "Ana" y `self.edad` será 32 en ese momento, produciendo el saludo correspondiente. Lo mismo para `persona2`.

Para confirmar la comprensión, veamos otro ejemplo con la clase Coche que definimos antes, creando una instancia y usando sus métodos:

```python
# Supongamos que la clase Coche está definida como antes
auto = Coche("Toyota", "azul") # Creamos un Coche marca Toyota, color azul
print(auto.marca, auto.color, auto.velocidad)  # salida: Toyota azul 0 (la velocidad es 0 inicialmente)
# Usamos métodos del objeto auto
auto.tocar_claxon()            # salida: Beep beep!
auto.acelerar(50)              # salida: El coche Toyota aceleró a 50 km/h
auto.acelerar(30)              # salida: El coche Toyota aceleró a 80 km/h
print(auto.velocidad)          # salida: 80 (el atributo velocidad cambió con los métodos)
otro_auto = Coche("Ford", "rojo")
otro_auto.acelerar(20)         # este acelera a 20 km/h
print(otro_auto.velocidad)     # salida: 20
print(auto.velocidad)          # salida: 80 (el Toyota sigue con su velocidad independiente)
```

Vemos que al instanciar **Coche**, pasamos los argumentos que `__init__` espera (marca y color). La variable `auto` ahora referencia un objeto Coche con esos atributos inicializados y `velocidad = 0`. Luego accedemos a los atributos (`auto.marca`, `auto.color`, `auto.velocidad`) y obtenemos los valores. Después llamamos a `auto.tocar_claxon()` y `auto.acelerar(50)`. Este último cambia el estado interno del objeto (`auto.velocidad` pasa a 50). Una segunda llamada a `auto.acelerar(30)` incrementa la velocidad a 80. Finalmente comprobamos `auto.velocidad` y vemos el efecto acumulativo.

Como práctica, es útil pensar que cada objeto "mantiene su información" y los métodos operan sobre su propia copia de esa información. Si creáramos otro coche, vemos que `otro_auto` tiene su velocidad, `auto` tiene la suya, y no se mezclan.

---

# Acceso y modificación de atributos

Ya adelantamos en la sección anterior cómo acceder y cambiar atributos, pero profundicemos brevemente:

- **Acceso a atributos:** Para leer el valor de un atributo de un objeto, utilizamos la sintaxis `objeto.nombre_atributo`. Esta nos devuelve el valor almacenado en ese atributo para ese objeto. Por ejemplo, `persona1.nombre` nos da el nombre de persona1. Podemos usar este valor como cualquier otro en expresiones, imprimirlo, etc.
- **Modificación de atributos:** Para asignar o cambiar el valor, usamos la sintaxis `objeto.nombre_atributo = nuevo_valor`. Siguiendo el ejemplo, `persona1.edad = 32` cambia la edad de persona1 a 32. Es importante destacar que cada objeto tiene su propio conjunto de atributos, así que modificar uno no afecta al otro. También es posible (aunque no siempre recomendable) agregar nuevos atributos a un objeto de forma dinámica asignándolos así, incluso si no estaban definidos originalmente en la clase.

A veces es útil realizar validaciones al modificar atributos o encapsular el acceso para controlar efectos colaterales. Para esos casos, se suelen usar métodos especiales o propiedades, pero eso escapa a los conceptos básicos.

---

# 🗃 Atributos de instancia vs. atributos de clase

Como mencionamos antes, los **atributos de instancia** pertenecen a cada objeto individual, mientras que los **atributos de clase** son compartidos por todas las instancias. Si modificamos un atributo de clase, el cambio se refleja en todos los objetos (ya que en realidad es un valor único asociado a la clase, no a las instancias). En cambio, modificar un atributo de instancia solo afecta a ese objeto en particular.

Para acceder a un atributo de clase, podemos hacerlo a través de la clase misma (`MiClase.atributo_de_clase`) o de una instancia (`mi_objeto.atributo_de_clase`), aunque normalmente se hace lo primero para dejar clara la intención. Para atributos de instancia, siempre necesitamos un objeto concreto.

**Ejemplo:** Si definimos un atributo de clase

```python
class Persona:
    especie = "Humano"
```

entonces `Persona.especie` dará "Humano", y también `persona1.especie` y `persona2.especie` (a través de las instancias) lo mostrarán. Si cambiamos `Persona.especie = "Homo sapiens"`, ambas instancias verán actualizado ese valor. Pero si hacemos `persona1.especie = "Extraterrestre"`, en realidad estaremos creando un nuevo atributo de instancia en persona1, que oculta al de clase para esa instancia. `persona2` seguiría viendo "Homo sapiens". Son detalles a tener en cuenta, aunque para empezar, suele bastar con saber que los atributos definidos dentro de `__init__` (con `self`) son de instancia, y los definidos directamente en la clase (fuera de métodos) son de clase.

# Diferencia entre función y método

Para ilustrar la diferencia entre **función** y **método**, consideremos un caso concreto: queremos tener una funcionalidad que salude a una persona. Podríamos implementarla de forma procedural (con una función) o de forma orientada a objetos (con un método en la clase Persona):

## Enfoque con función independiente:

```python
def saludar_persona(persona):
    # persona sería, por ejemplo, un diccionario con datos
    nombre = persona.get("nombre")
    edad = persona.get("edad")
    print(f"Hola, me llamo {nombre} y tengo {edad} años.")
```

Aquí `saludar_persona` es una función que recibe una estructura de datos (un diccionario) con la info de la persona y la usa para saludar. La función no está ligada a la estructura; podría recibir cualquier diccionario que tenga esas claves.

## Enfoque con método en una clase:

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def saludar(self):
        print(f"Hola, me llamo {self.nombre} y tengo {self.edad} años.")
```

En este caso, la lógica de saludo está dentro de la clase **Persona**. La función (método) ya no está separada de los datos; al contrario, vive dentro del objeto que tiene esos datos. Cuando llamamos `p.saludar()`, no necesitamos pasarle a la función el nombre ni la edad, ni siquiera el objeto `p` como tal, porque el método automáticamente tiene acceso a `self.nombre` y `self.edad`. Esto ejemplifica la **encapsulación**: los datos y el comportamiento van juntos. Además, evitamos posibles errores de pasar datos equivocados o inconsistentes, ya que la persona siempre saluda con sus propios datos.

Desde el punto de vista del diseño, usar métodos dentro de clases ayuda a organizar el código de forma más modular y cercana al dominio del problema. Cada objeto "sabe hacer cosas" por sí mismo, en lugar de tener un montón de funciones externas operando sobre estructuras de datos.

Otra pequeña diferencia técnica: cuando definimos un método dentro de una clase sin decoradores especiales, este será un **método de instancia**. Python internamente lo tratará un poco distinto que una función normal, porque esperará ser llamado desde una instancia. Si intentamos llamar al método directamente desde la clase sin instancia, por ejemplo `Persona.saludar()`, tendremos que pasarle manualmente un objeto Persona como self (e.g. `Persona.saludar(p)`), cosa que normalmente no hacemos. Esto contrasta con una función, que podemos llamar en cualquier momento pasando parámetros independientes.

En conclusión, aunque métodos y funciones comparten la misma naturaleza (bloques de código reutilizables), en POO los **métodos** están ligados a objetos y por tanto cuentan con el contexto (`self`) y típicamente manipulan los atributos de ese objeto, mientras que las **funciones** tradicionales son autónomas y necesitan que les proporcionemos todo lo que requieran a través de parámetros.

# Herencia, Polimorfismo y Más

En la **Programación Orientada a Objetos (POO)**, los conceptos avanzados como **herencia**, **polimorfismo**, **composición** y los **métodos especiales** de Python nos permiten escribir código más organizado, reutilizable y expresivo. En esta guía didáctica ampliaremos estos conceptos, introduciendo:
- **Herencia en Python:** cómo una clase puede heredar atributos y métodos de otra.
- La función `super()` y su uso: cómo aprovechar la herencia sin duplicar código.
- **Herencia múltiple:** cuando una clase hereda de dos o más clases (y qué implicaciones tiene).
- **Polimorfismo:** cómo diferentes clases pueden compartir métodos con el mismo nombre que se comportan de forma distinta.
- **Métodos especiales** (dunder methods): como `__str__`, `__repr__` y otros que permiten integrar nuestras clases con funcionalidades de Python.

Antes de profundizar en polimorfismo, veamos cómo inicializar correctamente nuestras clases hijas cuando éstas agregan atributos propios.

## 👪 Herencia en Python

**Herencia** es un pilar fundamental de la POO que nos permite crear clases nuevas basadas en clases existentes, reutilizando su código. En términos sencillos, la herencia modela una relación "es un": por ejemplo, un Perro es un Animal, un Estudiante es una Persona, un CocheEléctrico es un Coche. Aprovechando esta relación, podemos definir una clase base con atributos y comportamientos comunes, y luego definir subclases que heredan todo eso y agregan sus particularidades.

**Ventajas de usar herencia:**
- **Reutilización de código:** Definimos atributos y comportamientos comunes una sola vez en la superclase (clase base) y las subclases heredan todo esto, evitando duplicación.
- **Organización jerárquica:** Modelamos categorías generales (superclases) y casos específicos (subclases), lo que refleja mejor la estructura del problema.
- **Polimorfismo:** Permite tratar objetos de subclases como si fueran de la clase base, facilitando código genérico.

Veamos un ejemplo sencillo de herencia en Python. Definiremos una clase base `Animal` y una subclase `Perro` que hereda de `Animal`. La clase `Animal` tendrá atributos y métodos genéricos, y `Perro` los heredará, pudiendo además extenderlos:

```python
class Animal:
    def __init__(self, nombre):
        self.nombre = nombre
    def saludar(self):
        print(f"Hola, soy un animal y me llamo {self.nombre}")

class Perro(Animal):
    pass
```

Aquí definimos la clase `Perro` para heredar de `Animal`; obsérvese la sintaxis en Python para establecer herencia: ponemos entre paréntesis la superclase. La clase `Perro` no define su propio `__init__`, por lo que hereda automáticamente el `__init__` de `Animal`. Esto significa que al crear un `Perro`, en realidad se está llamando al constructor de `Animal`. `Perro` tampoco define `saludar()`, por lo que también hereda la implementación de `Animal`.

De este modo, si hacemos:

```python
mi_perro = Perro("Fido")
mi_perro.saludar()
```

el perro puede usar `saludar()` aunque no esté definido en `Perro`, porque la herencia lo tomó de `Animal`.

Ahora, agreguemos más detalle. `Perro` agrega un nuevo método `ladrar()` exclusivo de la subclase, que puede usar atributos heredados:

```python
class Perro(Animal):
    def ladrar(self):
        print("¡Guau! 🐕")
```

La herencia no solo sirve para añadir métodos; a veces queremos que la subclase cambie la implementación de algún método de la superclase. Por ejemplo, podríamos querer que `Perro` tenga un saludo distinto:

```python
class Perro(Animal):
    def saludar(self):
        print(f"¡Guau! Me llamo {self.nombre} y soy un perro.")
```

Aquí definimos la clase `Perro` para heredar de `Animal`; obsérvese la sintaxis en Python para establecer herencia: ponemos entre paréntesis la superclase. La clase `Perro` no define su propio `__init__`, por lo que hereda automáticamente el `__init__` de `Animal`. Esto significa que al crear un `Perro`, en realidad se está llamando al constructor de `Animal`. `Perro` tampoco define `saludar()`, por lo que también hereda la implementación de `Animal`.

De este modo, si hacemos:

```python
mi_perro = Perro("Fido")
mi_perro.saludar()
```

el perro puede usar `saludar()` aunque no esté definido en `Perro`, porque la herencia lo tomó de `Animal`.

Ahora, agreguemos más detalle. `Perro` agrega un nuevo método `ladrar()` exclusivo de la subclase, que puede usar atributos heredados:

```python
class Perro(Animal):
    def ladrar(self):
        print("¡Guau! 🐕")
```

La herencia no solo sirve para añadir métodos; a veces queremos que la subclase cambie la implementación de algún método de la superclase. Por ejemplo, podríamos querer que `Perro` tenga un saludo distinto:

```python
class Perro(Animal):
    def saludar(self):
        print(f"¡Guau! Me llamo {self.nombre} y soy un perro.")
```

Aquí hemos sobrescrito el método `saludar()` de `Animal` en la clase `Perro`. Ahora, `mi_perro.saludar()` usará esta nueva versión en lugar de la genérica de `Animal`.

# Herencia múltiple

En Python, una clase puede heredar de más de una clase (**herencia múltiple**). Aunque no es tan común en el diseño de clases (ya que puede añadir complejidad), es importante conocer que es posible y entender cómo funciona a grandes rasgos.

Con herencia múltiple, un objeto de la subclase es conceptualmente miembro de todas las superclases. Por ejemplo, podríamos modelar un dispositivo multifunción donde una clase `Telefono` tiene un método `llamar()`, una clase `Camara` tiene un método `fotografiar()`, y una subclase `Smartphone` herede de ambas:

```python
class Telefono:
    def llamar(self):
        print("Llamando por teléfono...")

class Camara:
    def fotografiar(self):
        print("Tomando una foto...")

class Smartphone(Telefono, Camara):
    def __init__(self):
        Telefono.__init__(self)
        Camara.__init__(self)
```

La herencia múltiple nos permite combinar funcionalidades de clases independientes. Sin embargo, hay que considerar algunos detalles:
- **Orden de herencia:** En la definición `class Smartphone(Telefono, Camara)`, el orden importa. Python buscará primero atributos/métodos en `Telefono` y, si no los encuentra, entonces en `Camara`. Este orden se define por la Method Resolution Order (MRO) de la clase.
- **Conflictos de nombres:** Si ambas superclases tienen un método o atributo con el mismo nombre, ¿cuál usa la subclase? Python seguirá el orden de la tupla de herencia (izquierda a derecha). En nuestro ejemplo, si tanto `Telefono` como `Camara` tuvieran un método `encender()`, al llamar `mi_movil.encender()`, se ejecutaría el de `Telefono` porque viene primero.
- **Inicialización de múltiples superclases:** Cuando se utiliza herencia múltiple, cada clase padre puede tener su propio `__init__`. Para inicializarlos, podríamos llamar explícitamente a cada uno (como hicimos arriba). Otra forma más cooperativa es usar `super()` en un contexto de herencia múltiple. Python determina el orden en que se llaman las superclases mediante el MRO. Usando `super()`, cada clase en una jerarquía de herencia múltiple puede cooperativamente llamar a la siguiente en la cadena de herencia sin saber exactamente cuál es. Si se llamaran métodos de superclase por nombre explícitamente, podríamos omitir inicializaciones de otras clases padre en casos de herencia múltiple. Con `super()`, Python se encarga de la secuencia correcta de llamadas. En casos simples de herencia única, `super()` llama al método de la única superclase. En casos de herencia múltiple, `super()` seguirá el orden definido por `Clase.mro()`.

Más adelante se puede profundizar brevemente cómo funciona la herencia múltiple en Python, pero en resumen, la herencia múltiple requiere cuidado para inicializar todas las partes necesarias. En la práctica, a menudo se evita la herencia múltiple en favor de otros mecanismos (como la composición, que veremos a continuación, o el uso de mixins) porque puede introducir complejidad, pero Python nos da la herramienta de la herencia múltiple para hacerlo si tiene sentido en nuestro modelo.

# Composición de clases

En lugar de una relación "es un" (como la herencia), la **composición** modela una relación "tiene un". Es decir, un objeto puede contener a otro objeto como parte de su estado interno para reutilizar su funcionalidad sin heredarla. Por ejemplo:
- Un `CocheEléctrico` es un `Coche` (herencia), pero tiene una `Batería` (composición). Un coche eléctrico no es un tipo de batería, sino que lleva una batería dentro.
- Una `Persona` tiene uno o varios `Vehículos` a su nombre, pero una persona no es un vehículo.

La composición se implementa simplemente definiendo atributos que son instancias de otras clases.

> ¿Cuándo usar composición? Cuando una clase A no es exactamente un tipo especializado de B, pero necesita usar a B internamente, es preferible usar composición. La herencia se debe usar solo cuando sí existe una relación "es un" clara. Evitemos herencias forzadas: Si algo no es conceptualmente una subclase, es mejor usar composición en lugar de herencia. (Por ejemplo, no tendría sentido hacer `class Bateria(Coche)` porque una batería no es un coche).

En resumen, la herencia modela relaciones "es un", mientras que la composición modela "tiene un". Ambas son herramientas útiles según el caso.

# 🎭 Polimorfismo

El término **polimorfismo** significa "muchas formas". En POO, se refiere a la capacidad de usar un mismo nombre de método para diferentes comportamientos, típicamente aprovechando la herencia. En lenguajes POO clásicos, el polimorfismo se logra mediante la herencia y la sobreescritura de métodos.

Veamos un ejemplo: la clase base `Animal` con un método genérico `hablar()`, y varias subclases (`Perro`, `Gato`, `Vaca`) que implementan `hablar()` de forma distinta:

```python
class Animal:
    def hablar(self):
        print("Sonido genérico de animal")

class Perro(Animal):
    def hablar(self):
        print("Guau!")

class Gato(Animal):
    def hablar(self):
        print("Miau")

class Vaca(Animal):
    def hablar(self):
        print("Muu")
```

Si tenemos una lista de animales y simplemente invocamos el método `hablar()` en cada uno:

```python
animales = [Perro(), Gato(), Vaca()]
for animal in animales:
    animal.hablar()
```

El bucle simplemente invoca `hablar()` y, gracias al polimorfismo, cada objeto responde con su propia implementación. `animal` en cada iteración puede ser un Perro, un Gato o una Vaca, y cada uno "habla" de forma distinta.

El polimorfismo aumenta la flexibilidad y escalabilidad del código:
- Podemos añadir nuevas subclases (nuevos animales con su propio `hablar()`) sin modificar el código que llama a `hablar()` en los animales.
- Permite programar con abstracciones (`Animal`) sin preocuparnos de los detalles de cada implementación concreta (`Perro`, `Gato`, `Vaca`, etc.).

En Python, el polimorfismo es muy natural gracias a su tipado dinámico. Ni siquiera se requiere que las clases compartan una superclase común; mientras los objetos tengan el método que se llama, Python lo ejecutará (esto es conocido como "duck typing"). Aun así, conceptualmente suele ser útil estructurar el polimorfismo mediante herencia para dejar claras las relaciones entre clases.

> **Resumen:** Podemos tratar a objetos de distintas clases de forma uniforme si comparten interfaces (métodos) comunes. Cada clase se encargará de su implementación particular. El polimorfismo permite escribir código más genérico y extenderlo fácilmente con nuevas clases.

# Métodos especiales (`__str__`, `__repr__`, etc.)

En Python existen métodos de instancia con nombres "especiales" (doble guión bajo al inicio y al final) que sirven para dotar a nuestras clases de ciertas funcionalidades integradas en el lenguaje. Por ejemplo, `__str__` y `__repr__` nos permiten definir cómo se representa nuestro objeto como cadena, `__add__` nos permite sobrecargar el operador +, `__iter__` hacer que el objeto sea iterable, etc. Estos métodos especiales (también llamados "dunder methods" por el doble underscore) comienzan y terminan con `__`.

Algunos de los métodos especiales más comunes:
- `__str__(self)`: representación informal o legible para humanos de un objeto (lo que se muestra con `print(obj)`).
- `__repr__(self)`: representación formal o para depuración de un objeto (lo que se muestra en la consola o al hacer `repr(obj)`; debería ser un string que permita recrear el objeto si es posible).
- `__len__(self)`: define el comportamiento de `len(objeto)`.
- `__eq__(self, otro)`: define el comportamiento de `==` (igualdad) entre objetos de la clase.
- `__add__`, `__sub__`, etc.: permiten definir cómo actúan los operadores +, - con objetos de la clase.
- `__iter__`, `__next__`: hacen que el objeto sea iterable (por ejemplo, en bucles for).
- `__getitem__`: define acceso mediante índices (`objeto[idx]`).
- `__call__`: hace que el objeto sea "llamable" como si fuera función.

No hace falta memorizarlos todos de golpe, pero conocer los más usados (como `__str__` y `__repr__`) es muy útil, y saber que existen otros nos da pistas de cómo lograr ciertos comportamientos avanzados cuando los necesitemos.

Además de representaciones, los métodos especiales permiten sobrecargar operadores y comportamientos. Por ejemplo, si definimos `__add__` en una clase `Punto(x, y)` para sumar otro punto, podríamos usar el operador + entre instancias de Punto en vez de llamar a un método. Otro ejemplo: `__iter__` y `__next__` permiten que nuestra clase se comporte como un iterador.

En conclusión, los métodos especiales permiten personalizar el comportamiento de las instancias de nuestras clases en contextos como:
- Conversión a string (`__str__`, `__repr__`).
- Uso de operadores (`__eq__`, `__add__`, etc.).
- Comportamiento en estructuras de control (`__len__` para ver si algo está vacío, `bool` para `bool(obj)`, etc.).
- Iteración (`__iter__`, `__next__`).
- Llamadas (`__call__`), entre otros.

Con esto cubrimos los principales conceptos avanzados de POO en Python. Ahora, a practicar con ejercicios que pongan en juego herencia, composición, polimorfismo y métodos especiales. Intenta resolverlos por tu cuenta y luego compara con las soluciones propuestas. Cada ejercicio incluye el enunciado, una posible estrategia (estructura sugerida) y una solución comentada paso a paso.

# Miembros Privados, Importaciones y Guía de Estilo

En este documento continuamos profundizando en la **Programación Orientada a Objetos (POO)** en Python, abordando temas esenciales como:
- Miembros privados (atributos y métodos "ocultos" dentro de una clase)
- Importación de clases y módulos
- Guía de estilo para escribir código Python limpio y mantenible

Como siempre, acompañamos cada sección con ejemplos prácticos, explicaciones y buenas prácticas.

## 👁 Miembros Privados en Python

En Python, podemos marcar atributos o métodos como "privados" usando un guion bajo doble `__` al inicio del nombre. Esto no los hace realmente inaccesibles, pero indica que no deben ser usados fuera de la clase (Python aplica name mangling, cambiando el nombre internamente para dificultar su acceso externo).

🔍 **Ejemplo:**

```python
class Banco:
    def __init__(self):
        self.__saldo = 0
    def ingresar(self, cantidad):
        self.__actualizar_saldo(cantidad)
    def __actualizar_saldo(self, cantidad):
        self.__saldo += cantidad  # método privado
```

En este ejemplo, la clase Banco tiene un atributo `__saldo` y un método `__actualizar_saldo`, ambos marcados como privados (doble guión bajo). Esto sugiere que son para uso interno de la clase. Desde fuera de la clase, no podríamos acceder directamente a `__saldo` ni llamar a `__actualizar_saldo` (al menos no sin usar trucos, ya que Python cambia sus nombres a `_Banco__saldo` internamente).

### 🛡 ¿Por qué usar miembros privados?
1. **Encapsulación:** Señala que ciertos atributos no deben ser modificados directamente desde fuera de la clase. Mejora la seguridad y mantiene la integridad de los datos.
2. **Control de acceso:** Solo los métodos de la clase pueden acceder a estos atributos. Esto evita cambios accidentales desde fuera.
3. **Evitar colisiones de nombres:** Reduce el riesgo de que otro código (subclases, librerías externas, etc.) use el mismo nombre por accidente.
4. **Abstracción y Documentación:** Señala a otros desarrolladores que ese atributo no forma parte de la interfaz pública de la clase.

### Métodos privados

Lo mismo aplica para métodos: si tenemos métodos auxiliares que no deberían ser usados fuera, podemos nombrarlos con `__` para indicar su privacidad. Por ejemplo, en la clase Banco anterior, `__actualizar_saldo` es un método privado que la clase usa para actualizar internamente el saldo.

> **Nota:** En Python es común usar un solo guión bajo `_atributo` para indicar "uso interno" (convención de protegido), y el doble `__atributo` solo cuando realmente queremos evitar colisiones en herencia. Los atributos con `_` pueden seguir accediéndose externamente (no hay name mangling), pero por convención no se deben tocar.

## 📦 Importación de clases y módulos

Al crecer nuestros programas, suele ser útil separar las clases en módulos (archivos .py) diferentes e importarlos según sea necesario.

### Importar una clase desde un módulo

Supongamos que tenemos un proyecto con la siguiente estructura de archivos:

```
proyecto/
├── vehiculos.py
└── main.py
```

**vehiculos.py:**

```python
class Coche:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def descripcion(self):
        return f"{self.marca} {self.modelo}"

class Camioneta(Coche):
    def __init__(self, marca, modelo, capacidad_carga):
        super().__init__(marca, modelo)
        self.capacidad_carga = capacidad_carga
```

**main.py:**

```python
# Importar clases específicas
from vehiculos import Coche, Camioneta
# Crear objetos
mi_coche = Coche("Toyota", "Corolla")
mi_camioneta = Camioneta("Ford", "Ranger", 1500)
# También puedes importar todo el módulo
import vehiculos as vh
otro_coche = vh.Coche("Honda", "Civic")
```

En main.py mostramos dos estilos:
- Importar clases específicas con `from vehiculos import Coche, Camioneta` y usarlas directamente.
- Importar el módulo completo con un alias `import vehiculos as vh` y luego acceder a las clases mediante el alias (por ejemplo `vh.Coche`).

En ambos casos estamos utilizando las clases definidas en otro archivo. Esto ayuda a organizar el código y facilita la reutilización.

> **Nota:** Al usar módulos, asegúrate de que estén en el mismo directorio (o en el PYTHONPATH) para que Python pueda encontrarlos.

## Guía de Estilo en Python

Para mantener un código consistente y fácil de leer, es importante seguir ciertas convenciones de estilo (PEP 8 es la guía oficial). A continuación resumimos algunas prácticas recomendadas:

### Variables
- Usar letras minúsculas.
- Nombres descriptivos (nada de x, z o a1).
- Usa snake_case.

### Funciones
- Letras minúsculas.
- Verbo + snake_case: `calcular_area`, `mostrar_resultado`.

### ⚡ Constantes
- En mayúsculas: `TASA_INTERES`, `PI`.
- Snake case (con guiones bajos si son varias palabras): `NOMBRE_CONSTANTE`.

### Clases
- Usa CamelCase: `CocheElectrico`, `CuentaBancaria`.
- El nombre debe reflejar lo que representa.

### Instancias y módulos
- En snake_case: `mi_coche`, `mi_modulo`.

### Docstrings (documentación interna)
- Para clases: Cada clase debe tener una cadena de documentación justo después de su definición:

```python
class Persona:
    """Clase que representa una persona con nombre y edad."""
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
```

- Para módulos: Al inicio del archivo .py, incluye:

```python
"""Este módulo contiene clases relacionadas con vehículos motorizados."""
```

### Buenas prácticas de formato
- Usa una línea en blanco entre métodos de una clase.
- Usa dos líneas en blanco entre clases dentro del mismo módulo.

### Orden de importaciones
Cuando importes módulos, sigue este orden:
1. Módulos de la biblioteca estándar.
2. (Línea en blanco)
3. Tus propios módulos.

**Ejemplo:**

```python
import math
import random
from vehiculos import Coche
```

Esto mejora la legibilidad y la organización del código.
