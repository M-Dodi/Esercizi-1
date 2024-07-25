"""

def merge_sort(list):
    list_length = len(list)
    if list_length == 1:
        return list
    
    q = list_length //2  
    left = merge_sort(list[:q])
    right = merge_sort(list[q:])

    return merge(left, right)


def merge(left, right):
    ordered = []

    while left and right:
        ordered.append((left if left[0] <= right[0] else right).pop(0))

    return ordered + left + right

"""





def mergeSort(input_list: list) -> list:

    if len(input_list) == 1:
        return input_list

    mid_point: int = len(input_list) // 2
    mergeSort(input_list = input_list[:mid_point])
    mergeSort(input_list = input_list[mid_point:])


def merge(list_1: list[int], list_2: list[int]) -> list[int]:

    i, j = 0, 0, 0
    result: list[int] = [None for _ in range(len(list_1 + list_2))]
    
    for k in range(len(result)):
        if list_1[i] > list_2[j]:

            result[k] = list_2[j]   
            j += 1
        else:

            result[k]  = list_1[i] 
            i += 1  
    return result

input_list: list[int] = (0, 1, 2, 3, 4, 5, 6, 7)

print(mergeSort(input_list))


    


   


