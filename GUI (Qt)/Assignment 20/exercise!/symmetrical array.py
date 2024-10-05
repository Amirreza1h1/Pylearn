def is_symmetrical(arr):
    if len(arr) <= 1:
        return True
    
    left = 0
    right = len(arr) - 1
    
    while left < right:
        if arr[left] != arr[right]:
            return False
        
        left += 1
        right -= 1
    
    return True

print(is_symmetrical([1,3,4,3,1]))
print(is_symmetrical([3,2,1]))