class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        close={"]",")","}"}
        L=[{"[","]"},{"(",")"},{"{","}"}]
        for i in s:
            if i not in close:
                stack.append(i)
            else:
                if stack:
                    last=stack.pop()
                    if {last,i} not in L:
                        return False
                else:
                    return False
        if stack:
            return False
        return True
        