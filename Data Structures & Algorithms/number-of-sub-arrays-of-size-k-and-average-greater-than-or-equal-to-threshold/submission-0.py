class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        L = 0
        currSum = sum(arr[:k-1])
        count = 0

        for R in range(k - 1, len(arr)):
            if R - L + 1 > k:
                currSum -= arr[L]
                L += 1
            
            currSum += arr[R]
            mean = currSum / k
            if mean >= threshold:
                count += 1

        return count