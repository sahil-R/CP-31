from typing import *
class Solution:
    def recurse(self,lastoperand,lastoperator,total,target,string,expression,ans):
        print(lastoperand,lastoperator,total,target,string,expression,ans)
        if len(string)==0:
            if total==target:
                # print(expression[:-1])
                exp=expression.copy()
                exp=exp[:-1]
                ans.append(''.join(exp))
                return
        else:
            item=int(string[0])
            string=string[1:]
            expression1=expression.copy()
            expression2=expression.copy()
            expression3=expression.copy()
            totaltemp=total
            for i in range(3):
                if i==0:
                    #multiplication
                    if lastoperand=="+" and len(expression)!=2:
                        totaltemp=total-lastoperator
                        totaltemp+=lastoperator*item
                    elif lastoperand=="-" and len(expression)!=2:
                        totaltemp+=lastoperator
                        totaltemp-=lastoperator*item
                    else:
                        totaltemp*=item
                    expression1.append(str(item))
                    expression1.append("*")
                    self.recurse(item,"*",totaltemp,target,string,expression1,ans)
                if i==1:
                    print("here")
                    totaltemp+=item
                    expression2.append(str(item))
                    expression2.append("+")
                    self.recurse(item,"+",totaltemp,target,string,expression1,ans)
                if i==2:
                    totaltemp-=item
                    expression3.append(str(item))
                    expression3.append("-")
                    self.recurse(item,"-",totaltemp,target,string,expression1,ans)

    def addOperators(self, num: str, target: int) -> List[str]:
        ans=[]
        self.recurse(0,"=",0,target,num,[],ans)
        return ans
    
s=Solution()
s.addOperators("123",6)