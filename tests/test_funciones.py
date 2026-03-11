from src.funciones import maxima_nota

def test_maxima_normal():
    notas = [3, 4.5, 2, 5]
    assert maxima_nota(notas) == 5

def test_maxima_vacio():
    notas = []
    assert maxima_nota(notas) == None

def test_maxima_rango():
    notas = [0, 1, 2, 3, 4, 5]
    assert maxima_nota(notas) == 5