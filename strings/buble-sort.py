nums1 = [5,3,8,6,7,2]
nums = [5,3,8,6,7,2]

nums1.sort()
print(nums1)
print(nums)

def sort(unsortedList):
    for i in range(len(unsortedList) - 1, 0, -1):
        for j in range(i):
              if unsortedList[j] > unsortedList[j+1]:
                  temp = unsortedList[j]
                  unsortedList[j] = unsortedList[j+1]
                  unsortedList[j+1]= temp

sort(nums) 
print(nums1)
print(nums)

