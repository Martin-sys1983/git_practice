def append_sum(lst):
    lst.append(lst[-2] + lst[-1])
    lst.append(lst[-2] + lst[-1])
    lst.append(lst[-2] + lst[-1])
    lst.append(lst[-2] + lst[-1])
    return lst
print(append_sum([1, 1, 2]))

def larger_list(lst1, lst2):
    if len(lst1) > len(lst2):
        return lst1[-1]
    if len(lst1) < len(lst2):
        return lst2[-1] 
    if len(lst1) == len(lst2):
        return lst1[-1]
print(larger_list([4, 10, 2, 5], [-10, 2, 5, 10]))

def more_than_n(lst, item, n):
    if lst.count(item) > n:
        return True
    else:
        return False
    
print(more_than_n([2, 4, 6, 2, 3, 2, 1, 2], 2, 3))


def append_size(lst):
    lst.append(len(lst))
    return lst          
    print(lst)    
print(append_size([23, 42, 108]))

def combine_sort(lst1, lst2):
    new_list = lst1 + lst2
    sorted_list = sorted(new_list)
    return sorted_list
print(combine_sort([4, 10, 2, 5], [-10, 2, 5, 10]))







