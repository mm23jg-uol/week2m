 def search_ordered_list(lst, target):
    sorted_lst = get_ordered_list(lst)
    low = 0
    high = length of sorted_lst - 1
     low <= high DO:
        mid = (low + high) // 2
        IF sorted_lst[mid] equals target THEN:
            RETURN True
        ELSE IF sorted_lst[mid] < target THEN:
             low = mid + 1
        ELSE:
             high = mid - 1
   
    RETURN False
