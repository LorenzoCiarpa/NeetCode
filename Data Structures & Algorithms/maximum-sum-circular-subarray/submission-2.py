class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        total = 0
        curr_max = 0
        max_sum = nums[0]
        curr_min = 0
        min_sum = nums[0]
        
        for num in nums:
            # Calcola il massimo sotto-array (Kadane classico)
            curr_max = max(curr_max + num, num)
            max_sum = max(max_sum, curr_max)
            
            # Calcola il minimo sotto-array (Kadane invertito)
            curr_min = min(curr_min + num, num)
            min_sum = min(min_sum, curr_min)
            
            # Calcola la somma totale
            total += num
            
        # Se tutti i numeri sono negativi, ritorna max_sum
        if max_sum < 0:
            return max_sum
            
        # Altrimenti, ritorna il massimo tra il Caso 1 e il Caso 2
        return max(max_sum, total - min_sum)