class MergeArrays:
    def mergeSortedLists(self, nums1, m, nums2, n):
        for i in range(n): # join lists in-place in nums1
            nums1[m+i]=nums2[i-n]
        noSwaps = False
        for i in reversed(range(m+n)): # bubble sort here with no-swaps check
            noSwaps=True
            for j in range(i):
                if (nums1[j]>nums1[j+1]):
                    temp = nums1[j+1]
                    nums1[j+1]=nums1[j]
                    nums1[j]=temp
                    noSwaps=False
            if(noSwaps):
                break
        return nums1
    def merge(self, nums1, m, nums2, n):
        if m == 0 or len(list(filter(lambda num: num > 0, nums1))) == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        elif n > 0:
            tempArr = []
            index1 = 0
            index2 = 0
            while(index1 < m or index2 < n):
                if (nums1[index1] > 0 and nums1[index1] <= nums2[index2]):
                    tempArr.append(nums1[index1])
                    index1+=1
                else:
                    tempArr.append(nums2[index2])
                    index2+=1
            for i in range(m+n):
                nums1[i] = tempArr[i]
        return nums1