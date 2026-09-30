class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x=0
        arr1=[]
        arr2=[]
        for i in range(len(nums)):
            if i<n:
                arr1.append(nums[i])
            else:
                arr2.append(nums[i])

        j=0
        for i in range(n):        
            nums[j]=arr1[i]
            j+=1
            nums[j]=arr2[i]
            j+=1

        return nums
