# origin quick sort

arr = list(map(int, input().split))

def origin_quick_sort(array, start_index, end_index):
  if start_index >= end_index:
    return
  pivot = start_index
  left_index = start_index + 1
  right_index = end_index

  while left_index <= right_index:
    while left_index <= end_index and array[left_index] <= array[pivot]:
      left_index += 1
    while right_index > start_index and array[right_index] >= array[pivot]:
      right_index -= 1
    
    if left_index > right_index:
      array[right_index], array[pivot] = array[pivot], array[right_index]
    else: 
      array[left_index], array[right_index] = array[right_index], array[left_index]
  
  origin_quick_sort(array, start_index, right_index - 1)
  origin_quick_sort(array, right_index + 1, end_index)


origin_quick_sort(arr, 0, len(arr) - 1)

# python quick sort

arr = list(map(int, input().split))

def python_quick_sort(array):
  if len(array) <= 1:
    return array
  
  pivot = array[0]
  tail = array[1:]

  left_side = [x for x in tail if x <= pivot]
  right_side = [x for x in tail if x > pivot]

  return python_quick_sort(left_side) + [pivot] + python_quick_sort(right_side)
