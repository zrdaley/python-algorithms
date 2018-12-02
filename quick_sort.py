def quick_sort(arr, l, h):
  if l < h:
    p = partition(arr, l, h)
    quick_sort(arr, l, p - 1)
    quick_sort(arr, p + 1, h)

def partition(arr, l, h):
  p = l
  for j in range(l+1, h+1):
    if arr[j] <= arr[l]:
      p += 1
      arr[j], arr[p] = arr[p], arr[j]
  arr[l], arr[p] = arr[p], arr[l]
  return p


array = [3, 2, 1, 5, 7, 9]
quick_sort(array, 0, len(array)-1)
print array
