# ruff

Algoritmo de maximización de paneles solares
-------------------------------------------

Este código en Python implementa un algoritmo para calcular la máxima cantidad de paneles solares rectangulares que se pueden colocar en un techo rectangular, dado las dimensiones de los paneles y las dimensiones del techo.

La función principal `max_paneles(a, b, x, y)` recibe cuatro parámetros:
- `a` y `b`: las dimensiones del panel solar (ancho y alto)
- `x` e `y`: las dimensiones del techo (ancho y alto)

El algoritmo considera dos orientaciones posibles para colocar los paneles: horizontal y vertical. Calcula la cantidad máxima de paneles que caben en cada orientación y devuelve el valor máximo.

La lógica del algoritmo es la siguiente:
1. Se asegura de que las dimensiones estén en el orden correcto (`a <= b` y `x <= y`).
2. Calcula la cantidad de paneles que caben en orientación horizontal dividiendo las dimensiones del techo por las dimensiones correspondientes del panel.
3. Calcula la cantidad de paneles que caben en orientación vertical de manera similar.
4. Devuelve la cantidad máxima de paneles que caben entre las dos orientaciones.

Este código es una solución eficiente y sencilla para el problema de maximizar la cantidad de paneles solares que se pueden colocar en un techo rectangular, y puede ser utilizado como base para resolver problemas similares.
