def binary_search(sorted_list, val, s, n):
  if n >= s:
    mid = s + ((n - s)/2)
    middle = sorted_list[mid]
    if val > middle:
      return binary_search(sorted_list, val, mid+1, n)
    elif val < middle:
      return binary_search(sorted_list, val, s, mid-1)
    else:
      return mid
  else:
    return -1

l = [1, 2, 3, 4, 5, 6, 7]
print binary_search(l, 2, 0, len(l)-1)
