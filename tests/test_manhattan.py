import numpy as np
import pytest
from src.paquete1.funcion1 import md

@pytest.mark.parametrize("input_a, input_b, expected_result", [
    (np.array([1,2,3,4]), np.array([5,6,7,8]), 16)
])
def test_answer(input_a, input_b, expected_result):
    result = md(input_a, input_b)
    np.testing.assert_allclose(result, expected_result)