#Generate Parentheses

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        parantheses = []
        
        def solution(opening=n, closing=n, string = ""):
            if opening==0 and closing ==0:
                parantheses.append(string)
        
            if opening>0:
                solution(opening-1, closing, string+"(")
        
            if closing>opening:
                solution(opening, closing-1, string+")")
                
        solution()
        return parantheses
