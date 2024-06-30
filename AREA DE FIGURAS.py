# Programa para calcular el área de un rectángulo

# Función para calcular el área
def calcular_area(ancho, alto):
    """
    Calcula el área de un rectángulo dado su ancho y alto.

    :param ancho: Ancho del rectángulo (float or int)
    :param alto: Alto del rectángulo (float or int)
    :return: El área del rectángulo (float)
    """
    area = ancho * alto
    return area

# Variables de ejemplo
width = 5
height = 10

# Calcular el área del rectángulo
area_rectangulo = calcular_area(width, height)

# Imprimir el resultado
print(f"El área del rectángulo con ancho {width} y alto {height} es: {area_rectangulo}")