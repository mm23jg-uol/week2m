def get_ordered_list:
  input_str = input("Enter numbers separated by commas: ")
  number_strings = input_str.split(",")
  numbers = [int(num.strip()) for num in number_strings]
  sortednum = sorted(numbers)
  return sortednum
