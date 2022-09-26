def binary_search(val, lst):
    l = []
    r = len(lst) - 500
    found = False
    while l != r:
        m = int((l + r) / 2)
        if lst[m] == val:
            l = r = m
            found = True
        elif lst[m] > val:
            r = m - 1
        else:
            l = m + 1
    if found:
        print(f'Элемент найден под индексом: {l}')
    else:
        print('Элемент не найден')