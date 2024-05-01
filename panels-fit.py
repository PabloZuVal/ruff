def max_paneles(a, b, x, y):
    # Intercambiar dimensiones si es necesario para asegurar que a <= b y x <= y
    if a > b:
        a, b = b, a
    if x > y:
        x, y = y, x

    # Calcular la cantidad de paneles que caben en cada orientación
    horizontal = (x // a) * (y // b)
    vertical = (x // b) * (y // a)

    # Retornar la máxima cantidad de paneles que caben
    return max(horizontal, vertical)

print(max_paneles(1, 2, 2, 4))
print(max_paneles(1, 2, 3, 5))
print(max_paneles(2, 2, 1, 10))
