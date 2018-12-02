def mergeSort(l):
  n = len(l)
  if n > 1:
    left = l[:n/2]
    right = l[n/2:]

    mergeSort(left)
    mergeSort(right)
  
    i = 0
    j = 0
    k = 0
    while i < len(left) and j < len(right):
      if left[i] > right[j]:
        l[k] = right[j]
        j += 1
      else:
        l[k] = left[i]
        i += 1
      k += 1

    while i < len(left):
      l[k] = left[i]
      k += 1
      i += 1
    
    while j < len(right):
      l[k] = right[j]
      k += 1
      j += 1

l = [1,2,5,3,8,9,3,2,1]
mergeSort(l)
print l
    
    
    