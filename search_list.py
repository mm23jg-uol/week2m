 def search_ordered_list(lst, target):
    sorted_lst = get_ordered_list(lst)
    low = 0
    high = len(sorted_lst) - 1

    while low <= high:
        mid = (low + high) // 2
        if sorted_lst[mid] == target:
            return True
        elif sorted_lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return False
