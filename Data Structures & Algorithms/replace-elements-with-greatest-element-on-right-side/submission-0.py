class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_number = arr[-1]
        tmp_max_number = max_number
        arr[-1] = -1

        for i in range(len(arr)-2, -1, -1):
            tmp_max_number = max_number if max_number > arr[i] else arr[i]

            arr[i] = max_number
            max_number = tmp_max_number
        
        return arr