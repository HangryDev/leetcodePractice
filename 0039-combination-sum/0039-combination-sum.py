class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = [] 
        self.dfs(candidates, target, [], answer)
        return answer 

    def dfs(self, candidates, currentVal, path, answer):
        # currentVal < 0 : return false 
        if currentVal < 0 :
            return
        # currentVal == 0 : return true. 경로 저장 
        if currentVal == 0 :
            answer.append(path)
            return answer
        # else (target > 0): 
        # brute force로 접근. candidates에서 하나씩 다 뺀다. 
        for i in range(len(candidates)):
            self.dfs(candidates[i:], currentVal -candidates[i], path+[candidates[i]], answer) 


