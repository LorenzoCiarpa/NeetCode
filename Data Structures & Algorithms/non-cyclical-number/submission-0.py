class Solution:
    def isHappy(self, n: int) -> bool:
        visit = set()
        newElem = n

        while newElem != 1:
            if newElem in visit:
                return False
            visit.add(newElem)

            s = str(newElem)
            newElem = 0

            for elem in s:
                newElem += int(elem) ** 2
        return True
        