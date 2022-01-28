def dimensoes(m):
    lin = len(m)
    col = len(m[0])
    return (print("{}{}".format(lin,col)))

import pytest

@pytest.mark.parametrize("entrada, esperado", [
    ([[1], [2], [3]], 31)
    ])
def testa_dimensoes(entrada, esperado):
    assert dimensoes(entrada) == esperado
    
    
    
