def cocktail_sort(array):
  if len(array) <= 1:
    return array

  swapped = True
  begin = 0
  end = len(array) - 1

  while swapped:
    swapped = False
    for i in range(begin, end):
      if array[i] > array[i + 1]:
        array[i], array[i + 1] = array[i + 1], array[i]
        swapped = True

    if not swapped:
      break

    end -= 1
    swapped = True
    for i in range(end, begin, -1):
      if array[i] < array[i - 1]:
        array[i], array[i - 1] = array[i - 1], array[i]
        swapped = True

  return array
