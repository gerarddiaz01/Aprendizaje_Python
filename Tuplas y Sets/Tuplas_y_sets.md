# 🐍 Tuplas y Sets

## 🔹 ¿Qué es una TUPLA?

Una **tupla** es una estructura de datos muy similar a una lista, con la
diferencia clave de que **es inmutable**.

Características:

-   No se pueden modificar después de ser creadas (no append, no remove,
    no pop, etc.)

-   Sí se pueden **recorrer** y **consultar**.

-   Permiten **extraer porciones** (slicing), pero se genera una **nueva
    tupla**.

-   Se puede usar el operador in para verificar si un elemento está
    presente.

## 💡 ¿Por qué usar TUPLAS?

-   Son **más rápidas** que las listas.

-   Ocupan **menos espacio en memoria**.

-   Se pueden usar como **llaves en un diccionario** (por ser
    inmutables).

-   Útiles cuando:

    -   Sabemos que los valores no deben cambiar.

    -   Queremos garantizar la integridad de los datos.

### Ejemplo:
```python
coordenada = (40.7128, -74.0060) # latitud, longitud
```
## 🧰 SINTAXIS BÁSICA
```python
tupla = (1, 2, 3)

type(tupla) # <class 'tuple'>

tupla_vacia = ()

tupla_unitaria = (1,) # ¡OJO! El uso de la coma es obligatorio
```
## ❌ INMUTABILIDAD
```python
tupla = (1, 2, 3)

tupla[0] = 99 # Error: 'tuple' object does not support item assignment
```
## 🧬 OPTIMIZACIÓN: Lista vs Tupla

|   | Lista | Tupla  |   |   |
|---|---|---|---|---|
| Mutable | ✅ Sí  | ❌ No  |   |   |
| Espacio de memoria  | Mayor uso  | Menor uso  |   |   |
| Tiempo de creación  | Más lento  | Más rápido  |   |   |
| Uso ideal  | Datos cambiantes  | Datos fijos  |   |   |

**Ejemplo con sys.getsizeof(): Para saber cuanto ocupa en bytes en el
sistema**
```python
import sys

lista = [1, 2, 3]

tupla = (1, 2, 3)

sys.getsizeof(lista) # Más grande

sys.getsizeof(tupla) # Más optimizado
```
## ➔ Conversión entre Listas y Tuplas
```python
lista = [1, 2, 3]

tupla = tuple(lista)

nueva_lista = list(tupla)
```
## 🛠 OPERACIONES COMUNES CON TUPLAS

### Acceder a elementos
```python
tupla = (10, 20, 30, 40)

tupla[1] # 20

tupla[-1] # 40
```
### Slicing
```python
tupla[1:3] # (20, 30)
```
### Comprobar existencia
```python
20 in tupla # True

99 in tupla # False
```
### Número de elementos, ocurrencias e indices
```python
len(tupla)

tupla.count(20)

tupla.index(30)
```
### Mínimo, máximo y ordenamiento
```python
min(tupla)

max(tupla)

sorted(tupla) # devuelve una lista

reversed(tupla) # lista en orden inverso
```
## 📄 Tuplas de Tuplas

### Podemos combinar tuplas usando zip
```python
tupla1 = (1, 2, 3)

tupla2 = (a, b, c)

tupla_combinada = tuple(zip(tupla1, tupla2))

print(tupla_combinada)
```
### Podemos acceder a los elementos de una tupla de tuplas
```python
mi_tupla = ((1, 'a'), (2, 'b'), (3, 'c'))

print(mi_tupla[0][0]) # 1

print(mi_tupla[1][1]) # b

print(mi_tupla[2][0]) # 3

alumnos = (("Ana", 10), ("Luis", 8), ("Sara", 9, 10))

alumnos[0][0] # "Ana"
```
### Slicing en tuplas anidadas
```python
alumnos[1:] # (("Luis", 8), ("Sara", 9, 10))

alumnos[0:2] El 2 no está incluido, es -1 # (("Ana", 10), ("Luis", 8))

alumnos[2] [0:2] De la tercera tupla, coge el elemento 0 y el 1 # ("Sara", 9)
```
🐁 Tupla unitaria
```python
x = (5,) # ¡OJO! El uso de la coma es obligatorio

type(x) # <class 'tuple'>
```
## 🏦 Empaquetamiento y Desempaquetamiento

### Empaquetamiento

El empaquetamiento ocurre cuando agrupamos múltiples valores en una sola
tupla. Esto se hace automáticamente al asignar varios valores a una
variable o al crear una tupla explícitamente.

#### Empaquetamiento de tupla
```python
tupla = ("El aleph", "Jorge Luis Borges")

print(tupla)

# Salida: ('El aleph', 'Jorge Luis Borges')
```
### Desempaquetamiento

El desempaquetamiento ocurre cuando extraemos los valores de una tupla y
los asignamos a variables individuales. Esto se hace asignando la tupla
a un número igual de variables.

#### Desempaquetamiento de tupla
```python
titulo, autor = ("El aleph", "Jorge Luis Borges")

print(titulo)  # Salida: El aleph

print(autor)   # Salida: Jorge Luis Borges
```
-   Aquí, la tupla ("El aleph", "Jorge Luis Borges") se desempaqueta
    en las variables titulo y autor.

-   El número de variables debe coincidir con el número de elementos en
    la tupla, de lo contrario, Python lanzará un error.

### Error común
```python
nombre, edad = persona \# Error: not enough values to unpack
```
# 🐍 Conjuntos
```python
Lista: [ ]

Tupla: ( )

Set: { }
```
## ¿Qué es un SET?

Un **set** es una colección **no ordenada**, de **elementos únicos** e **inmutables**.

## Características:

-   ❌ No hay índices (no se accede con [0], [1]...)

-   ❌ No se pueden reasignar valores a los elementos.

-   ✅ Se pueden **añadir** y **eliminar** elementos.

-   ✅ No hay elementos duplicados (son únicos).

### Ejemplo:
```python
mi_set = {1, 2, 3, 3, 4}

print(mi_set) # {1, 2, 3, 4} (elimina duplicado)
```
### Ejemplo: Crear set vacío
```python
mi_set = set()
```
### Ejemplo: El orden no se preserva
```python
set_frutas = {'manzana', 'naranja', 'plátano'}

print(set_frutas) # {'naranja', 'manzana', 'plátano'}
``` 
Podemos comprobar pertenencias, usar in para ver si un elemento está dentro del set, devolverá un True o False.

Éstas pruebas de pertenencia son más eficientes con los sets que listas porqué no tienen indices.

## 🤐 ¿Por qué los sets no tienen índices?

Los **sets** no están ordenados internamente. Cada elemento tiene un **hash**, que permite a Python ubicarlo en un \"bucket\" específico.
Gracias a esto:

-   Las **búsquedas son muy rápidas**, más que en listas.

-   No tiene sentido acceder por posición, ya que el orden puede
    cambiar.

### Ejemplo:
```python
mi_set = {"a", "b", "c"}

"a" in mi_set # True
```
## ➕ Añadir elementos a un set
```python
mi_set = {1, 2, 3}

mi_set.add(4) \# {1, 2, 3, 4}
```
## ➖ Eliminar elementos de un set

### Usando remove()
```python
mi_set.remove(2) # Elimina 2

mi_set.remove(9) # ❌ Lanza error si el elemento no existe
```
### Usando discard()
```python
mi_set.discard(9) # No lanza error si no existe
```
### Diferencia entre remove() y discard()

-   remove() lanza error si no encuentra el elemento.

-   discard() simplemente no hace nada.

## 🔄 Conversión entre listas y sets
```python
mi_lista = [1, 2, 2, 3, 4, 4, 5]

mi_set = set(mi_lista) # Elimina duplicados

nueva_lista = list(mi_set) # Vuelve a convertirlo a lista
```
## 📆 Ejemplo Práctico: eliminar duplicados
```python
nombres = ["Ana", "Luis", "Ana", "Luis", "Pedro"]

nombres_unicos = list(set(nombres))

# ['Pedro', 'Luis', 'Ana'] (orden no garantizado)
```
## ⚡ OPERACIONES CON SETS

### Unión (union() o |)

Junta ambos sets eliminando duplicados.
```python
A = {1, 2, 3}

B = {3, 4, 5}

A.union(B) # {1, 2, 3, 4, 5}

A | B # {1, 2, 3, 4, 5}
```
### Intersección (intersection() o &)

Muestra únicamente elementos que haya en ambas listas de manera común.
```python
A & B # {3}

nombres_comunes = nombres1.intersection(nombres2)
```
### Diferencia (difference() o -)

Muestra los elementos que el primer set tiene pero que el segundo no
tiene, exclusivamente.
```python
A - B # {1, 2}
```
### Diferencia Simétrica (symmetric_difference() o \^)
```python
A ^ B # {1, 2, 4, 5} (elementos que están en un solo set)
```