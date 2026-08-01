class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        fin = len(nums)
        while k < fin:
            if nums[k] == val:
                for i in range(k, fin):
                    if i+1 < fin:
                        nums[i] = nums[i+1]
                fin -= 1
            else:
                k += 1
        return k
