class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ops = []

        for op in operations:
            if op.lstrip('-').isnumeric():
                ops.append(int(op))

            elif op == '+':
                ops.append(ops[-1] + ops[-2])
            
            elif op == 'C':
                ops.pop()
            
            elif op == 'D':
                ops.append(ops[-1]*2)
        return sum(ops)