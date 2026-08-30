class Solution:
    def isValid(self, s: str) -> bool:
        history = []

        for i in range(len(s)):
            if s[i] not in [')', ']', '}']:
                history.append(s[i])
            
            else:
                if not history:
                    return False
                
                if s[i] == ')' and history[-1] == '(':
                    history.pop(-1)
                    continue
                
                if s[i] == ']' and history[-1] == '[':
                    history.pop(-1)
                    continue
                
                if s[i] == '}' and history[-1] == '{':
                    history.pop(-1)
                    continue

                return False
                
        if history:
            return False

        return True 
        