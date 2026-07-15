class Solution:
    def isValid(self, s: str) -> bool:
        hashmap = { "}":"{" , "]":'[',")":'('}
        stack = []

        for i in s:
            if i not in hashmap :
            #its an open bracket 
                stack.append(i)
            else:
                if len(stack) == 0 :
                    return False
                else:
                    pop = stack.pop()
                    if pop != hashmap[i]:
                        return False
        return not stack


        

      