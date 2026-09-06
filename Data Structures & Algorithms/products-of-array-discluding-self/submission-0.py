class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefixProd, postfixProd = [0]*len(nums), [0]*len(nums)

        currentProd = 1
        for i in range(1, len(prefixProd)):
            currentProd *= nums[i-1]
            prefixProd[i] = currentProd
        
        currentProd = 1
        for i in range(len(postfixProd) - 2, -1, -1):
            currentProd *= nums[i+1]
            postfixProd[i] = currentProd
        
        prefixProd[0] = postfixProd [-1] = 1
        result = []
        for i in range(len(nums)):
            result.append(prefixProd[i] * postfixProd[i])
        
        return result