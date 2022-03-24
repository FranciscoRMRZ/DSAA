#! python3
# Escribir una función que tome dos arreglos y devuelva una arreglo que
# contenga los datos de su intersección

def same_elements(arr_a, arr_b):
    intersection = []
    for element in arr_a:
        if element in arr_b and element not in intersection:
            intersection.append(element)
    
    return sorted(intersection)

def same_elements_alternative(arr_a, arr_b):
    intersection = []
    for element_a in arr_a:
        for element_b in arr_b:
            if element_a == element_b and element_a not in intersection:
                intersection.append(element_a)

    return sorted(intersection)

def same_elements_with_sets(arr_a, arr_b):
    return sorted(list(set(arr_a).intersection(set(arr_b))))

def same_elements_with_comprehension(arr_a, arr_b):
    return sorted([element for element in set(arr_a) if element in set(arr_b)])




