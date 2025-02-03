def get_ordered_list:
  input_str = input("Enter numbers separated by commas: ")
  number_strings = input_str.split(",")
  numbers = [int(num.strip()) for num in number_strings]
  sortednum = sorted(numbers)
  return sortednum
from ordered_list import get_ordered_list  # Import the function from ordered_list.py

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
