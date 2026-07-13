class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op={'+','-','*','/'}
        stack=[]
        for x in tokens:
            if x not in op:
                stack.append(int(x))
            else:
                m=stack.pop()
                print(m)
                n=stack.pop()
                print(n)
                r=0
                if x=="+":
                    r=m+n
                elif x=="-":
                    r=n-m
                elif x=="*":
                    r=m*n
                else:
                    r=int(n/m)
                print(r)
                stack.append(r)
        return stack.pop()
            