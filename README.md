# Example Package Metaheurísticas

Paquete Python para el cálculo de distancias en espacios multidimensionales, desarrollado como parte del curso de Metaheurísticas.

## Descripción

Este proyecto implementa funciones de cálculo de distancias utilizadas en algoritmos de metaheurísticas. Actualmente incluye la implementación de la **Distancia Manhattan**.

## Requisitos

- Python >= 3.9
- numpy

## Instalación

```bash
pip install -e .
```

## Estructura del Proyecto

```
Repositorio.Test/
├── LICENSE                 # Licencia MIT
├── README.md              # Este archivo
├── pyproject.toml         # Configuración del proyecto
├── src/
│   └── paquete1/
│       ├── __init__.py
│       └── manhattan.py   # Implementación de distancia Manhattan
└── tests/
    ├── __init__.py
    └── test_manhattan.py  # Pruebas unitarias
```

## Módulos

### paquete1.manhattan

#### `md(A, B) -> float`

Calcula la distancia Manhattan entre dos vectores n-dimensionales.

**Parámetros:**
- `A` (numpy.ndarray): Vector n-dimensional 1
- `B` (numpy.ndarray): Vector n-dimensional 2

**Retorna:**
- `float`: Suma absoluta de las diferencias elemento a elemento: |a₀-b₀| + ... + |aₙ-bₙ|

**Ejemplo:**
```python
import numpy as np
from paquete1.manhattan import md

A = np.array([1, 2, 3, 4])
B = np.array([5, 6, 7, 8])
distancia = md(A, B)  # Resultado: 16
```

## Pruebas

Para ejecutar las pruebas unitarias:

```bash
pytest tests/
```

O ejecutar pruebas específicas:

```bash
pytest tests/test_manhattan.py -v
```

## Autores

- **Enrique Anael Gómez Linares** - enrique.gomez@edu.uaa.mx
- **Victoria Galván Delgadillo** - galvand.victoria@gmail.com

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

## Enlaces

- [Repositorio GitHub](https://github.com/galvandvictoria-alt/Repositorio.Test)