#! python3
# - Convertir cada elemento de list1 en llave de dict1
# - Revisar si los elementos de list2 alguno es llave de dict1
# - Cada elemento que sea llave en dict1, añadir a list_instersect
import time, datetime, random
import intersection
num_elements = 1_000_000
arr_a = [random.randint(0, num_elements) for i in range(num_elements)]
arr_b = [random.randint(0, num_elements) for j in range(num_elements)]

def intersection_dict(arr1, arr2):
    start = time.time()
    dict_from_list = {}
    intersection = []
    for key in arr1:
        dict_from_list[key] = 1

    for key in arr2:
        try:
            dict_from_list[key]
            intersection.append(key)
        except:
            pass

    elapsed = time.time() - start
    print(f'Took {str(datetime.timedelta(seconds=elapsed))} time to finish')
    #print(intersection)

# start = time.time()
# intersection.same_elements(arr_a, arr_b)
# elapsed = time.time() - start
# print(f'Took {str(datetime.timedelta(seconds=elapsed))} time to finish')


intersection_dict(arr_a, arr_b)