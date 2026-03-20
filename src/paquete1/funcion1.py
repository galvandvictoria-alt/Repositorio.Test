import numpy as np

def md(A:np.ndarray, B:np.ndarray) -> float:
    """
    Calcula la distancia Manhattan entre dos vectores
    Args: 
        A (array): Vector n dimensional 1
        B (array): Vector n dimensional 2
    Return:
        float: |(a0-b0)+...+(a_n-b_n)|
    """
    return np.abs(np.sum(A-B))

md()