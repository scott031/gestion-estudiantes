def maxima_nota(notas):
    if not notas:
        return None
    
    for n in notas:
        if n < 0 or n > 5:
            raise ValueError("Las notas deben estar entre 0 y 5")
    
    return max(notas)
